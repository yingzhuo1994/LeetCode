class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        # 1st solution
        # O(nlogn) time | O(n) space
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

        # 2nd solution
        # O(nlogn) time | O(n) space
        self.mergeSort(nums)
        result = ''.join(map(str, nums))
        return result if result[0] != '0' else '0'
    
    def mergeSort(self, arr: List[int]):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            self.mergeSort(L)
            self.mergeSort(R)
            i = j = k = 0
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if int(str(L[i]) + str(R[j])) >= int(str(R[j]) + str(L[i])):
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1