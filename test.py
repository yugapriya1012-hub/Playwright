# #9
# # 1.pytest -s -v
# # 2.pytest filename.py
# # 3.pytest -v

# #2
# import pytest
# @pytest.fixture(scope="function")
# def testing_scenario():
#     a={{"id":"TC01",
#        "scenario":"Login",
#        "result":"Pass"},
#        {"id":"TC02",
#         "scenario":"Login",
#         "result":"Fail"
#         }
#     }
#     print(a.tuple())
    
# #per file
# @pytest.fixture(scope="module")
# def run_per_file(testing_scenario):
#      a={{"id":"TC01",
#        "scenario":"Login",
#        "result":"Pass"},
#        {"id":"TC02",
#         "scenario":"Login",
#         "result":"Fail"
#         }
#     }
#     print(a.tuple)


# @pytest.fixture(scope="session")
# def run_per_file(testing_scenario):
#      a={{"id":"TC01",
#        "scenario":"Login",
#        "result":"Pass"},
#        {"id":"TC02",
#         "scenario":"Login",
#         "result":"Fail"
#         }
#     }
#     print(a.tuple)




#10
# from playwright.sync_api import Page,expect,Playwright
# def test_browser_for_testing(page:Page):
#     browser=Playwright.chromium.launch(headless=False)
#     context=browser.new_context()
#     page=context.new_page()
#     page.goto("url")

# def test_browser(page:Page):
#     page.goto("url")
     

# first i put browser name in this line(browser=Playwright.browser name.launch(headless=False))
# and i will test  main features eg.login,signup and i use assertion and .fill(),.close(),.click(),etc.
# in form field and i want to redirect i use wait_for_url() and wait_for_load_state() it use to 'domcontentloaded'
# and i use to redirect page.goto() and first i import Page,expect in playwright . synchronous api 

#7
# def reverse_character(text):
#     rev=""
#     COUNT=0
#     for i in range(0,len(text)):
#         rev=i+rev
#         COUNT=COUNT+1
#     assert COUNT==17
 

#8

user = {
  "username": "test_user",
  "password": "Pass123",
  "email": "test@example.com"
}

# if user["password"]<6 and user["email"] not in "@":
    
# from playwright.sync_api import Page,expect,Playwright
# def test_browser_for_testing(page:Page):
#     browser=Playwright.chromium.launch(headless=False)
#     context=browser.new_context()
#     page=context.new_page()
#     page.goto("http://127.0.0.1:5501/page/signin.html")

# def test_browser(page:Page):
#     page.goto("http://127.0.0.1:5501/page/signin.html")
#     page.get_by_label("Email Address").fill("testexample.com")
#     page.get_by_label("Password").fill("12345")
#     page.get_by_role("button",name="Sign In").click()


