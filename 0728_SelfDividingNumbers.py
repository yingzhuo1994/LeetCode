class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isValid(number):
            for ch in str(number):
                d = int(ch)
                if d == 0:
                    return False
                if number % d != 0:
                    return False
            return True
        
        ans = []
        for number in range(left, right + 1):
            if isValid(number):
                ans.append(number)
        
        return ans