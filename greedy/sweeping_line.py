def find_most_illuminated_point(lamps):
    '''
    sweeping line algo
    '''
    events = []
    for coord, radius in lamps:
        events.append((coord - radius, 1))  # Start of illumination
        events.append((coord + radius + 1, -1))  # End of illumination

    events.sort(key=lambda x: (x[0], -x[1]))  # Sort events

    current_illumination = 0
    max_illumination = 0
    most_illuminated_point = float('inf')

    for point, event_type in events:
        current_illumination += event_type
        if current_illumination > max_illumination:
            max_illumination = current_illumination
            most_illuminated_point = point
        elif current_illumination == max_illumination:
            most_illuminated_point = min(most_illuminated_point, point)

    return most_illuminated_point

# Example usage
lamps = [[-2,3],[2,3],[2, 1]]
result = find_most_illuminated_point(lamps)
print(f"The point illuminated by the highest number of lamps is: {result}")