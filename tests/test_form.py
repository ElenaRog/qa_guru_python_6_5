import os

from selene import browser, command, be, have


def test_demoqa_form_sending():
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Elena')
    browser.element('#lastName').type('Rogozina')
    browser.element('#userEmail').type('elenarog@mail.ru')
    browser.element("#gender-radio-2").perform(command.js.click)
    browser.element('#userNumber').type('5554678578')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('June')
    browser.element('.react-datepicker__year-select').send_keys('1997')
    browser.element('.react-datepicker__day--027:not(.react-datepicker__day--outside-month)').click()

    browser.element('#subjectsInput').type('biology').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Agra').press_enter()
    browser.element('#uploadPicture').send_keys(os.path.abspath("picture/image.png"))
    browser.element('#currentAddress').type('Baker st. 221B')
    browser.element('#submit').should(be.visible).click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('tbody>tr')[0].should(have.text('Elena Rogozina'))
    browser.all('tbody>tr')[1].should(have.text('elenarog@mail.ru'))
    browser.all('tbody>tr')[2].should(have.text('Female'))
    browser.all('tbody>tr')[3].should(have.text('5554678578'))
    browser.all('tbody>tr')[4].should(have.text('27 June,1997'))
    browser.all('tbody>tr')[5].should(have.text('Biology'))
    browser.all('tbody>tr')[6].should(have.text('Sports'))
    browser.all('tbody>tr')[7].should(have.text('image.png'))
    browser.all('tbody>tr')[8].should(have.text('Baker st. 221B'))
    browser.all('tbody>tr')[9].should(have.text('Uttar Pradesh Agra'))
