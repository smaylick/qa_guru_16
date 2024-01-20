"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, have


@pytest.mark.desktop
def test_github_desktop(desktop_browser):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in')).click()
    browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.mobile
def test_github_mobile(mobile_browser):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in')).click()
    browser.element('#login').should(have.text('Sign in to GitHub'))
