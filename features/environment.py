from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from utils.pages.calorie_calc import CarbCalcPage

def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    context.driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.calculator = CarbCalcPage()
