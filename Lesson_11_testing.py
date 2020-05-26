import unittest

from Lesson_11_name import format_name

class NameTest(unittest.TestCase):
    """тесты для функции"""

    def test1(self):
        formated = format_name('ivan', 'ivanov')
        self.assertEqual(formated, 'Ivan Ivanov')

    def test2(self):
        formated = format_name('ivan', 'ivanov', 'ivanovich')
        self.assertEqual(formated, 'Ivan Ivanov Ivanovich')
        self.assertNotEqual()
        self.assertTrue()
        self.assertIn()
        self.assertNotIn()

unittest.main()
print(dir(unittest.TestCase))