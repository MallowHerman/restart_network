from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()


def login(browser):
    try:
        login_url = os.environ.get('BASE_URL')
        browser.get(login_url)

        input_username = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'txt_Username'))
        )

        input_password = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'txt_Password'))
        )

        button_login = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'button'))
        )
        
        input_username.send_keys(os.environ.get('LOGIN'))
        input_password.send_keys(os.environ.get('PASSWORD'))

        sleep(5)

        button_login.click()

        WebDriverWait(browser, 10)

    except Exception as e:
        print(f'Something went wrong: {e}')

    finally:
        browser.quit()

def restart(browser):
    try:
        restart_url = f"{os.environ.get('BASE_URL')}/html/ssmp/reset/reset.asp"
        browser.get(restart_url)

        button_restart = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'btnReboot'))
        )

        button_restart.click()

        sleep(2)

        alert = WebDriverWait(browser, 10).until(
            EC.alert_is_present()
        )

        sleep(2)

        alert.accept()

        sleep(5)

        WebDriverWait(browser, 5)

    except Exception as e:
        print(f'Something went wrong: {e}')

    finally:
        browser.quit()



# Configurar o serviço do ChromeDriver
service = ChromeService(ChromeDriverManager().install())

# Inicializar o navegador Chrome
browser = webdriver.Chrome(service=service)

if __name__ == '__main__':
    login(browser)
    restart(browser)

