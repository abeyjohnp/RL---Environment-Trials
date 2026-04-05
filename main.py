import gymnasium as gym
from gymnasium import spaces

class TresureHuntEnv(gym.Env):
    def __init__(self):
        super().__init__()
        self.action_space = spaces.Discrete(2)
        self.observation_space= spaces.Discrete(5)
        self.agent_position = 0
        self.goal_position = 4