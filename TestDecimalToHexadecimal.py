import unittest

from decimal_to_hexadecimal import decimal_to_hexadecimal


class TestDecimalToHexadecimal(unittest.TestCase):

    def test_decimal_to_hexadecimal_1(self):
        self.assertEqual(decimal_to_hexadecimal(12), "0xc")

    def test_decimal_to_hexadecimal_16(self):
        self.assertEqual(decimal_to_hexadecimal(16), "0x10")

    def test_decimal_to_hexadecimal_255(self):
        self.assertEqual(decimal_to_hexadecimal(255), "0xff")


if __name__ == "__main__":
    unittest.main()
