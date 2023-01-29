from classes.user import User
from pages.practice_form import practice_form
import allure
from selene.support.shared import browser
from utils import attach
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@allure.title('Тест на заполнение формы')
def test_final(browser_setup):
    options = Options()
    selenoid_capabilities = {
        "browserName": "UNKNOWN",
        "browserVersion": "",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="http://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver=driver

    ilja = User(
        name='Andrew',
        last_name='Domnin',
        email='domniniv@mail.ru',
        gender='Male',
        phone='8905101010',
        adress='Sad area, Dreary area, Sadness, Disappointment Avenue, house 13',
        birthday=[5, 2, 1987],
        subjects='Maths',
        hobbies='Reading',
        photo='foto.bmp',
        state='NCR',
        sity='Delhi'
    )
    with allure.step('Заполняем форму'):
        practice_form.fill(ilja)
    with allure.step('Проверяем корректность заполнения'):
        practice_form.assert_f(ilja)

    attach.add_screenshot(browser)
    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

practice_form = practice_form()
