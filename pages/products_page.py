from utils.config import MERCHANT_ID

class ProductsPage:

    def __init__(self, page):
        self.page = page

    def go_to_products(self):
        url = f"https://qa-mdashboard.dev.gokwik.in/gk-pages/store/{MERCHANT_ID}/products"
        self.page.goto(url)

    def is_products_page_loaded(self):
        return "products" in self.page.url.lower()

    def click_add_product(self):
        self.page.locator('[data-test-id="products_add_button"]').click()

    def create_product(self, product_name):
        import time

        self.click_add_product()

        #Locate & enter product namme
        title_input = self.page.locator('[data-test-id="title_input"]')
        title_input.wait_for()
        title_input.fill(product_name)

        #locate & enter prduct SKU
        sku = f"SKU_{int(time.time())}"
        self.page.locator('[data-test-id="inventory_card_sku_input"]').fill(sku)

        #Click on Create product button
        self.page.get_by_role("button", name="Create Product").click()

        # Wait for products page
        self.page.wait_for_timeout(3000)

        #Force navigating to listing page as auto-navigation not working
        self.page.goto(f"https://qa-mdashboard.dev.gokwik.in/gk-pages/store/{MERCHANT_ID}/products")

        return sku

    def search_product(self, product_name):
        search_box = self.page.get_by_role("textbox")
        search_box.fill(product_name)

        self.page.wait_for_timeout(1000)  # small wait for filtering

    def is_product_visible(self, product_name):
        return self.page.get_by_text(product_name).is_visible()
    
    def delete_product(self, product_name):

        #Search product
        self.search_product(product_name)

        #Wait for product row
        product_row = self.page.locator(f"text={product_name}").first
        product_row.wait_for()

        #Select the checkbox
        self.page.locator('input[data-test-id^="generic_table_row_checkbox"]').first.click()

        #Click 3-dot menu
        self.page.locator('[data-test-id="bulk_action_toolbar_more_actions_button"]').click()

        #Click Delete Products option
        self.page.locator("span:has-text('Delete products')").click()

       #Confirm Delete from pop-up
        self.page.get_by_role("button", name="OK").click()

       #Wait for deletion
        self.page.wait_for_timeout(2000)