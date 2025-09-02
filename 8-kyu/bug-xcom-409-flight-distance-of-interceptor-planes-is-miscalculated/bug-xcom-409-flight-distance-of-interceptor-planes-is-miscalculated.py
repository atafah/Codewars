# speed of aircrafts is given in *knots*
# travelTime is in *minutes*
# travel distance should be returned in *kilometers*
​
def travel_distance(avg_speed, travel_time):
    KM_PER_MILE = 1.609344
    
    travel_hours = travel_time / 60
    
    travel_kms = avg_speed * 1.852 * travel_hours
    
    return travel_kms