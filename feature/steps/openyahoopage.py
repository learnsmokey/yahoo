from behave import given


@given("Open New Yahoo Page")
def open_p1(context):
    # context.app.main_page.MainPage.driver = context.driver
    # context.app.main_page.MainPage.open_webpage(context.driver, "https://yahoo.com")
    # context.app.main_page.open_webpage("https://yahoo.com")
    context.app.main_page.open_direct_webpage(context, "https://yahoo.com")
