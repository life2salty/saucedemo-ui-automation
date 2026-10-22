# UI Test Automation — SauceDemo

An educational UI automation portfolio project for the [SauceDemo](https://www.saucedemo.com/) demo e-commerce application.

## Tech stack

- Python
- Playwright
- pytest
- Chromium
- GitHub Actions

## Automated scenarios

- Verify that the login form is displayed.
- Verify login with valid credentials.
- Verify invalid login attempts using pytest parameterization:
  - Incorrect password
  - Incorrect username
  - Empty username
  - Empty password
- Verify that a locked-out user cannot log in.
- Verify that a product can be added to the cart.
- Verify that two different products can be added and both appear in the cart.
- Verify that a product can be removed from the cart.

The tests use Playwright locators and assertions, pytest's `@pytest.mark.parametrize`, the Playwright-provided `page` fixture, and a custom `logged_in_page` fixture that prepares a fresh authenticated page for each cart test.

## Install locally

Use Python 3.10 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Run tests

```bash
python -m pytest -v
```

## Continuous integration

GitHub Actions runs the UI tests on pushes and pull requests. See the [Actions tab](../../actions).

## Scope

This is a learning portfolio project. The automated tests cover the scenarios listed above and are not commercial QA experience. They do not claim comprehensive checkout, security, performance, or cross-browser coverage.
