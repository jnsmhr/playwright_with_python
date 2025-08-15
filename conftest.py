# conftest.py
import pytest
from playwright.sync_api import Playwright, Browser, Page

@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture
def page(browser: Browser):
    page = browser.new_page()
    yield page
    page.close()