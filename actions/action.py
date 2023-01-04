import os.path
from selene.support.shared import browser
from selene import have

def open_page():
    browser.open('/automation-practice-form')

def fill_user_fields(name,last_name,email,phone,adress):
    browser.element('[id="firstName"]').type(name)
    browser.element('[id="lastName"]').type(last_name)
    browser.element('[id="userEmail"]').type(email)
    browser.element('[id="userNumber"]').type(phone)
    browser.element('#currentAddress').type(adress)

def select_option(selector, text):
    browser.element(selector).click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text(text)
    ).click()

def select_state(text):
    select_option('#state',text)

def select_sity(text):
    select_option('#city', text)

def select_subjects(text):
    browser.element('[autocapitalize="none"]').type(text).press_tab()

def upload_picture(path_to_photo):
    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), '../resources/'+ path_to_photo)
        )
    )

def select_date_of_birthday(day,month,year):
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element(f'[value="{month-1}"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element(f'[value = "{year}"]').click()
    browser.element(f'.react-datepicker__day--00{day}').click()

def push_submit_button():
    browser.element('[id="submit"]').press_enter()

def asser_user_registration(name,email,male,phone,birthday,subjects,hobbies,photo,adress,options):
    browser.all("tbody tr").should(have.size(10))
    browser.all('tbody tr td:last-child').should(have.texts(
        name,email,male,phone,birthday,subjects,hobbies,photo,adress,options))

def select_gender(gender):
    browser.element(f'[name=gender][value={gender}]+label').click()

def select_hobbies(hobies):
    checkboxes_click(browser.all('[for^=hobbies-checkbox]'), hobies)

def checkboxes_click(elements, *by_texts):
    for value in by_texts:
        elements.element_by(have.text(value)).click()