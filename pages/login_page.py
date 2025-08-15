class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.locator("#username")
        self.password_field = page.locator("#password")

    def navigate(self):
        self.page.goto("https://example.com/login")

    def enter_credentials(self, username: str, password: str):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.page.click("button#login")