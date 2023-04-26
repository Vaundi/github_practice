import unittest
import dec_2_hex as dh


class dhTestCase(unittest.TestCase):

    def test_dh1(self):
        answer = dh.decimal_to_hex(100)
        self.assertEqual(answer, "0x64")

    def test_dh2(self):
        answer = dh.decimal_to_hex(15)
        self.assertEqual(answer, "0xf")


if __name__ == "__main__":
    unittest.main()
