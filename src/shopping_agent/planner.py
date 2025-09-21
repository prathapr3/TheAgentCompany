import ollama
import re
from .prompts.basic_test import popup_closing_action_generator_prompt

class Planner:
    def __init__(self):
        pass

    def plan(self, current_state):
        print("Planning next action based on current state.")
        response = None # coordinates of where to click

        # Here, you would integrate with the LLM to determine the best action
        with open("./current_state.png", "rb") as image_file:
            image_bytes = image_file.read()

        messages=[
            {
                'role': 'user',
                'content': popup_closing_action_generator_prompt,
                'images': [image_bytes]  # Provide image as a byte array
            }
        ]

        # messages.append({'role': 'user', 'content': basic_add_to_bag_action_generator_prompt.format(
        #     #HTML_snippet=current_state["web_content_representation"]#,
        #     IMAGE_snippet=current_state["visual_representation"]
        # )})

        try:
            response = ollama.chat(model='qwen2.5vl:7b', messages=messages)
            model_response = response['message']['content']
            print(f"Qwen2.5-VL: {model_response}")
            messages.append({'role': 'assistant', 'content': model_response})
        except Exception as e:
            print(f"An error occurred: {e}")

        # Post-process the model response to determine the action
        # Example response looks like this: "The coordinates of the "Add To Bag" button are approximately (500, 200) in the given image."
        # Extract coordinates from the
        if response:
            print("Model response received, processing...")
            # Extract coordinates from the model
            # Here, you would implement the logic to parse the coordinates and map them to an action
            # For simplicity, let's assume we always return action 0
            # Example parsing logic (this is a placeholder and should be replaced with actual parsing code)
            coordinates = self._extract_coordinates(response['message']['content'])            
            return coordinates
        else:
            print("No response from model, defaulting to action 0.")
            # Default action if no valid   

        return (0,0)  # return in case there is no reponse from the model
    
    def _extract_coordinates(self, model_response: str):
        # Implement logic to extract coordinates from the model response
        # This is a placeholder implementation
        match = re.search(r'\((\d+),\s*(\d+)\)', model_response)
        if match:
            print(f"Extracted coordinates: {match}")
            x, y = int(match.group(1)), int(match.group(2))
            return (x, y)
        return None

if __name__ == "__main__":
    planner = Planner()
    dummy_state = {
        "visual_representation": [0.1, 0.2, 0.3],  # Example embedding
        "web_content_representation": "Sample webpage content"
    }
    action = planner.plan(dummy_state)
    print(f"Planned action: {action}")