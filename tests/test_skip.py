"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have


@pytest.mark.desktop
def test_github_desktop(is_desktop_browser):
    if not is_desktop_browser:
        pytest.skip(reason='Тест для экрана компьютера')
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.mobile
def test_github_mobile(is_desktop_browser):
    if is_desktop_browser:
        pytest.skip(reason='Тест для экрана телефона')
    browser.open('https://github.com')
    browser.element('.js-details-target.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('#login').should(have.text('Sign in to GitHub'))
