def place_base_stations(A):
    # Sort the house positions in increasing order
    A.sort()
    
    # Initialize the variable to keep track of the number of base stations placed
    num_base_stations = 0
    
    # Start with the left-most house
    left_most_house = A[0]
    
    # Continue until all houses are covered
    while A:
        # Place a base station 4km to the right of the left-most house
        base_station_position = left_most_house + 4
        
        # Increment the count of base stations placed
        num_base_stations += 1
        
        # Remove houses covered by this base station
        A = [house for house in A if house > base_station_position]
        
        # If there are remaining houses, update the left-most house
        if A:
            left_most_house = A[0]
    
    return num_base_stations

# Example usage
houses = [1, 5, 9, 12, 18, 22, 25]
print("Minimum number of base stations required:", place_base_stations(houses))
