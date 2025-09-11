import re
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright

class PlaywrightHandler:
    def __init__(self):
        self.playwright_handle = sync_playwright().start()
        self.browser = self.playwright_handle.chromium.launch()
        self.page = self.browser.new_page()

    def navigate_to(self, url: str):
        self.page.goto(url)

    def click_element(self, selector: str):
        self.page.click(selector)

    def get_text(self, selector: str) -> str:
        return self.page.inner_text(selector)

    def fill_input(self, selector: str, text: str):
        self.page.fill(selector, text)
    
    def take_screenshot(self):
        print("Taking screenshot")
        self.current_state = self.page.screenshot(path = 'current_state.png', type = 'png', full_page=True)

    def close(self):
        self.browser.close()
        self.playwright_handle.stop()

if __name__ == "__main__":
    pwh = PlaywrightHandler()
    pwh.navigate_to("https://www.outerknown.com/")
    pwh.take_screenshot()
    print(pwh.get_text("h2"))
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