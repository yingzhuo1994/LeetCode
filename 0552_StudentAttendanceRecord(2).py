# 1st solution
# O(n) time | O(1) space
class Solution:
    def checkRecord(self, n: int) -> int:
        '''
        res[0] ---> the number of answer which includes 'A' , not ending with 'L'
        res[1] ---> the number of answer which includes 'A', ending with one 'L'
        res[2] ---> the number of answer which includes 'A', ending with two 'L'
        res[3] ---> the number of answer which don't include 'A' , not ending with 'L'
        res[4] ---> the number of answer which don't include 'A' , ending with one 'L'
        res[5] ---> the number of answer which don't include 'A' , ending with two 'L'
        '''
        MOD = 10**9 + 7

        res = [1, 0, 0, 1, 1, 0]
        for i in range(1, n):
            temp = [0, 0, 0, 0, 0, 0]
            temp[0] = sum(res) % MOD
            temp[1] = res[0] % MOD
            temp[2] = res[1] % MOD
            temp[3] = (res[3] + res[4] + res[5]) % MOD
            temp[4] = res[3] % MOD
            temp[5] = res[4] % MOD
            res = temp
        return sum(res) % MOD