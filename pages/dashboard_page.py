from utils.config import MERCHANT_ID

class DashboardPage:

    def __init__(self, page):
        self.page = page

    def switch_merchant(self):
        # Wait for dashboard
        self.page.wait_for_load_state("networkidle")

        # Click switch merchant dropdown
        self.page.get_by_role("button", name="qa.gokwik").click()

        # Search merchant
        search_box = self.page.get_by_role("textbox")
        search_box.fill(MERCHANT_ID)

        # Select merchant radio button
        self.page.get_by_text(MERCHANT_ID).click()

        #Click on Set Merchant button
        self.page.click('button:has-text("Set Merchant")')

        # Wait for page reload
        self.page.wait_for_load_state("networkidle")