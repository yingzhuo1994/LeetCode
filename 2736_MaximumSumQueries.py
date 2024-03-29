# 1st solution, TLE
class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        dic = {}
        for a, b in zip(nums1, nums2):
            if a not in dic:
                dic[a] = b
            else:
                dic[a] = max(dic[a], b)
        
        nums = list(dic.keys())
        nums.sort()

        def query(x, y):
            start, end = 0, len(nums)
            while start < end:
                mid = start + (end - start) // 2
                if nums[mid] < x:
                    start = mid + 1
                else:
                    end = mid
            if start >= len(nums):
                return -1
            array = [[dic[nums[i]], dic[nums[i]] + nums[i]] for i in range(start, len(nums))]
            array.sort()
            left, right = 0, len(array)
            while left < right:
                mid = left + (right - left) // 2
                if array[mid][0] < y:
                    left = mid + 1
                else:
                    right = mid
            
            if left >= len(array):
                return -1
            
            return max([array[i][1] for i in range(left, len(array))])
        
        return [query(x, y) for x, y in queries]

# 2nd solution
# O(n * log(⁡n)+ q * log(⁡q) + q * log(⁡n)) time 
# O(n + q) space
class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        a = sorted(((a, b) for a, b in zip(nums1, nums2)), key=lambda p: -p[0])
        j = 0
        st = []
        for i, (x, y) in sorted(enumerate(queries), key=lambda p: -p[1][0]):
            while j < len(a) and a[j][0] >= x:  # 下面只需关心 ay (a[j][1])
                ax, ay = a[j]
                while st and st[-1][1] <= ax + ay:  # ay >= st[-1][0]
                    st.pop()
                if not st or st[-1][0] < ay:
                    st.append((ay, ax + ay))
                j += 1
            p = bisect_left(st, (y,))
            if p < len(st):
                ans[i] = st[p][1]
        return ans
