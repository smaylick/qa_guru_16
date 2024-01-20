"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have


@pytest.mark.parametrize("desktop_browser", [(1920, 1080), (1600, 900)], indirect=True)
def test_github_desktop(desktop_browser):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in')).click()
    browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize("mobile_browser", [(800, 400), (480, 360)], indirect=True)
def test_github_mobile(mobile_browser):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in')).click()
    browser.element('#login').should(have.text('Sign in to GitHub'))
