import gymnasium as gym
from .planner import Planner

class WebActionWrapper(gym.ActionWrapper):
    def __init__(self, env: gym.Env, epsilon: float = 0.1):
        super(WebActionWrapper, self).__init__(env)
        self.env = env
        self.epsilon = epsilon
        self.planner = Planner()

    def action(self, action: gym.core.WrapperActType) -> gym.core.WrapperActType:
        action = self._identify_best_action()
        self._act(action)

        return action

    def _act(self, action: tuple):
        print(f"Executing action: {action}")
        self.browser_handler = self.env.unwrapped.browser_handler

        # Click on the coordinates returned by the planner
        self.env.unwrapped.browser_handler.click_at_position(action[0], action[1])

        # # Map the action integer to specific environment actions
        # if action == 0:
        #     self.env.unwrapped.browser_handler.click_element("a[href*='add-to-cart']")
        # elif action == 1:
        #     self.env.unwrapped.browser_handler.click_element("a[href*='cart']")
        # elif action == 2:
        #     self.env.unwrapped.browser_handler.click_element("a[href*='checkout']")
        # elif action == 3:
        #     self.env.unwrapped.browser_handler.click_element("a[href*='home']")
        # else:
        #     raise ValueError(f"Unknown action: {action}")

    def _identify_best_action(self) -> int:
        print("Identifying best action using planner.")
        # Get the current state from the environment
        self.current_state = self.env.unwrapped._get_obs()
        
        # Use planner to determine the best action
        best_action = self.planner.plan(self.current_state)

        return best_action

if __name__ == "__main__":
    env = WebActionWrapper(gym.make("CartPole-v1"))

    obs = env.reset()
    total_reward = 0.0

    while True:
        obs, reward, done, _, _ = env.step(0)
        total_reward = total_reward + float(reward)
        if done:
            break

    print(f"Reward got: {total_reward:.2f}")
