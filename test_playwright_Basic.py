import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser():
    print("Launching Chromium browser")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        print("Closing Chromium browser")
        browser.close()