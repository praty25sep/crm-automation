def test_create_product(page):
    from pages.login_page import LoginPage
    from pages.dashboard_page import DashboardPage
    from pages.products_page import ProductsPage
    import time

    login = LoginPage(page)
    dashboard = DashboardPage(page)
    products = ProductsPage(page)

    product_name = f"TestProduct_{int(time.time())}"

    login.login()
    dashboard.switch_merchant()
    products.go_to_products()

    products.create_product(product_name)
    products.search_product(product_name)
    assert products.is_product_visible(product_name), "Product not visible after creation"


    assert products.is_product_visible(product_name)

    products.delete_product(product_name)
    products.search_product(product_name)
    assert not products.is_product_visible(product_name), "Product still visible after deletion"