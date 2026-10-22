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


@pytest.mark.parametrize(
    ("username", "password", "expected_error"),
    [
        pytest.param(
            USERNAME,
            "wrong_password",
            "Username and password do not match",
            id="wrong-password",
        ),
        pytest.param(
            "wrong_user",
            PASSWORD,
            "Username and password do not match",
            id="wrong-username",
        ),
        pytest.param(
            "",
            PASSWORD,
            "Username is required",
            id="empty-username",
        ),
        pytest.param(
            USERNAME,
            "",
            "Password is required",
            id="empty-password",
        ),
    ],
)
def test_login_rejected_for_invalid_credentials(
    page: Page, username: str, password: str, expected_error: str
):
    login(page, username=username, password=password)

    error = page.locator('[data-test="error"]')
    expect(error).to_be_visible()
    expect(error).to_contain_text(expected_error)
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


def test_user_can_add_two_products_to_cart(page: Page):
    login(page)

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()

    expect(page.locator(".shopping_cart_badge")).to_have_text("2")

    page.locator(".shopping_cart_link").click()

    expect(page.locator('[data-test="inventory-item-name"]')).to_have_count(2)
    expect(page.locator('[data-test="inventory-item-name"]')).to_have_text(
        ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    )


def test_user_can_remove_product_from_cart(page: Page):
    login(page)

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator(".shopping_cart_link").click()

    expect(page.locator('[data-test="inventory-item-name"]')).to_have_count(1)

    page.locator('[data-test="remove-sauce-labs-backpack"]').click()

    expect(page.locator('[data-test="inventory-item-name"]')).to_have_count(0)
    expect(page.locator(".shopping_cart_badge")).to_have_count(0)
