import pytest
from selene.support.shared import browser

@pytest.fixture(scope="session")
def br_set():
    browser.config.window_width = 1920
    browser.config.window_height = 1020
    browser.open("https://demoqa.com/automation-practice-form")
    browser.config.hold_browser_open = True

