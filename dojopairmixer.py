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
        
    raw_input("Press any key to start the Dojo")
    for t, (pilot, copilot) in enumerate(turns):
        if sys.platform.startswith("linux"):
            os.system("clear")
        elif sys.platform.startswith("win"):
            os.system("cls")
        else:
            print "\n" * 80
            
        print time.strftime("[%H:%M:%S %x]")
        
        print "<current>\t%d.  %-15s + %-15s" % (t+1, pilot, copilot)
        if t < len(turns) - 1:
            print "<next>\t\t%d.  %-15s + %-15s" % (t+2, turns[t+1][0], turns[t+1][1])
        
        time.sleep(minutes_per_turn * 60)
        msg = "Time is over! Press OK to continue\n\nThis time: %s and %s" % (turns[t+1][0], turns[t+1][1])
        if sys.platform.startswith("linux"):
            return_code = os.system("zenity --info --text %r" % msg)
        elif sys.platform.startswith("win"):
            return_code = os.system("echo WScript.Echo(%r); > tmp.js & wscript tmp.js & del tmp.js" % msg)
        else:
            return_code = 1
        if return_code != 0:
            raw_input("Time is over! Press any key to continue")
    raw_input("The Dojo is over. Press any key to end")


if __name__ == '__main__':
    import os
    import sys
    import time
    _main()
