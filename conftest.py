import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def br_set():
    browser.config.window_width = 1024
    browser.config.window_height = 768
    browser.open("https://demoqa.com/automation-practice-form")

