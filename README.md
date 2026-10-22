# UI Test Automation — SauceDemo

## About the Project

An educational UI test automation project for the [SauceDemo](https://www.saucedemo.com/) demo e-commerce application.

The project uses Python, Playwright, and pytest to verify basic login and shopping cart functionality.

## Tech Stack

- Python
- Playwright
- pytest
- Chromium

## Automated Test Scenarios

1. Verify that the login page displays the username, password, and login button.
2. Verify that a user can log in with valid credentials.
3. Verify that a user can add a product to the shopping cart and see it in the cart.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Run Tests

```bash
python -m pytest -v test_login.py
```

## Project Status

Three automated UI test scenarios have been implemented and executed locally.

This is a learning and portfolio project, not commercial QA experience.