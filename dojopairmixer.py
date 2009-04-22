#!/usr/bin/env python

import random
from itertools import cycle


def sort_people(people, minutes_per_dojo, minutes_per_turn):
    number_of_turns = minutes_per_dojo // minutes_per_turn
    
    random.shuffle(people)
    
    turns = []
    people_iterator = cycle(people)
    pilot, copilot = people_iterator.next(), people_iterator.next()
    
    while len(turns) < number_of_turns:
        turns.append((pilot, copilot))
        pilot, copilot = copilot, people_iterator.next()
    
    return turns


def _main():
    args = sys.argv[1:]
    if len(args) < 2:
        print "usage: %s NAMES_FILE MINUTES_PER_DOJO [MINUTES_PER_TURN]" % sys.argv[0]
        sys.exit(1)
    people, minutes_per_dojo = args[:2]
    if args[2:]:
        minutes_per_turn = args[2]
    else:
        minutes_per_turn = 7
    
    people = open(people).read().splitlines()
    minutes_per_dojo, minutes_per_turn = int(minutes_per_dojo), int(minutes_per_turn)
    turns = sort_people(people, minutes_per_dojo, minutes_per_turn)
    
    for t, (pilot, copilot) in enumerate(turns):
        print "%d.  %-15s + %-15s" % (t+1, pilot, copilot)


if __name__ == '__main__':
    import sys
    _main()
