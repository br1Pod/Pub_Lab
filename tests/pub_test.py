# tests/pub_test.py

import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    
    def setUp(self): 
      self.pub = Pub("Casino Royale", 100.00)

