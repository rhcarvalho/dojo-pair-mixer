#!/usr/bin/env python

import unittest
from dojopairmixer import *


class BaseTestCase(unittest.TestCase):
    def assertEqual(self, first, second, msg=None):
        if msg is not None:
            msg += ' (%r != %r)' % (first, second)
        super(BaseTestCase, self).assertEqual(first, second, msg)


class DojoPremissesTests(BaseTestCase):
    def test_two_participants_per_turn(self):
        people = ["John", "Peter", "Evan", "Anthony", "Laura", "Cindy"]
        minutes_per_dojo, minutes_per_turn = 120, 7
        
        turns = sort_people(people, minutes_per_dojo, minutes_per_turn)
        
        self.assertTrue(all(len(turn) == 2 for turn in turns),
            "A turn should always have exactly "
            "two participants (pilot and co-pilot)")

    def test_no_solo_turn(self):
        people = ["John", "Peter", "Evan", "Anthony", "Laura", "Cindy"]
        minutes_per_dojo, minutes_per_turn = 120, 7
        
        turns = sort_people(people, minutes_per_dojo, minutes_per_turn)
        
        self.assertTrue(all(pilot != copilot for pilot, copilot in turns),
            "A turn should not be solo "
            "(pilot and co-pilot should not be the same person)")


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


class DojoWithThreePeopleTests(BaseTestCase):
    def test_two_turn_dojo_with_three_people(self):
        people = ["John", "Peter", "Evan"]
        minutes_per_dojo, minutes_per_turn = 15, 7
        
        turns = sort_people(people, minutes_per_dojo, minutes_per_turn)
        
        self.assertEqual(len(turns), 2,
            "Given enough time to run two turns, there should be the two")
        self.assertEqual(set(people), set(turns[0] + turns[1]),
            "Given three participants, they all should always "
            "be in the first two turns")

    
if __name__ == '__main__':
    unittest.main()

