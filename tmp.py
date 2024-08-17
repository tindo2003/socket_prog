def funcHopSkipJump(matrix):
    # Define the directions for counter-clockwise movement
    # Down -> Right -> Up -> Left
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    n = len(matrix)
    m = len(matrix[0])
    dir_idx = 0  # Start with moving down

    row, col = 0, 0  # Start from the top-left corner (0, 0)
    visited = [[False] * m for _ in range(n)]  # To track visited cells
    visited[row][col] = True  # Mark the starting cell as visited

    steps = 0  # To count the steps taken



    while True:
        # Skip alternate cells by moving twice
        print("start moving twice")
        for _ in range(2):
            
            # Find the next cell in the current direction
            next_row = row + directions[dir_idx][0]
            next_col = col + directions[dir_idx][1]
            print(next_row, next_col)
            

            # If next cell is within bounds and not visited, move to it
            if 0 <= next_row < n and 0 <= next_col < m and not visited[next_row][next_col]:
                row, col = next_row, next_col
                visited[row][col] = True
            else:
                # Change direction counter-clockwise
                print("not within bound")
                dir_idx = (dir_idx + 1) % 4
                next_row = row + directions[dir_idx][0]
                next_col = col + directions[dir_idx][1]

                # If after changing direction, we can't move, we're done
                if not (0 <= next_row < n and 0 <= next_col < m and not visited[next_row][next_col]):
                    print("i am done")
                    return matrix[row][col]
                row, col = next_row, next_col
                print(f"changed dir to {row},{col}")
                visited[row][col] = True

        # Increment the step count
        steps += 1

        # If no further valid moves exist, return the current cell's value
        if steps == n * m:
            break

    return matrix[row][col]

# Example usage with the provided input:
n, m = 3, 4
matrix = [
    [9, 8, 7, 6],
    [5, 4, 3, 2],
    [1, 10, 11, 12]
]

result = funcHopSkipJump(matrix)
print(result)  # Expected output: 4
