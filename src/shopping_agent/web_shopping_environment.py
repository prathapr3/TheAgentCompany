import gymnasium as gym
from gymnasium import spaces
import numpy as np
from playwright_interface import PlaywrightHandler
class WebShoppingEnvironment(gym.Env):
    def __init__(self, url: str):
        print("WebShoppingEnvironment initialized.")
        super().__init__()

        # Define observation space
        self.observation_space = spaces.Box(low=0, high=255, shape=(84, 84, 3), dtype=np.uint8) # Not sure why we need this

        # Define action space
        self.action_space = spaces.Discrete(4) # Example: 4 discrete actions

        # Initialize environment-specific variables
        self.current_state = None
        self.current_step = 0
        self.home_url = url
        self.max_episode_steps = 100

        # Initialize the playwright handler or any other web interaction tool here and initiatialize the first state
        self.browser_handler = PlaywrightHandler()
        self.browser_handler.navigate_to(url)

    def _get_obs(self):
        print("Getting observation.")
        # Return the current observation
        self.current_state = self.browser_handler.capture_current_state()

        return self.current_state

    def _get_info(self):
        # Return any auxiliary information (optional)
        print("Getting info.")
        return {"current_step": self.current_step}

    def reset(self, *, seed=None, options=None):
        print("Environment reset.")
        super().reset(seed=seed, options=options)
        # Reset the environment to an initial state
        self.current_state = self.observation_space.sample() # Example: random initial state
        self.current_step = 0
        observation = self._get_obs()
        info = self._get_info()
        return observation, info

    def step(self, action):
        print(f"Taking action: {action}")
        # Apply the action and update the environment state
        # Calculate reward, determine if episode is terminated/truncated
        self.current_step += 1
        reward = 0.0
        terminated = False
        truncated = False

        # Example: Simple reward and termination logic
        if action == 0:
            reward = 1.0
        if self.current_step >= self.max_episode_steps:
            truncated = True

        self.current_state = self.observation_space.sample() # Example: random next state

        observation = self._get_obs()
        info = self._get_info()
        return observation, reward, terminated, truncated, info

    def render(self):
        print("Rendering environment.")
        # Implement rendering logic (optional)
        if self.render_mode == "rgb_array":
            return np.zeros((84, 84, 3), dtype=np.uint8) # Example: return a black image
        # For "human" mode, display a window or print to console
        pass

    def close(self):
        print("Closing environment.")
        # Clean up resources (optional)
        pass

if __name__ == "__main__":
    wse = WebShoppingEnvironment("https://www.outerknown.com/")
    wse.close()
    print("Done")
    # print(wse._get_obs())
