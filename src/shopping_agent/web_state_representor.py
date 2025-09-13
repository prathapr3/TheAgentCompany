import ollama
import base64
from PIL import Image
from sentence_transformers import SentenceTransformer

VISUAL_EMBEDDING_MODEL_NAME = "clip-ViT-B-32"
VLM_MODEL_NAME = "qwen2.5vl:7b"
EMBEDDING_MODEL_NAME = "llava-llama3:latest"

class WebStateRepresentor:
    def __init__(self):
        self.web_content = None
        self.screenshot_embedding = None
        self.vlm_name = VLM_MODEL_NAME
        self.embedding_model_name = EMBEDDING_MODEL_NAME
        self.visual_embedding_model_name = VISUAL_EMBEDDING_MODEL_NAME

    def represent_state(self, screenshot: bytes, webpage_content: str):
        # Convert screenshot bytes to a base64 string if needed
        screenshot_base64 = base64.b64encode(screenshot).decode('utf-8')

        model = SentenceTransformer(self.visual_embedding_model_name)
        self.screenshot_embedding = model.encode(screenshot_base64)

        # # Get image description from VLM
        # response_vlm = ollama.chat(
        #     model = self.vlm_name,
        #     messages = [
        #         {
        #             'role': 'user',
        #             'content': 'Describe this image in detail.',
        #             'images': [screenshot_base64]
        #         }
        #     ]
        # )

        # image_description = response_vlm['message']['content']
        # print(f"Image Description: {image_description}")

        # # Generate embedding for the description using an embedding model
        # self.screenshot_embedding = ollama.embeddings(
        #     model = self.embedding_model_name,
        #     prompt = image_description
        # )

        # Keeping the webpage content as is for now
        self.web_content = webpage_content

        return {"visual_representation": self.screenshot_embedding, "web_content_representation": self.web_content}

if __name__ == "__main__":
    with open("current_state.png", "rb") as img_file:
        screenshot_bytes = img_file.read()
    webpage_content = "<html><body><h1>Sample Page</h1></body></html>"
    representor = WebStateRepresentor()
    state = representor.represent_state(screenshot_bytes, webpage_content)
    print("Screenshot Embedding:", state["visual_representation"])
    print("Webpage Content:", state["web_content_representation"])
    print("WebStateRepresentor test completed.")
