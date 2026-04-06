from utils.config import BASE_URL, EMAIL, PASSWORD, OTP

class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self):
        # Open site
        self.page.goto(BASE_URL)

        #locate & enter email
        self.page.fill('input[type="email"]', EMAIL)

        # Click next button
        self.page.click('button:has-text("Next")')

        # locate & enter password
        self.page.fill('input[type="password"]', PASSWORD)

        # Click next button
        self.page.click('button:has-text("Next")')

        # Wait for OTP screen
        self.page.wait_for_url("**/verify-otp")

        # locate & enter OTP
        otp_input = self.page.get_by_role("textbox")
        otp_input.wait_for()
        otp_input.fill(OTP)

        # click next button
        self.page.click('button:has-text("Next")')