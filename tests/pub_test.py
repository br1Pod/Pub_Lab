# tests/pub_test.py

import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink


class TestPub(unittest.TestCase):
    
    def setUp(self): 
      self.pub = Pub("Casino Royale", 100)
      self.drink = Drink("Vodka Martini", 10, 50)
      self.customer = Customer("Bond, James Bond", 50, 53)


    # @unittest.skip("Delete this line to run the test")
    def test_has_name(self):
        self.assertEqual("Casino Royale", self.pub.name)

    # @unittest.skip("Delete this line to run the test")
    def test_total_till(self):
        self.assertEqual(100, self.pub.till)

    # @unittest.skip("Delete this line to run the test")
    def test_increase_till(self):
        self.pub.increase_till(self.drink)
        self.assertEqual(110, self.pub.till)

    # @unittest.skip("Delete this line to run the test")
    def test_check_age(self):
        self.assertEqual(True, self.pub.check_age(self.customer))

    # # @unittest.skip("Delete this line to run the test")
    # def test_refuse_service(self):
    #     self.assertEqual("Get Out", self.pub.refuse_service(self.customer))    