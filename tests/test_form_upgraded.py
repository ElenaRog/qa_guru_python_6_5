from pathlib import Path
from selene.support.shared import browser
from selene import have, be
from tests import picture


def test_student_registration_form():
    browser.open('/automation-practice-form')

    # WHEN
    browser.element('#firstName').type('Elena')
    browser.element('#lastName').type('Rogozina')
    browser.element('#userEmail').type('elenarog@mail.ru')
    browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
    browser.element('#userNumber').type('5554678578')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('June')
    browser.element('.react-datepicker__year-select').send_keys('1997')
    browser.element('.react-datepicker__day--027:not(.react-datepicker__day--outside-month)').click()

    browser.element('#subjectsInput').type('Biology').press_enter()
    browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Uttar Pradesh')
    ).click()

    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Agra')
    ).click()

    browser.element('#uploadPicture').set_value(
        str(Path(picture.__file__).parent.joinpath('image.png').absolute())
    )

    browser.element('#currentAddress').type('Baker st. 221B')
    browser.element('#submit').should(be.visible).click()
    # THEN

    browser.element('[id=example-modal-sizes-title-lg]').should(
        have.text('Thanks for submitting the form')
    )

    browser.element('.table').all('td').should(
        have.texts(
            ('Student Name', 'Elena Rogozina'),
            ('Student Email', 'elenarog@mail.ru'),
            ('Gender', 'Female'),
            ('Mobile', '5554678578'),
            ('Date of Birth', '27 June,1997'),
            ('Subjects', 'Biology'),
            ('Hobbies', 'Sports'),
            ('Picture', 'image.png'),
            ('Address', 'Baker st. 221B'),
            ('State and City', 'Uttar Pradesh Agra'),
        )
    )
