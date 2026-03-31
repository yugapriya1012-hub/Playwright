from playwright.sync_api import Page,expect
# def test_playwrightBasics(playwright):
#     browser=playwright.chromium.launch(headless=False)
#     context=browser.new_context()
#     page=context.new_page()
#     page.goto("http://127.0.0.1:5501/page/signin.html")

# def test_playwrightShortCut(page:Page):
#     page.goto("http://127.0.0.1:5501/page/signin.html")

# def test_coreLocators(page:Page):
#     page.goto("http://127.0.0.1:5501/page/signin.html")
#     page.get_by_label("Email Address").fill("1234@gmail.com")
#     page.get_by_label("Password").fill("12345")
#     page.get_by_role("button",name="Sign In").click()
#     expect(page.get_by_text("Incorrect email or password")).to_be_visible()

# def test_firefoxBrowser(playwright):

#     firefoxBrowser= playwright.firefox
#     browser=firefoxBrowser.launch(headless=False)
#     page=browser.new_page()
#     page.goto("http://127.0.0.1:5501/page/signin.html")
#     page.get_by_label("Email Address").fill("1234@gmail.com")
#     page.get_by_label("Password").fill("12345")
#     page.get_by_role("button",name="Sign In").click()
#     expect(page.get_by_text("Incorrect email or password")).to_be_visible()

    