import os.path
from selene.support.shared import browser
from selene import have


def test_form(browser_setup):
    browser.open("/automation-practice-form")
    browser.element('[id="firstName"]').type('Ilja')
    browser.element('[id="lastName"]').type('Domnin')
    browser.element('[id="userEmail"]').type('domniniv@mail.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[for="gender-radio-2"]').click()
    browser.element('[for="gender-radio-3"]').click()
    browser.element('[id="userNumber"]').type('89051010101')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="1"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value = "1987"]').click()
    browser.element('.react-datepicker__day--005').click()
    browser.element('[autocapitalize="none"]').type("math").press_tab()
    browser.element('[autocapitalize="none"]').type("ch").press_tab()
    browser.element('[for ="hobbies-checkbox-1"]').click()
    browser.element('[for ="hobbies-checkbox-2"]').click()
    browser.element('[for ="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'foto/foto.bmp')
        )
    )
    browser.element('[id="currentAddress"]').type(
        'Sad area, Dreary area, Sadness, Disappointment Avenue, house 13')
    browser.element('[id="state"]').click()
    browser.element('[id="react-select-3-option-2"]').click()
    browser.element('[id="city"]').click()
    browser.element('[id="react-select-4-option-0"]').click()
    browser.element('[id="submit"]').press_enter()
    browser.all("tbody tr").should(have.size(10))
    browser.all('tbody tr td:last-child').should(have.texts(
        'Ilja Domnin',
        'domniniv@mail.ru',
        'Other',
        '8905101010',
        '05 February,1987',
        'Maths, Chemistry',
        'Sports, Reading, Music',
        'foto.bmp',
        'Sad area, Dreary area, Sadness, Disappointment Avenue, house 13',
        'Haryana Karnal'))
