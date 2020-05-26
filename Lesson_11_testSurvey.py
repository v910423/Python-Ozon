import unittest
from Lesson_11_survey import survey

class TestSurvey(unittest.TestCase):

    def setUp(self):
        """создание опроаса"""
        question = 'the best language is? '
        self.mysurvey = survey(question)
        self.answers = ['python', 'c#', '1c', 'c++']

    def test_save_single_answer(self):
        self.mysurvey.save_answer(self.answers[0])
        self.assertIn(self.answers[0], self.mysurvey.answers)

    def test_save_all_answer(self):
        for each in self.answers:
            self.mysurvey.save_answer(each)
        for each in self.answers:
            self.assertIn(each, self.mysurvey.answers)

unittest.main()