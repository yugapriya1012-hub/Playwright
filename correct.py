# from playwright.sync_api import Page, expect

# def test_login(page: Page):
#     page.goto("http://127.0.0.1:5501/page/signin.html")

#     page.wait_for_load_state("domcontentloaded")

#     page.locator("input[type='email']").fill("vdyuga2007@gmail.com")
#     page.locator("input[type='password']").fill("yuga123")

#     page.locator("button:has-text('Sign In')").click()

#     page.wait_for_selector("text=Welcome")

#     expect(page.locator("text=Welcome")).to_be_visible()

