# 1st solution, TLE
# O(n^2) time | O(1) space
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        n = len(properties)
        visited = set()
        for i in range(n):
            for j in range(i + 1, n):
                if i not in visited and all(properties[i][k] < properties[j][k] for k in range(2)):
                    visited.add(i)
                if j not in visited and all(properties[i][k] > properties[j][k] for k in range(2)):
                    visited.add(j)
        return len(visited)

# 2nd solution
# O(nlog(n)) time | O(n) space
from collections import defaultdict
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        attackDic = defaultdict(list)
        for attack, defense in properties:
            attackDic[attack].append(defense)
        
        attackArray = sorted(attackDic.keys())
        count = 0
        for attack in attackArray:
            attackDic[attack].sort()
            
        maxDefense = attackDic[attackArray[-1]][-1]
        for i in reversed(range(0, len(attackArray) - 1)):
            attack = attackArray[i]
            count += bisect.bisect_left(attackDic[attack], maxDefense)
            maxDefense = max(maxDefense, attackDic[attack][-1])

        return count


# 2nd solution
# O(nlog(n)) time | O(n) space
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        
        stack = []
        ans = 0
        
        for attack, defense in properties:
            while stack and stack[-1] < defense:
                stack.pop()
                ans += 1
            stack.append(defense)

        return ans