class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1st solution
        a, b = 0, len(nums) - 1
        m = (a + b) // 2
        while a < b:
            if nums[m] == target:
                break
            if nums[a] <= nums[m]:
                if target == nums[a]:
                    m = a
                    break
                elif target < nums[a]:
                    a = m + 1
                else:
                    if target < nums[m]:
                        b = m - 1
                    else:
                        a = m + 1
            else:
                if target == nums[b]:
                    m = b
                    break
                elif target > nums[b]:
                    b = m - 1
                else:
                    if target > nums[m]:
                        a = m + 1
                    else:
                        b = m - 1
            m = (a + b) // 2
        return m if nums[m] == target else -1

        # 2nd solution
        a, b = 0, len(nums) - 1
        while a <= b:
            m = (a + b) // 2
            if nums[m] == target:
                return m
            if nums[a] <= nums[m]:
                if nums[a] <= target < nums[m]:
                    b = m - 1
                else:
                    a = m + 1
            else:
                if nums[m] < target <= nums[b]:
                    a = m + 1
                else:
                    b = m -1
        return -1
