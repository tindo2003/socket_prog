class Logger:
    """
    @param timestamp: Timestamp
    @param message: Message
    @return: Whether the log can be printed
    """
    def __init__(self):
        self.my_dict = {}
    def could_print_message(self, timestamp: int, message: str) -> bool:
        # --- write your code here ---
        if message not in self.my_dict or self.my_dict[message] + 10 <= timestamp:
            self.my_dict[message] = timestamp    
            return True
        return False