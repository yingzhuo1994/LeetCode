class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # 1st solution
        # O(n) time | O(1) space
        lst = [str(i) for i in range(1, n + 1)]
        for i in range(n // 3):
            lst[2 + i * 3] = "Fizz"
        for i in range(n // 5):
            lst[4+ i * 5] = "Buzz"
        for i in range(n // 15):
            lst[14 + i * 15] = "FizzBuzz"
        return lst
