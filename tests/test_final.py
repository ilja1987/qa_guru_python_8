from classes.user import User
from pages.practice_form import practice_form
import allure


@allure.title('Fill form test')
def test_final():
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
    with allure.step('Fill'):
        practice_form.fill(ilja)
    with allure.step('Test correct fill'):
        practice_form.assert_f(ilja)


practice_form = practice_form()
