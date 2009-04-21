def sort_people(people, minutes_per_dojo, minutes_per_turn):
    number_of_turns = minutes_per_dojo // minutes_per_turn
    
    return [tuple(people)] * number_of_turns
