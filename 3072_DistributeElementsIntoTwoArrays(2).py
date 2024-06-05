# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        nums1 =[nums[0]]
        nums2 = [nums[1]]
        lst1 = [nums[0]]
        lst2 = [nums[1]]
        for i in range(2, len(nums)):
            a = len(nums1) - bisect.bisect_right(nums1, nums[i])
            b = len(nums2) - bisect.bisect_right(nums2, nums[i])
            if a > b:
                nums1.insert(len(nums1) - a, nums[i])
                lst1.append(nums[i])
            elif a < b:
                nums2.insert(len(nums2) - b, nums[i])
                lst2.append(nums[i])
            else:
                if len(nums1) <= len(nums2):
                    nums1.insert(len(nums1) - a, nums[i])
                    lst1.append(nums[i])
                else:
                    nums2.insert(len(nums2) - b, nums[i])
                    lst2.append(nums[i])
        return lst1 + lst2
