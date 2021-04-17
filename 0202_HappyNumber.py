class Solution:
    def isHappy(self, n: int) -> bool:
        # 1st solution
        # O(log n) time | O(log n) space
        # dic = []
        # while True:
        #     if n == 1:
        #         return True
        #     if n not in dic:
        #         dic.append(n)
        #         newN = 0
        #         for num in str(n):
        #             newN += int(num) * int(num)
        #         n = newN
        #     else:
        #         return False

        # 2nd solution
        # O(log n) time | O(1) space
        def digitSquareSum(n):
            squareSum = 0
            for num in str(n):
                squareSum += int(num) * int(num)
            return squareSum

        slow = digitSquareSum(n)
        fast = digitSquareSum(slow)
        while slow != fast:
            slow = digitSquareSum(slow)
            fast = digitSquareSum(fast)
            fast = digitSquareSum(fast)
        return slow == 1
