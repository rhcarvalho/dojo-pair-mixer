#!/usr/bin/env python

import unittest
from dojopairmixer import *


class Tests(unittest.TestCase):
    def test_one_turn_dojo_with_two_people(self):
        people = ["John", "Peter"]
        minutes_per_dojo, minutes_per_turn = 7, 7
        
        turns = sort_people(people, minutes_per_dojo, minutes_per_turn)
        
        self.assertTrue(turns in ([("John", "Peter")],
                               [("Peter", "John")]))

    def test_two_turn_dojo_with_two_people(self):
        people = ["John", "Peter"]
        minutes_per_dojo, minutes_per_turn = 15, 7
        
        turns = sort_people(people, minutes_per_dojo, minutes_per_turn)
        
        self.assertEqual(len(turns), 2)
        self.assertTrue(people[0] in turns[0])

    
if __name__ == '__main__':
    unittest.main()

