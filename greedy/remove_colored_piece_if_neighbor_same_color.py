class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_counter, b_counter = 0, 0
        consecutive = 1
        
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                consecutive += 1
            else:
                if consecutive > 2:
                    if colors[i-1] == "A":
                        a_counter += consecutive - 2
                    else:
                        b_counter += consecutive - 2
                consecutive = 1

        # Handle the last sequence
        if consecutive > 2:
            if colors[-1] == "A":
                a_counter += consecutive - 2
            else:
                b_counter += consecutive - 2
        
        return a_counter > b_counter
