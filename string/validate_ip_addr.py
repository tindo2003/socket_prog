class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        elements = queryIP.split(".")
        
        if len(elements) == 4:
            for ele in elements:
                if len(ele) > 1:
                    if ele[0] == "0": return "Neither"
                if not ele.isdigit(): return "Neither"
                if int(ele) < 0 or int(ele) > 255:  return "Neither"
            return "IPv4"

        elements = queryIP.split(":")
        if len(elements) == 8:
            for ele in elements:
                if len(ele) == 0 or len(ele) > 4: 
                    print("here")
                    return "Neither"
                for c in ele:
                    if not ('A' <= c <= 'F' or 'a' <= c <= 'f' or c.isdigit()):
                        print("here")
                        return "Neither"
            return "IPv6"
        return "Neither"