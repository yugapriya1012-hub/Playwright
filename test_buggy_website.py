from playwright.sync_api import Page,expect,Playwright
# Chromium
def Test_buggy(page:Page):
    page.goto("https://buggy.justtestit.org/")
    browser=Playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    # page.goto("https://buggy.justtestit.org/")

def test_Register(page:Page):
    page.goto("https://buggy.justtestit.org/register")

    page.wait_for_load_state("domcontentloaded")

    page.locator("button:has-text('Register')").click()

    page.get_by_label("Login").fill("vdyuga2007@gmail.com")
    page.get_by_label("Full Name").fill("Yuga")
    page.get_by_label("Last Name").fill("priya")
    page.locator("input[type='Password']").fill("yuga97^V")
    page.locator("input[type='Confirm Password']")
    page.get_by_role("button",name="Register").click()

    page.wait_for_selector("text=login")

    expect(page.locator("text=login")).to_be_visible()

def test_login(page:Page):
    page.goto("https://buggy.justtestit.org/register")
    page.get_by_placeholder("Login").fill("vdyuga2007@gmail.com")
    page.locator("input[type='password']").fill("yuga97^V")
    page.get_by_role("button",name="Login").click()


def test_navigation(page:Page):
    page.goto("https://buggy.justtestit.org/")
    page.get_by_role("link",name="Popular Make").click()
    expect(page.locator("text=Lamborghini")).to_be_visible()

    
    page.get_by_role("link",name="Diablo").click()
    expect(page.locator("text=Lamborghini")).to_be_visible()


    cards=page.locator(".container")
    count=cards.count()
    for i in range(count):
        card=cards.nth(i)
        title=card.text_content()
        if "Lamborghini" in title:
            print(title)
            cards.locator("button").click()
            break
        
    
# #Firefox
# # def Test_buggy(page:Page):
# #     # page.goto("https://buggy.justtestit.org/")
# #     browser=Playwright.firefox
# #     page=browser.launch(headless=False)
# #     page.goto("https://buggy.justtestit.org/")

# # def test_Register(page:Page):
# #     page.goto("https://buggy.justtestit.org/register")

# #     page.wait_for_load_state("domcontentloaded")

# #     page.locator("button:has-text('Register')").click()

# #     page.get_by_label("Login").fill("vdyuga2007@gmail.com")
# #     page.get_by_label("Full Name").fill("Yuga")
# #     page.get_by_label("Last Name").fill("priya")
# #     page.locator("input[type='Password']").fill("yuga97^V")
# #     page.locator("input[type='Confirm Password']")
# #     page.get_by_role("button",name="Register").click()

# #     page.wait_for_selector("text=login")

# #     expect(page.locator("text=login")).to_be_visible()

# # def test_login(page:Page):
# #     page.goto("https://buggy.justtestit.org/register")
# #     page.get_by_placeholder("Login").fill("vdyuga2007@gmail.com")
# #     page.locator("input[type='password']").fill("yuga97^V")
# #     page.locator("button",name="Login").click()


