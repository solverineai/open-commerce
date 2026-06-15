import unittest

from opencommerce import ProfitEngine


class ProfitEngineTest(unittest.TestCase):
    def test_calculate_profit(self):
        result = ProfitEngine().calculate_profit(
            selling_price=35000,
            product_cost=17000,
            marketplace_fee=3500,
            payment_fee=900,
            shipping_cost=3200,
            ad_cost=2500,
        )

        self.assertEqual(result["gross_revenue"], 35000.0)
        self.assertEqual(result["total_costs"], 27100.0)
        self.assertEqual(result["net_profit"], 7900.0)
        self.assertEqual(result["margin_rate"], 0.2257)
        self.assertEqual(result["roi"], 0.2915)
        self.assertEqual(result["break_even_unit_price"], 27100.0)

    def test_margin_from_costs(self):
        margin = ProfitEngine().calculate_margin(revenue=100, total_costs=75)
        self.assertEqual(margin, 0.25)

    def test_break_even_for_quantity(self):
        break_even = ProfitEngine().calculate_break_even(
            unit_product_cost=10,
            marketplace_fee=5,
            payment_fee=3,
            quantity=2,
        )
        self.assertEqual(break_even, 14.0)

    def test_quantity_must_be_positive(self):
        with self.assertRaises(ValueError):
            ProfitEngine().calculate_profit(
                selling_price=100,
                product_cost=50,
                quantity=0,
            )


if __name__ == "__main__":
    unittest.main()
