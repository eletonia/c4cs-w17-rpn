import readline
import unittest
import rpn
import sys
from termcolor import colored, cprint

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	def test_subtract(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)
	def test_exponentation(self):
		result = rpn.calculate('2 3 ^')
		self.assertEqual(8, result)