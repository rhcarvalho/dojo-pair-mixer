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
