import unittest
from demo3_pytest_version import convert_md5


class MyTestCase(unittest.TestCase):
    def test_letters(self):
        keyw = 'abcdD'
        self.assertEqual(convert_md5.convert_md5().md5(keyw),convert_md5.convert_md5().md52(keyw) )

    def test_numbers(self):
        keyw = '1234'
        self.assertEqual(convert_md5.convert_md5().md5(keyw),convert_md5.convert_md5().md52(keyw) )

    def test_empty(self):
        keyw = ''
        self.assertEqual(convert_md5.convert_md5().md5(keyw),convert_md5.convert_md5().md52(keyw) )

    def test_space(self):
        keyw = ' '
        self.assertEqual(convert_md5.convert_md5().md5(keyw),convert_md5.convert_md5().md52(keyw) )

if __name__ == '__main__':
    unittest.main()
