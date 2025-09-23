// frontend/src/auth/token.ts
import { auth } from './firebase';

let _token: string | null = null;
export const setIdToken = (t: string | null) => { _token = t; };

export const getIdToken = async (): Promise<string | null> => {
  // Always get fresh token from Firebase
  const user = auth.currentUser;
  if (!user) {
    console.warn('No authenticated user found');
    return null;
  }
  
  try {
    const token = await user.getIdToken();
    if (!token || token.split('.').length !== 3) {
      console.error('Invalid token format:', token);
      return null;
    }
    return token;
  } catch (error) {
    console.error('Failed to get ID token:', error);
    return null;
  }
};
