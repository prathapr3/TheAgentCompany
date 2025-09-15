import gymnasium as gym
import random

class WebActionWrapper(gym.ActionWrapper):
    def __init__(self, env: gym.Env, epsilon: float = 0.1):
        super(WebActionWrapper, self).__init__(env)
        self.env = env
        self.epsilon = epsilon

    def action(self, action: gym.core.WrapperActType) -> gym.core.WrapperActType:
        action = self._identify_best_action()
        return action

    def _identify_best_action(self) -> int:
        self.current_state = self.env.unwrapped._get_obs()
        # This is where you would implement the logic to identify the best action
        # For demonstration, we'll use a random action with probability epsilon
        if random.random() < self.epsilon:
            action = self.env.action_space.sample()
            print(f"_identify_best_action::random action {action}")
            return action
        return 0  # Always return action '0' as the best action for demonstration

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
