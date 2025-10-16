import time

from selenium.webdriver.support import expected_conditions as EC
from _pytest.config import Config
from selenium.webdriver.support.wait import WebDriverWait
from FAANLocators.CustomersLocators import LoginLocators, AdminLocators, LogoutLocators


class Action_Page:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        enter_email = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.EMAIL))
        enter_email.send_keys(email)
        time.sleep(10)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.PASSWORD))
        enter_password.send_keys(password)
        time.sleep(10)

    def click_login(self):
        click_login = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.LOGIN))
        click_login.click()
        time.sleep(10)

class Admin_Page:
    def __init__(self, driver):
        self.driver = driver

    def click_dash_board(self):
        click_Dashboard = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminLocators.DASHBOARD))
        click_Dashboard.click()
        time.sleep(Config.WAIT_TIME)

    def click_users(self):
        click_users = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminLocators.USERS))
        click_users.click()
        time.sleep(Config.WAIT_TIME)

    def click_services(self):
        click_services = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminLocators.SERVICES))
        click_services.click()
        time.sleep(Config.WAIT_TIME)

    def click_customers(self):
        click_customers = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminLocators.CUSTOMERS))
        click_customers.click()
        time.sleep(Config.WAIT_TIME)

    def click_bills(self):
        click_bills = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminLocators.BILLS))
        click_bills.click()
        time.sleep(Config.WAIT_TIME)

    def click_report(self):
        click_report = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminLocators.REPORTS))
        click_report.click()
        time.sleep(Config.WAIT_TIME)

    def click_audit_trail(self):
        click_audit_trail = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminLocators.AUDIT_TRAIL))
        click_audit_trail.click()
        time.sleep(Config.WAIT_TIME)

    def click_invoices(self):
        click_invoices = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminLocators.INVOICES))
        click_invoices.click()
        time.sleep(Config.WAIT_TIME)

    def click_payment(self):
        click_payment = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminLocators.PAYMENT))
        click_payment.click()
        time.sleep(Config.WAIT_TIME)

    def click_feedback_disputes(self):
        click_feedback_disputes = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminLocators.FEEDBACK_DISPUTES))
        click_feedback_disputes.click()
        time.sleep(Config.WAIT_TIME)

    def click_profile(self):
        click_profile = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminLocators.PROFILE))
        click_profile.click()
        time.sleep(Config.WAIT_TIME)

class Logout_Page:
    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        click_logout = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LogoutLocators.LOGOUT))
        click_logout.click()
        time.sleep(Config.WAIT_TIME)

    def click_logout_button(self):
        click_logout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LogoutLocators.LOGOUT_BUTTON))
        click_logout_button.click()
        time.sleep(Config.WAIT_TIME)