def sort_people(people, minutes_per_dojo, minutes_per_turn):
    number_of_turns = minutes_per_dojo // minutes_per_turn
    
    turns = [tuple(people)] * number_of_turns
    turns[0] = turns[0][::-1]
    
    if turns[2:]:
        turns[2] = turns[2][::-1]
    
    return turns
