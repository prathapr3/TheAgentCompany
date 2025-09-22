import re
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
from .web_state_representor import WebStateRepresentor
class PlaywrightHandler:
    def __init__(self):
        self.playwright_handle = sync_playwright().start()
        self.browser = self.playwright_handle.chromium.launch()
        self.page = self.browser.new_page()
        self.page.set_viewport_size({"width": 1920, "height": 3020}) # Set viewport size to 1920x3020
        self.web_state_representator = WebStateRepresentor()
        self.current_state = None

    def navigate_to(self, url: str):
        self.page.goto(url)
        #self.page.wait_for_load_state("networkidle")  # wait until network is idle
        self.page.wait_for_timeout(2000)

    def click_element(self, selector: str):
        self.page.click(selector)

    def click_at_position(self, x: int, y: int):
        print(f"Clicking at position: ({x}, {y})")
        self.page.mouse.click(x, y)
        self.page.wait_for_timeout(2000)  # wait for 2 seconds to allow page to load
        self.page.screenshot(path = 'clicked_state.png', type = 'png', full_page=True)

    def get_text(self, selector: str) -> str:
        return self.page.inner_text(selector)

    def fill_input(self, selector: str, text: str):
        self.page.fill(selector, text)

    def is_checkout_complete(self) -> bool:
        # Example logic to determine if checkout is complete
        try:
            confirmation_text = self.page.inner_text("body")
            if re.search(r"Thank you for your order", confirmation_text, re.IGNORECASE):
                return True
        except:
            return False
        return False

    # Takes a screenshot and returns a representation of the image bytes and website content
    def capture_current_state(self):
        current_screenshot = self.page.screenshot(path = 'current_state.png', type = 'png', full_page=True)
        current_webpage_content = self.page.content()
        self.current_state = self.web_state_representator.represent_state(current_screenshot, current_webpage_content)
        return self.current_state

    def close(self):
        self.browser.close()
        self.playwright_handle.stop()

if __name__ == "__main__":
    pwh = PlaywrightHandler()
    pwh.navigate_to("https://www.outerknown.com/")
    state = pwh.capture_current_state()
    print("Screenshot Embedding:", state["visual_representation"])
    print("Webpage Content:", state["web_content_representation"])
    print(pwh.get_text("h1"))
    pwh.close()

# def interact_with_website():
#     with sync_playwright() as p:
#         # Launch a Chromium browser instance (you can also use firefox or webkit)
#         # headless=False opens a visible browser window
#         browser = p.chromium.launch(headless=False) 
        
#         # Create a new page (tab) in the browser
#         page = browser.new_page()

#         # Navigate to a specific URL
#         page.goto("https://www.example.com")

#         # Interact with elements on the page:

#         # 1. Type text into an input field:
#         # page.fill("#username-input", "my_username") 

#         # 2. Click a button:
#         # page.click("#submit-button")

#         # 3. Get text content from an element:
#         # element_text = page.locator(".my-class").inner_text()
#         # print(f"Text from element: {element_text}")

#         # 4. Take a screenshot:
#         # page.screenshot(path="example_screenshot.png")

#         # 5. Wait for a specific element to appear:
#         # page.wait_for_selector("#dynamic-content")

#         # Perform other actions as needed...

#         # Close the browser
#         browser.close()