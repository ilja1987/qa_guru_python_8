from classes.user import User
from pages.practice_form import practice_form


def test_final(browser_setup):
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

    practice_form.fill(ilja)

    practice_form.assert_f(ilja)


practice_form = practice_form()