from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def open_facebook():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.messenger.com/?locale=pl_PL")
