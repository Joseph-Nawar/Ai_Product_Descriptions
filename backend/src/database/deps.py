# backend/src/database/deps.py
"""
FastAPI database dependencies for session-per-request pattern
"""

import logging
from typing import Generator
from fastapi import Depends
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy.pool import StaticPool

from .connection import get_engine

logger = logging.getLogger(__name__)

# Create a scoped session factory for thread-safe session management
def get_session_factory():
    """Get thread-safe session factory"""
    engine = get_engine()
    
    # For SQLite, use StaticPool with proper configuration
    if engine.url.drivername == 'sqlite':
        # Create a new engine with proper SQLite configuration for concurrent access
        from sqlalchemy import create_engine
        engine = create_engine(
            engine.url,
            poolclass=StaticPool,
            connect_args={
                "check_same_thread": False,
                "timeout": 30,  # 30 second timeout for locks
            },
            pool_pre_ping=True,
            echo=False
        )
    
    # Create scoped session factory for thread safety
    session_factory = sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False,
        expire_on_commit=False
    )
    
    return scoped_session(session_factory)

# Global scoped session factory
_session_factory = None

def get_session_factory_singleton():
    """Get singleton session factory"""
    global _session_factory
    if _session_factory is None:
        _session_factory = get_session_factory()
    return _session_factory

def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency that provides a database session per request.
    Ensures proper session cleanup and thread safety.
    """
    session_factory = get_session_factory_singleton()
    db = session_factory()
    
    try:
        yield db
        # Always try to commit - let SQLAlchemy handle the state
        try:
            db.commit()
            logger.debug("Database session committed successfully")
        except Exception as commit_error:
            logger.warning(f"Commit failed (may be expected): {str(commit_error)}")
    except Exception as e:
        # Always try to rollback on error
        try:
            db.rollback()
            logger.debug("Database session rolled back successfully")
        except Exception as rollback_error:
            logger.warning(f"Rollback failed: {str(rollback_error)}")
        logger.error(f"Database session error: {str(e)}")
        raise
    finally:
        # Always try to close the session
        try:
            db.close()
            logger.debug("Database session closed")
        except Exception as close_error:
            logger.warning(f"Close failed: {str(close_error)}")
        # Always try to remove from registry
        try:
            session_factory.remove()
        except Exception as remove_error:
            logger.warning(f"Remove from registry failed: {str(remove_error)}")

def get_db_session() -> Generator[Session, None, None]:
    """
    Alternative dependency for cases where you need a session without FastAPI dependency injection.
    Use with caution - ensure proper cleanup.
    """
    session_factory = get_session_factory_singleton()
    db = session_factory()
    
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        logger.error(f"Database session error: {str(e)}")
        raise
    finally:
        db.close()
        session_factory.remove()

