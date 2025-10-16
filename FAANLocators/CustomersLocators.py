from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.CSS_SELECTOR, "#root > div > div > div.auth-form-side > form > button")

class AdminLocators:
    DASHBOARD = (By.CSS_SELECTOR, "#root > div > div > div.sidebar > nav > div.nav-item.active > span.desktop-label")
    USERS = (By.XPATH, "/html/body/div/div/div/div[1]/nav/div[2]")
    SERVICES = (By.CSS_SELECTOR, "#root > div > div > div.sidebar > nav > div:nth-child(3) > span.desktop-label")
    CUSTOMERS = (By.XPATH, "/html/body/div/div/div/div[1]/nav/div[4]")
    BILLS = (By.CSS_SELECTOR, "#root > div > div > div.sidebar > nav > div.nav-item.active")
    REPORTS = (By.CSS_SELECTOR, "/html/body/div/div/div/div[1]/nav/div[6]")
    AUDIT_TRAIL = (By.XPATH, "/html/body/div/div/div/div[1]/nav/div[7]/span[1]")
    INVOICES = (By.CSS_SELECTOR, "#root > div > div > div.sidebar > nav > div.nav-item.active > span.desktop-label")
    PAYMENT = (By.XPATH, "/html/body/div/div/div/div[1]/nav/div[9]/span[1]")
    FEEDBACK_DISPUTES = (By.CSS_SELECTOR, "#root > div > div > div.sidebar > nav > div.nav-item.active > span.desktop-label")
    PROFILE = (By.XPATH, "/html/body/div/div/div/div[1]/nav/div[11]")

class LogoutLocators:
    LOGOUT = (By.CSS_SELECTOR, "#root > div > div > div.sidebar > div.sidebar-footer > div")
    LOGOUT_BUTTON = (By.XPATH, "/html/body/div/div/div/div[2]/div[3]/div/div/div[3]/button/div/span")

