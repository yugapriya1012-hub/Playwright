from playwright.sync_api import Page

def test_login(page: Page):
    page.goto("http://127.0.0.1:5501/page/signin.html")

    page.wait_for_load_state("domcontentloaded")

    # Fill login form
    page.locator("input[type='email']").fill("vdyuga2007@gmail.com")
    page.locator("input[type='password']").fill("yuga123")

    # Click login
    page.get_by_role("button", name="Sign In").click()

    # Wait for home page
    page.wait_for_url("**/home.html")

    # Validation
    assert "home" in page.url