def find_non_overlapping_intervals(lamps):
    # Generate events for all lamps
    events = []
    for lamp in lamps:
        x, r = lamp
        events.append((x - r, 1))  # Start event
        events.append((x + r, -1))  # End event

    events.sort()

    coverage = 1
    previous_pos = events[0][0]
    res = 0

    for position, event_type in events[1:]:
        old = coverage
        if event_type == 1:
            coverage += 1
        else:
            coverage -= 1
        if old == 1:
            res += position - previous_pos
        previous_pos = position
    return res


# Example usage:
lamps = [
    [-2, 3],  # Lamp at position 1 with radius 2 (covers from -1 to 3)
    [2, 3],  # Lamp at position 3 with radius 1 (covers from 2 to 4)
    [2, 1],  # Lamp at position 5 with radius 2 (covers from 3 to 7)
]

res = find_non_overlapping_intervals(lamps)
print("Non-overlapping intervals where only one lamp shines:")
print(res)
