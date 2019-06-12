import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print("veryGood")
        self.assertEqual(False, True)

    def testTwo(self):
        try:
            print("good")
            self.assertTrue(False, "Кек чебурек")
        except:
            print("bad")


if __name__ == '__main__':
    unittest.main()
