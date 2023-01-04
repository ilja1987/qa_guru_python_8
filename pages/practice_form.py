import os.path
from selene.support.shared import browser
import tests.action as action
from selene import have

def fill_form(user):
    action.open_page()
    action.fill_user_fields(user.name,
                            user.last_name,
                            user.email,
                            user.phone,
                            user.adress)

    action.select_date_of_birthday(user.birthday[0],user.birthday[1],user.birthday[2])

    action.select_subjects(user.subjects)

    action.select_gender(user.gender)

    action.select_hobbies(user.hobbies)

    action.upload_picture(user.photo)

    action.select_state(user.state)
    action.select_sity(user.sity)

    action.push_submit_button()
def assert_form(user):
    action.asser_user_registration(user.name + ' ' + user.last_name,
                                   user.email,
                                   user.gender,
                                   user.phone,
                                   '05 February,1987',
                                   user.subjects,
                                   user.hobbies,
                                   user.photo,
                                   user.adress,
                                   user.state + ' ' + user.sity)
