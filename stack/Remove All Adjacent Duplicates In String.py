class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for c in s:
            if st:
                if c == st[-1]:
                    st.pop()
                else:
                    st.append(c)
            else:
                st.append(c)
        return "".join(st)
