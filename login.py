from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)



        page = browser.new_page()

        # Open login page
        page.goto("http://127.0.0.1:5501/page/signin.html")

        # Enter username
        page.fill("input[name='username']", "myusername")

        # Enter password
        page.fill("input[name='password']", "mypassword")

        # Click login button
        page.click("button[type='submit']")

        
        page.wait_for_selector("text=Dashboard")

        print("Login Successful ")

        browser.close()
        