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

        # 2nd solution
        # O(n) time | O(1) space
        lst = []
        for i in range(1, n + 1):
            divisible_by_3 = (i % 3 == 0)
            divisible_by_5 = (i % 5 == 0)
            if divisible_by_3 and divisible_by_5:
                lst.append("FizzBuzz")
            elif divisible_by_3:
                lst.append("Fizz")
            elif divisible_by_5:
                lst.append("Buzz")
            else:
                lst.append(str(i))
        return lst

        # 3rd solution without "%" operation
        # O(n) time | O(1) space
        lst = []
        fizz, buzz = 0, 0
        for i in range(1, n + 1):
            fizz += 1
            buzz += 1
            if fizz == 3 and buzz == 5:
                lst.append("FizzBuzz");
                fizz = 0
                buzz = 0
            elif fizz == 3:
                lst.append("Fizz")
                fizz = 0
            elif buzz == 5:
                lst.append("Buzz")
                buzz = 0
            else:
                lst.append(str(i))
        return lst
