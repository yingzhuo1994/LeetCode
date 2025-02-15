# 1st solution
# O(n * logU) time | O(n * logU) space
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        st = set()
        for i, x in enumerate(arr):
            st.add(x)
            for j in range(i - 1, -1, -1):
                if arr[j] | x == arr[j]:
                    break
                arr[j] |= x
                st.add(arr[j])
        return len(st)