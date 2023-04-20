from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from utils.pages.calorie_calc import CarbCalcPage
from allure_commons._allure import attach
from allure_commons.types import AttachmentType

def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    context.driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

    context.calculator = CarbCalcPage()

def after_all(context):
    context.driver.quit()

def after_step(context, step):
    if step.status == 'failed':
        attach(context.driver.get_screenshot_as_png(),name="Screenshot",attachment_type=AttachmentType.PNG)