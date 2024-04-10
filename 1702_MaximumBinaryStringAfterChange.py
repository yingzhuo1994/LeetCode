# 1st solution
# O(n) time | O(n) space
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        n = len(binary)
        zeros = binary.count("0")
        if zeros <= 1:
            return binary
        idx = 0
        for i in range(n):
            if binary[i] == "0":
                idx = i
                break
        return binary[:idx] + ("1" * (zeros - 1)) + "0" + ("1" * (n - idx - zeros))
        

            

