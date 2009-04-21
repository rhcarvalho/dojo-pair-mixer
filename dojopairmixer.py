import random
import math

def sort_people(people, minutes_per_dojo, minutes_per_turn):
    number_of_turns = minutes_per_dojo // minutes_per_turn
    
    random.shuffle(people)
    people *= int(math.ceil(2.0 * number_of_turns / len(people)))
    
    turns = []
    
    for i in range(0, len(people), 2):
        turns.append((people[i], people[i+1]))
    
    return turns[:number_of_turns]
