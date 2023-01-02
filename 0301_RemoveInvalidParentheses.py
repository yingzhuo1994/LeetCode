# 1st solution
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        array = list(s)
        leftCount = 0
        rightCount = 0
        for ch in array:
            if ch == "(":
                leftCount += 1
            elif ch == ")":
                rightCount += 1
        minCost = abs(leftCount - rightCount)
        maxCost = leftCount + rightCount

        def isPossible(array, cost):
            leftCount = 0
            for ch in array:
                if ch == "(":
                    leftCount += 1
                elif ch == ")":
                    if leftCount == 0:
                        cost -= 1
                    else:
                        leftCount -= 1
            if cost >= leftCount:
                return True
            return False

        while minCost < maxCost:
            cost = minCost + (maxCost - minCost) // 2
            if isPossible(array, cost):
                maxCost = cost
            else:
                minCost = cost + 1
        print(minCost)
        results = []
        def formulateArray(idx, cost, lst, leftCount=0):
            if cost < 0:
                return
            if idx == len(array):
                # print(lst, cost, leftCount)
                if cost == 0 and leftCount == 0:
                    results.append(lst[:])
                elif cost == leftCount and lst[-cost:] == ["(" for _ in range(cost)]:
                    results.append(lst[:len(lst)-leftCount])
                return
            if array[idx] == "(":
                formulateArray(idx + 1, cost, lst + ["("], leftCount + 1)
                # if len(lst) > 0 and array[idx] != lst[-1]:
                formulateArray(idx + 1, cost - 1, lst, leftCount)
            elif array[idx] == ")":
                if leftCount > 0:
                    formulateArray(idx + 1, cost, lst + [")"], leftCount - 1)
                    # if len(lst) > 0 and array[idx] != lst[-1]:
                    formulateArray(idx + 1, cost - 1, lst, leftCount)
                else:
                    formulateArray(idx + 1, cost - 1, lst, leftCount)
            else:
                formulateArray(idx + 1, cost, lst + [array[idx]], leftCount)
        
        formulateArray(0, minCost, [])
        results = ["".join(lst) for lst in results]
        results = list(set(results))
        return results