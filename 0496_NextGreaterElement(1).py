# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1 for _ in nums1]
        for i in range(len(nums1)):
            state = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    state = True
                if nums1[i] < nums2[j] and state:
                    result[i] = nums2[j]
                    break
        return result

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]):
        stack, dic = [], {}
        for num in nums2:
            while stack and stack[-1] < num:
                dic[stack.pop()] = num
            stack.append(num)
        
        return [dic.get(x, -1) for x in nums1]