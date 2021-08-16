import unittest
import miniProject as prog

class TestMyProgram(unittest.TestCase):
    def test_totalgrp1(self):
        data = prog.grp1['Calories']
        result = round(prog.EvaluateMarks.totalgrp1(data), 1)
        self.assertEqual(result, 3637.2)

    def test_meangrp1(self):
        data = prog.grp1['Calories']
        result = round(prog.EvaluateMarks.meangrp1(data), 1)
        self.assertEqual(result, 330.7)

    def test_totalgrp2(self):
        data = prog.grp2['Calories']
        result = round(prog.EvaluateMarks.totalgrp2(data), 1)
        self.assertEqual(result, 2782.2)

    def test_meangrp2(self):
        data = prog.grp2['Calories']
        result = round(prog.EvaluateMarks.meangrp2(data), 1)
        self.assertEqual(result, 278.2)

    def test_totalgrp3(self):
        data = prog.grp3['Calories']
        result = round(prog.EvaluateMarks.totalgrp3(data), 1)
        self.assertEqual(result, 2939.2)

    def test_meangrp3(self):
        data = prog.grp3['Calories']
        result = round(prog.EvaluateMarks.meangrp3(data), 1)
        self.assertEqual(result, 293.9)