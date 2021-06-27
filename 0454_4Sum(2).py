class Solution:
    # 1st brute-force solution
    # O(n^4) time | O(1) space
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        n = len(nums1)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for l in range(n):
                        if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:
                            count += 1
        return count
    
    # 2nd hashtable solution
    # O(n^2) time | O(n^2) space
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashtable = {}
        for a in nums1:
            for b in nums2 :
                if a + b in hashtable :
                    hashtable[a+b] += 1
                else :
                    hashtable[a+b] = 1
        count = 0         
        for c in nums3 :
            for d in nums4 :
                if -c - d in hashtable :
                    count += hashtable[-c-d]
        return count