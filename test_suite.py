import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Actions.ActionsPage import Action_Page, Admin_Page, Logout_Page
from Config.Configuration import Config

# Fixture to launch browser
@pytest.fixture(scope="session")
def driver_setup():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()

# Fixture to perform login
@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login_page = Action_Page(driver)
    login_page.login_url("https://faan-bare.vercel.app/login")
    return login_page

# Test: Successful login
def test_login_with_valid_credentials(login):
    login.enter_email(Config.EMAIL)
    login.enter_password(Config.PASSWORD)
    login.click_login()

# Test Admin Page
def test_admin_page(login):
    admin_page = Admin_Page(login.driver)
    admin_page.click_dash_board()

    admin_page.click_users()
    admin_page.click_services()
    admin_page.click_customers()
    admin_page.click_bills()
    admin_page.click_report()
    admin_page.click_audit_trail()
    admin_page.click_invoices()
    admin_page.click_payment()
    admin_page.click_feedback_disputes()
    admin_page.click_profile()

# Test Logout Page
def test_logout_page(login):
    logout_page = Logout_Page(login.driver)
    logout_page.click_logout()
    logout_page.click_logout_button()