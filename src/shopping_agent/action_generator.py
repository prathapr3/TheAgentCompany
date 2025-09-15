import gymnasium as gym
import random

class WebActionWrapper(gym.ActionWrapper):
    def __init__(self, env: gym.Env, epsilon: float = 0.1):
        super(WebActionWrapper, self).__init__(env)
        self.env = env
        self.epsilon = epsilon

    def action(self, action: gym.core.WrapperActType) -> gym.core.WrapperActType:
        print(f"Original action: {action}")

        # Get the env observation first and the decide what action to take
        # current_state = env.observation_space.sample()  # Placeholder for actual observation

        print(f"Action before epsilon-greedy: {action}")
        if random.random() < self.epsilon:
            current_state = self.env.unwrapped._get_obs()
            print(f"Current state: {current_state}")
            action = self.env.action_space.sample()
            print(f"Random action {action}")
            return action

        print(f"Action after epsilon-greedy: {action}")
        return action

    def _identify_best_action(self, current_state) -> int:
        # Placeholder logic for identifying the best action based on the state
        # In a real scenario, this could involve a trained model or heuristic
        if random.random() < self.epsilon:
            action = self.env.action_space.sample()
            print(f"Random action {action}")
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
