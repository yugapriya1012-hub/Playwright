# # from playwright.sync_api import Page

# # def test_UIValidationDynamicScript(page:Page):
# #     page.goto("http://127.0.0.1:5501/page/signin.html")
# #     page.get_by_label("Email Address").fill("1234@gmail.com")
# #     page.get_by_label("Password").fill("12345")
# #     page.get_by_role("button",name="Sign In").click()

# from playwright.sync_api import Page, expect

# def test_UIValidationDynamicScript(page: Page):

#     # Login page open
#     page.goto("https://rahulshettyacademy.com/loginpagePractise/")

#     # Fill login details
#     page.get_by_label("Username:").fill("rahulshettyacademy")
#     page.get_by_label("Password:").fill("learning")

#     # Select dropdown
#     page.get_by_role("combobox").select_option("teach")

#     # Accept terms
#     page.locator("#terms").check()

#     # Click Sign In
#     page.get_by_role("button", name="Sign In").click()

#     # Wait for cards to load (Auto-wait)
#     cards = page.locator(".card")

#     # Filter card with iphone X
#     iphone_card = cards.filter(has_text="iphone X")

#     # Click Add button inside that card
#     iphone_card.get_by_role("button", name="Add").click()

#     # Assertion (verify product added or visible)
#     expect(iphone_card).to_contain_text("iphone X")