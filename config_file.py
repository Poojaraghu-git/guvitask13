import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def get_driver4():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    print("driver created")
    yield driver
    print("driver closed")
    driver.quit()