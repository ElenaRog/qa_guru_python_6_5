import pytest
from selene.support.shared import browser


@pytest.fixture(autouse=True)
def browser_settings():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    browser.quit()
