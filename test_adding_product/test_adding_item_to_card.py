class TestCard:
    def test_addin_product_to_card(self, app):
        app.add_product_to_card(3)
        assert app.get_count_product_in_card() == 3
        app.delete_products_from_card()
        assert app.get_count_product_in_card() == 0



