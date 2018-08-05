import unittest
from unittest_version import convert_up_low


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        keyw = 'abcdD'
        method = 'low'
        result = convert_up_low.convert_up_low().convert_up_low(keyw, method)
        if method == 'upper':
            self.assertEqual(result,keyw.upper())
        else:
            self.assertEqual(result, keyw.lower())

    def test_something2(self):
        keyw = 'abcd324D'
        method = 'low'
        result = convert_up_low.convert_up_low().convert_up_low(keyw, method)
        if method == 'upper':
            self.assertEqual(result, keyw.upper())
        else:
            self.assertEqual(result, keyw.lower())

    def test_something3(self):
        keyw = 'abcdD'
        method = 'upper'
        result = convert_up_low.convert_up_low().convert_up_low(keyw, method)
        if method == 'upper':
            self.assertEqual(result, keyw.upper())
        else:
            self.assertEqual(result, keyw.lower())

    def test_something4(self):
        keyw = 'abcdD342'
        method = 'upper'
        result = convert_up_low.convert_up_low().convert_up_low(keyw, method)
        if method == 'upper':
            self.assertEqual(result, keyw.upper())
        else:
            self.assertEqual(result, keyw.lower())




                    #
    # def test_md51(self):
    #     keyw = 'abcdD'
    #     self.assertEqual(demo.search_baidu().md5(keyw),demo.search_baidu().md52(keyw))

if __name__ == '__main__':
    unittest.main()
