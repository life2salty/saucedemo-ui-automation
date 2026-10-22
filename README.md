# UI Test Automation — SauceDemo

An educational UI automation portfolio project for the [SauceDemo](https://www.saucedemo.com/) demo e-commerce application.

## Tech stack

- Python
- Playwright
- pytest
- Chromium
- GitHub Actions

## Automated scenarios

1. Verify that the login form is displayed.
2. Verify login with valid credentials.
3. Verify that login is rejected when the password is incorrect.
4. Verify that a locked-out user cannot log in.
5. Verify that a product can be added to the cart.
6. Verify that two different products can be added and both appear in the cart.
7. Verify that a product can be removed from the cart.

The tests use Playwright locators, assertions, a reusable login helper, and pytest-playwright's `page` fixture.

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

This is a learning portfolio project. It covers the seven UI scenarios listed above and is not commercial QA experience. It does not claim comprehensive checkout, security, performance, or cross-browser coverage.
