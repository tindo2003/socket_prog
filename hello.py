def funcPatternExpander(inputStr):
    
    char_stack = []
    current_str = ""
    i = 0
    while i < len(inputStr):
        if inputStr[i] == '(':
            char_stack.append(current_str)
            current_str = ""
        elif inputStr[i] == ')':
            i += 1
            num_start = i + 1
            while inputStr[i] != '}':
                i += 1
            repeat_times = int(inputStr[num_start:i])
            current_str = char_stack.pop() + current_str * repeat_times
        else:
            current_str += inputStr[i]
        i += 1

    return current_str