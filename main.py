import gymnasium as gym
from gymnasium import spaces

class TresureHuntEnv(gym.Env):
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
