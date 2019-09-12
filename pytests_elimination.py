# Testing the code
import unittest
from parentheses_matching_elimination import check

class TestSum(unittest.TestCase):

    def test_01(self):
        self.assertEqual(check("(a[0]+b[2c[6]]){24+53}"), True, "True")

    def test_02(self):
        self.assertEqual(check("f(e(d))"), True, "True")

    def test_03(self):
        self.assertEqual(check("[()]{}([])"), True, "True")

    def test_04(self):
        self.assertEqual(check("((b)"), False, "False")

    def test_05(self):
        self.assertEqual(check("(c]"), False, "False")

    def test_06(self):
        self.assertEqual(check("{(a[])"), False, "False")

    def test_07(self):
        self.assertEqual(check("([)]"), False, "False")

    def test_08(self):
        self.assertEqual(check(")("), False, "False")

    def test_09(self):
        self.assertEqual(check(""), False, "False")

if __name__ == '__main__':
    unittest.main()
