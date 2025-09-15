import ollama
from .prompts.basic_test import basic_action_generator_prompt, basic_test_prompt

class Planner:
    def __init__(self):
        pass

    def plan(self, current_state) -> int:
        # Placeholder logic for planning
        # In a real scenario, this would involve complex decision-making
        messages = []

        messages.append({'role': 'user', 'content': basic_action_generator_prompt.format(
            HTML_snippet=current_state["web_content_representation"],
            IMAGE_snippet=current_state["visual_representation"],
            selector="<SELECTOR_PLACEHOLDER>"
        )})

        try:
            response = ollama.chat(model='qwen2.5vl:7b', messages=messages)
            model_response = response['message']['content']
            print(f"Qwen2.5-VL: {model_response}")
            messages.append({'role': 'assistant', 'content': model_response})
        except Exception as e:
            print(f"An error occurred: {e}")

        return 0  # Always return action 0 as a placeholder
    
if __name__ == "__main__":
    planner = Planner()
    dummy_state = {
        "visual_representation": [0.1, 0.2, 0.3],  # Example embedding
        "web_content_representation": "Sample webpage content"
    }
    action = planner.plan(dummy_state)
    print(f"Planned action: {action}")