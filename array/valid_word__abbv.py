class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def valid_word_abbreviation(self, word: str, abbr: str) -> bool:
        # write your code here
        idx = 0 
        abbr = list(abbr)
        N = len(abbr)
        num = ""
        for r in range(N):
            cur_ele = abbr[r]
            if cur_ele.isdigit():
                if len(num) == 0 and cur_ele == '0':
                    return False
                num += cur_ele
            else:
                if num:
                    num_int = int(num)
                else:
                    num_int = 0
                while num_int > 0:
                    idx += 1
                    num_int -= 1
                num = ""
                if word[idx] != cur_ele:
                    return False  
                idx += 1
        
        if idx < len(word):
            if len(num) == 0: return False
            num_int = int(num)
            while num_int > 0:
                # abbr overshoots
                if idx >= len(word):
                    return False 
                num_int -= 1
                idx += 1
        elif len(num) > 0: 
            return False 
        return True
    '''
    apple ape
    a2e   ape
    '''