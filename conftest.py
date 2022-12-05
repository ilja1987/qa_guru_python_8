import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def br_set():
    browser.open("https://demoqa.com/automation-practice-form")
    browser.config.window_width = 800
    browser.config.window_height = 600
