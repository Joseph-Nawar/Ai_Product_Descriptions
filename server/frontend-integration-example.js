// server/frontend-integration-example.js
// Example of how to integrate the subscription system with your frontend

class SubscriptionService {
  constructor(apiBaseUrl = 'http://localhost:3001/api') {
    this.apiBaseUrl = apiBaseUrl;
  }

  // Get user's current plan and usage
  async getUserInfo(email) {
    try {
      const response = await fetch(`${this.apiBaseUrl}/user/${email}`);
      if (!response.ok) {
        throw new Error('Failed to get user info');
      }
      return await response.json();
    } catch (error) {
      console.error('Error getting user info:', error);
      return null;
    }
  }

  // Check if user can generate descriptions
  async canGenerateDescriptions(email, batchSize = 1) {
    try {
      const response = await fetch(`${this.apiBaseUrl}/check-usage`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email,
          action: 'generate_description',
          metadata: { batch_size: batchSize }
        })
      });
      return await response.json();
    } catch (error) {
      console.error('Error checking usage:', error);
      return { allowed: false, reason: 'Network error' };
    }
  }

  // Check if user can regenerate a description
  async canRegenerateDescription(email, descriptionId) {
    try {
      const response = await fetch(`${this.apiBaseUrl}/check-usage`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email,
          action: 'regenerate_description',
          metadata: { description_id: descriptionId }
        })
      });
      return await response.json();
    } catch (error) {
      console.error('Error checking regeneration:', error);
      return { allowed: false, reason: 'Network error' };
    }
  }

  // Record usage after successful generation
  async recordUsage(email, action, count = 1, metadata = {}) {
    try {
      const response = await fetch(`${this.apiBaseUrl}/record-usage`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email,
          action,
          count,
          metadata
        })
      });
      return await response.json();
    } catch (error) {
      console.error('Error recording usage:', error);
      return { success: false };
    }
  }
}

// React component example
const GenerateDescriptionComponent = ({ userEmail }) => {
  const [userInfo, setUserInfo] = useState(null);
  const [isGenerating, setIsGenerating] = useState(false);
  const [batchSize, setBatchSize] = useState(1);
  const subscriptionService = new SubscriptionService();

  useEffect(() => {
    // Load user info on component mount
    subscriptionService.getUserInfo(userEmail).then(setUserInfo);
  }, [userEmail]);

  const handleGenerate = async () => {
    // Check if user can generate
    const canGenerate = await subscriptionService.canGenerateDescriptions(userEmail, batchSize);
    
    if (!canGenerate.allowed) {
      alert(canGenerate.reason);
      if (canGenerate.upgrade_required) {
        // Redirect to upgrade page
        window.location.href = '/pricing';
      }
      return;
    }

    setIsGenerating(true);
    
    try {
      // Generate descriptions (your AI logic here)
      const descriptions = await generateAIDescriptions(batchSize);
      
      // Record usage
      await subscriptionService.recordUsage(userEmail, 'generate_description', batchSize);
      
      // Update user info
      const updatedInfo = await subscriptionService.getUserInfo(userEmail);
      setUserInfo(updatedInfo);
      
      // Show results
      console.log('Generated descriptions:', descriptions);
      
    } catch (error) {
      console.error('Error generating descriptions:', error);
      alert('Failed to generate descriptions');
    } finally {
      setIsGenerating(false);
    }
  };

  const handleRegenerate = async (descriptionId) => {
    // Check if user can regenerate
    const canRegenerate = await subscriptionService.canRegenerateDescription(userEmail, descriptionId);
    
    if (!canRegenerate.allowed) {
      alert(canRegenerate.reason);
      if (canRegenerate.upgrade_required) {
        window.location.href = '/pricing';
      }
      return;
    }

    try {
      // Regenerate description
      const newDescription = await regenerateAIDescription(descriptionId);
      
      // Record usage
      await subscriptionService.recordUsage(userEmail, 'regenerate_description', 1, { description_id: descriptionId });
      
      // Update user info
      const updatedInfo = await subscriptionService.getUserInfo(userEmail);
      setUserInfo(updatedInfo);
      
      console.log('Regenerated description:', newDescription);
      
    } catch (error) {
      console.error('Error regenerating description:', error);
      alert('Failed to regenerate description');
    }
  };

  if (!userInfo) {
    return <div>Loading user info...</div>;
  }

  return (
    <div className="generate-description">
      {/* Usage Display */}
      <div className="usage-info">
        <h3>Your Plan: {userInfo.plan}</h3>
        <p>
          Descriptions: {userInfo.usage.descriptions_used} / {userInfo.usage.descriptions_limit}
          ({userInfo.usage.descriptions_remaining} remaining)
        </p>
        <p>Max batch size: {userInfo.usage.max_batch_size}</p>
        <p>Regenerations per description: {userInfo.usage.regenerations_per_description === -1 ? 'Unlimited' : userInfo.usage.regenerations_per_description}</p>
      </div>

      {/* Generation Controls */}
      <div className="generation-controls">
        <label>
          Batch Size:
          <input
            type="number"
            min="1"
            max={userInfo.usage.max_batch_size}
            value={batchSize}
            onChange={(e) => setBatchSize(parseInt(e.target.value))}
          />
        </label>
        
        <button 
          onClick={handleGenerate}
          disabled={isGenerating || userInfo.usage.descriptions_remaining === 0}
        >
          {isGenerating ? 'Generating...' : 'Generate Descriptions'}
        </button>
        
        {userInfo.usage.descriptions_remaining === 0 && (
          <div className="upgrade-prompt">
            <p>You've reached your monthly limit!</p>
            <button onClick={() => window.location.href = '/pricing'}>
              Upgrade Plan
            </button>
          </div>
        )}
      </div>

      {/* Features Display */}
      <div className="features">
        <h4>Your Features:</h4>
        <ul>
          {userInfo.features.map(feature => (
            <li key={feature}>{feature.replace(/_/g, ' ')}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

// Usage in your main app
const App = () => {
  const [userEmail, setUserEmail] = useState('user@example.com'); // Get from auth
  
  return (
    <div className="app">
      <GenerateDescriptionComponent userEmail={userEmail} />
    </div>
  );
};

module.exports = { SubscriptionService, GenerateDescriptionComponent };


