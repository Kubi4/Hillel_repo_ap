import unittest

from lesson_12.homeworks import sum_of_2_numbers, reverse_string, order_price, pages_quantity


class TestSumOf2Numbers(unittest.TestCase):
    def test_sum_of_2_numbers_positive(self):
        self.assertEqual(sum_of_2_numbers(2,3), 5)
    def test_sum_of_2_numbers_negative(self):
        self.assertEqual(sum_of_2_numbers(-2,-3), -5)
        self.assertEqual(sum_of_2_numbers(2,-3), -1)
        self.assertEqual(sum_of_2_numbers(-2, 3), 1)
    def test_sum_of_2_numbers_with_zero(self):
        self.assertEqual(sum_of_2_numbers(2,0), 2)
        self.assertEqual(sum_of_2_numbers(0,3), 3)
        self.assertEqual(sum_of_2_numbers(0, 0), 0)

class TestReverseString(unittest.TestCase):
    def test_reverse_string_reversing(self):
        self.assertEqual(reverse_string("String"), "gnirtS")
    def test_reverse_string_is_str(self):
        self.assertIsInstance(reverse_string("String"), str)
class TestOrderPrice(unittest.TestCase):
    def test_order_price_many_items(self):
        self.assertEqual(order_price({100:2, 200:3, 300:4}), (100*2+200*3+300*4))
    def test_order_price_one_item(self):
        self.assertEqual(order_price({100:2}), (100*2))
    def test_order_price_empty_order(self):
        self.assertEqual(order_price({}), 0)
    def test_order_price_zero_quantity(self):
        self.assertEqual(order_price({100:0,200:3}), (200*3))
    def test_order_price_zero_price(self):
        self.assertEqual(order_price({0:1, 200:3}), (200*3))

class TestPagesQuantity(unittest.TestCase):
    def test_pages_quantity_division(self):
        self.assertEqual(pages_quantity(20, 5), 4)
    def test_pages_quantity_last_page_not_empty(self):
        self.assertEqual(pages_quantity(23, 5), 5)
    def test_pages_quantity_one_photo(self):
        self.assertEqual(pages_quantity(1, 5), 1)
    def test_pages_quantity_without_photos(self):
        self.assertEqual(pages_quantity(0, 5), 0)
    def test_pages_quantity_one_photo_per_page(self):
        self.assertEqual(pages_quantity(3, 1), 3)
    def test_pages_quantity_all_photos_on_one_page(self):
        self.assertEqual(pages_quantity(3, 10), 1)

if __name__ == '__main__':
    unittest.main()