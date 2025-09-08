import gymnasium as gym
import shopping_agent # Import your package to register the env


if __name__ == "__main__":
    env = gym.make("web-shopping-v0")

    observation, info = env.reset()
    for _ in range(10):
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)
        print(f"Obs: {observation}, Reward: {reward}, Terminated: {terminated}, Truncated: {truncated}, Info: {info}")
        if terminated or truncated:
            observation, info = env.reset()
    env.close()
