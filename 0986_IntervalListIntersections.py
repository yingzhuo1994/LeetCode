# 1st solution
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        first, second = 0, 0
        result = []
        while first < len(firstList) and second < len(secondList):
            listOne = firstList[first]
            listTwo = secondList[second]
            if listOne[0] <= listTwo[0] <= listOne[1]:
                if listTwo[1] <= listOne[1]:
                    segment = [listTwo[0], listTwo[1]]
                    second += 1
                else:
                    segment = [listTwo[0], listOne[1]]
                    first += 1
                result.append(segment)
            elif listTwo[0] <= listOne[0] <= listTwo[1]:
                if listOne[1] <= listTwo[1]:
                    segment = [listOne[0], listOne[1]]
                    first += 1
                else:
                    segment = [listOne[0], listTwo[1]]
                    second += 1
                result.append(segment)
            elif listOne[0] >= listTwo[1]:
                second += 1
            elif listTwo[0] >= listOne[1]:
                first += 1
        return result

# 2nd solution
# O(m + n) time | O(m + n) space
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans