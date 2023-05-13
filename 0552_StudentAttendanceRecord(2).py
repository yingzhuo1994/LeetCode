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

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        valid_late_present = [0] * (n+1)
        valid_late_present[1] = 2 
            
        end_with_L = 1
        end_with_LL = 0
        end_with_P = 1
            
        for i in range(2,n+1):
            new_end_with_L = end_with_P
            new_end_with_LL = end_with_L
            new_end_with_P = end_with_L + end_with_LL + end_with_P
            valid_late_present[i] = new_end_with_L + new_end_with_LL + new_end_with_P
            # update the old variables with the new variables' values
            end_with_P = new_end_with_P % MOD
            end_with_L = new_end_with_L % MOD
            end_with_LL = new_end_with_LL % MOD
        
        # calucalte absents
        valid_late_present[0] = 1 
        strings_with_a = 0
        for i in range(n):
            strings_with_a += (valid_late_present[i] * valid_late_present[n - i - 1])
            strings_with_a %= MOD

        ans = strings_with_a + valid_late_present[n]
        
        return ans % MOD