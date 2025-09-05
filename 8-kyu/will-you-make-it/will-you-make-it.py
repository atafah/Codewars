def zero_fuel(distance_to_pump, mpg, fuel_left):
    can_travel = fuel_left * mpg
    return can_travel >= distance_to_pump