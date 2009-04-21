#!/usr/bin/env python

import unittest
from dojopairmixer import *


class BaseTestCase(unittest.TestCase):
    def assertEqual(self, first, second, msg=None):
        if msg is not None:
            msg += ' (%r != %r)' % (first, second)
        super(BaseTestCase, self).assertEqual(first, second, msg)


class DojoWithTwoPeopleTests(BaseTestCase):
    def test_one_turn_dojo_with_two_people(self):
        people = ["John", "Peter"]
        minutes_per_dojo, minutes_per_turn = 7, 7
        
        turns = sort_people(people, minutes_per_dojo, minutes_per_turn)
        
        self.assertTrue(turns in ([("John", "Peter")],
                                  [("Peter", "John")]),
            "Given two participants and time for only one turn, "
            "the turn should be one of the only two possible setups")

    def test_two_turn_dojo_with_two_people(self):
        people = ["John", "Peter"]
        minutes_per_dojo, minutes_per_turn = 15, 7
        
        turns = sort_people(people, minutes_per_dojo, minutes_per_turn)
        
        self.assertEqual(len(turns), 2,
            "Given enough time to run two turns, there should be the two")
        self.assertTrue(people[0] in turns[0],
            "Given two participants, one should always be in a turn")
        self.assertTrue(turns[0] != turns[1],
            "Subsequent turns should not repeat pairs in the same role")

    def test_three_turn_dojo_with_two_people(self):
        people = ["John", "Peter"]
        minutes_per_dojo, minutes_per_turn = 25, 7
        
        turns = sort_people(people, minutes_per_dojo, minutes_per_turn)
        
        self.assertEqual(len(turns), 3,
            "Given enough time to run three turns, there should be the three")
        self.assertTrue(people[0] in turns[0],
            "Given two participants, one should always be in a turn")
        self.assertTrue(turns[0] != turns[1] and turns[1] != turns[2],
            "Subsequent turns should not repeat pairs in the same role")

    
if __name__ == '__main__':
    unittest.main()

