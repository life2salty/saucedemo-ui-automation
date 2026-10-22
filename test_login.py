import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def login(page: Page, username: str = USERNAME, password: str = PASSWORD):
    page.goto(BASE_URL)
    page.locator('[data-test="username"]').fill(username)
    page.locator('[data-test="password"]').fill(password)
    page.locator('[data-test="login-button"]').click()


def test_login_page_is_displayed(page: Page):
    page.goto(BASE_URL)

    expect(page.locator('[data-test="username"]')).to_be_visible()
    expect(page.locator('[data-test="password"]')).to_be_visible()
    expect(page.locator('[data-test="login-button"]')).to_be_visible()


def test_user_can_login(page: Page):
    login(page)

    expect(page).to_have_url(f"{BASE_URL}inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_login_fails_with_invalid_password(page: Page):
    login(page, password="wrong_password")

    expect(page.locator('[data-test="error"]')).to_be_visible()
    expect(page.locator('[data-test="error"]')).to_contain_text(
        "Username and password do not match"
    )
    expect(page).to_have_url(BASE_URL)


def test_locked_out_user_cannot_login(page: Page):
    login(page, username="locked_out_user")

    expect(page.locator('[data-test="error"]')).to_be_visible()
    expect(page.locator('[data-test="error"]')).to_contain_text(
        "Sorry, this user has been locked out."
    )
    expect(page).to_have_url(BASE_URL)


def test_user_can_add_product_to_cart(page: Page):
    login(page)

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    page.locator(".shopping_cart_link").click()

    expect(page).to_have_url(f"{BASE_URL}cart.html")
    expect(page.locator('[data-test="inventory-item-name"]')).to_have_text(
        ["Sauce Labs Backpack"]
    )


def test_user_can_remove_product_from_cart(page: Page):
    login(page)

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator(".shopping_cart_link").click()

    expect(page.locator('[data-test="inventory-item-name"]')).to_have_count(1)

    page.locator('[data-test="remove-sauce-labs-backpack"]').click()

    expect(page.locator('[data-test="inventory-item-name"]')).to_have_count(0)
    expect(page.locator(".shopping_cart_badge")).to_have_count(0)
