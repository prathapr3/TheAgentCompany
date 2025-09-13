###
# File to help import locally. No need to write any code here.
###

from gymnasium.envs.registration import register

register(
    id="web-shopping-v0",
    entry_point="shopping_agent.web_shopping_environment:WebShoppingEnvironment", # Path to your environment class
    # max_episode_steps=200, # Optional: default max steps
)

# print("Registered the environment.")
