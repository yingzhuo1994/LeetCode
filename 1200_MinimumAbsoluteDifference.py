# 1st solution, TLE
# O(n^2) time | O(n^2) space
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        minDiff = float("inf")

        arr.sort()
        for i in range(len(arr)):
            for j in range(i):
                a, b = arr[j], arr[i]
                diff = b - a
                if diff > minDiff:
                    continue
                dic[diff].append([a, b])
                minDiff = min(minDiff, diff)
        return dic[minDiff]

# 2nd solution
# O(n*log(n)) time | O(n) space
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        answer = []
        minDiff = float("inf")

        arr.sort()
        for i in range(1, len(arr)):
            a, b = arr[i - 1], arr[i]
            diff = b - a
            if diff == minDiff:
                answer.append([a, b])
            elif diff < minDiff:
                answer = [[a, b]]
                minDiff = min(minDiff, diff)

        return answer

# 3rd solution, Counting Sort
# O(m + n) time | O(m + n) space
# where m is the difference betwee max and min values of arr.
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Initialize the auxiliary array `line`.
        # Keep a record of the minimum element and the maximum element.
        min_element = min(arr)
        max_element = max(arr)
        shift = -min_element
        line = [0] * (max_element - min_element + 1)
        answer = []
        
        # For each integer `num` in `arr`, we increment line[num + shift] by 1.
        for num in arr:
            line[num + shift] = 1
        
        # Start from the index representing the minimum integer, initialize the 
        # absolute difference `min_pair_diff` as a huge value such as
        # `max_element - min_element` in order not to miss the absolute 
        # difference of the first pair.
        min_pair_diff = max_element - min_element
        prev = 0
        
        # Iterate over the array `line` and check if line[curr] 
        # holds the occurrence of an input integer.
        for curr in range(1, max_element + shift + 1):
            # If line[curr] == 0, meaning there is no occurrence of the integer (curr - shift) 
            # held by this index, we will move on to the next index.
            if line[curr] == 0:
                continue
                
            # If the difference (curr - prev) equals `min_pair_diff`, we add this pair 
            # {prev - shift, curr - shift} to the answer list. 
            if curr - prev == min_pair_diff:
                answer.append([prev - shift, curr - shift])
            elif curr - prev < min_pair_diff:
                # If the difference (curr - prev) is smaller than `min_pair_diff`, 
                # we empty the answer list and add the pair {curr - shift, prev - shift} 
                # to the answer list and update the `min_pair_diff`
                answer = [[prev - shift, curr - shift]]
                min_pair_diff = curr - prev
            
            # Update prev as curr.     
            prev = curr
            
        return answer