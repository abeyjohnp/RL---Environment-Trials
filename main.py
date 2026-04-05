import gymnasium as gym
from gymnasium import spaces

class TreasureHuntEnv(gym.Env):
    def __init__(self):
        super().__init__()
        self.action_space = spaces.Discrete(2) #chooses among 0 1
        self.observation_space= spaces.Discrete(5) #chooses among 0- 4
        self.agent_position = 0
        self.goal_position = 4
        #so if algo comes it first checks for the action space
        #and the observation space, so that it can construct the brain of the correct size

    def reset(self, seed=None):
        super().reset(seed=seed)
        """
        A seed is just a number like say seed =42, it locks down that mathematical
        randomness, if you run code today with seed = 42 and even next week with same seed 42
        you eventually are able to recreate the exact random events that occured.
        Therefore seed = None, is just giving the user of your environment the power 
        to say "Restart the game, and lock the randomness to the number 42."
        """
        
        
        # 1. Put the agent back at the starting square
        self.agent_position = 0
        
        # 2. Get the current observation (where the agent is right now)
        observation = self.agent_position
        
        # 3. Create an empty dictionary for extra information
        info = {}
        
        # 4. Return the observation and info (Required by Gym)
        return observation, info

    def step(self, action):
        # 1. APPLY THE ACTION
        # action is 0 (move left) or 1 (move right)
        if action == 1:
            self.agent_position += 1
        elif action == 0:
            self.agent_position -= 1
            
        # Prevent the agent from walking off the edge of our 5-space track!
        
        if self.agent_position < 0:
            self.agent_position = 0
        if self.agent_position > 4:
            self.agent_position = 4
            
        # 2. CAPTURE THE NEW OBSERVATION
        observation = self.agent_position
        
        # 3. CALCULATE REWARD & CHECK IF DONE (TERMINATED)
        if self.agent_position == self.goal_position:
            # They found the treasure!
            reward = 10.0
            terminated = True
        else:
            # They just took a normal step. Give a negative reward so 
            # the AI learns to reach the treasure as fast as possible!
            reward = -1.0 
            terminated = False
            
        # 4. TRUNCATED (Time Limit)
        # We aren't implementing a time limit in this basic example.
        truncated = False 
        
        # 5. INFO
        info = {}
        
        # 6. RETURN ALL 5 VALUES (Required by Modern Gymnasium)
        return observation, reward, terminated, truncated, info

if __name__ == "__main__":
    # 1. Create the environment from our Blueprint
    env = TreasureHuntEnv()
    
    # 2. Start a new Episode
    obs, info = env.reset()
    print(f"Game Started! Agent is at position: {obs}")
    
    total_score = 0
    
    # 3. We are going to force the agent to walk Right (Action 1) exactly 5 times
    for step_number in range(1, 6):
        print(f"\n--- Step {step_number} ---")
        action = 1 # 1 means move right
        print(f"Action Taken: Move Right (1)")
        
        # 4. Feed the action into the environment!
        obs, reward, terminated, truncated, info = env.step(action)
        
        total_score += reward
        print(f"New Position: {obs} | Reward: {reward}")
        
        # 5. Check if the game is telling us we won
        if terminated:
            print(f">>> TREASURE FOUND! Total Score: {total_score}")
            break

