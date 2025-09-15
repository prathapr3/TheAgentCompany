import gymnasium as gym
import shopping_agent # Import your package to register the environment
from shopping_agent.actor import WebActionWrapper

if __name__ == "__main__":
    env = WebActionWrapper(gym.make("web-shopping-v0"))

    observation, info = env.reset(options={"home_url": "https://www.outerknown.com/products/the-team-hoodie-charcoal?variant=51506517573816"})
    for _ in range(10):
        action = env.action_space.sample() # hack -- action will be from the wrapper
        observation, reward, terminated, truncated, info = env.step(action)
        # print(f"Obs: {observation}, Reward: {reward}, Terminated: {terminated}, Truncated: {truncated}, Info: {info}")
        if terminated or truncated:
            observation, info = env.reset()
    env.close()
