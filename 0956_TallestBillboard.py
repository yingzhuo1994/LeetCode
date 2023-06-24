# 1st solution, TLE
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:        
        rods.sort()
        total = sum(rods)
        half = total // 2
        # print(rods)
        # print(total, half)
        
        level = collections.defaultdict(list)
        level[0].append(0)
        for i, rod in enumerate(rods):
            newLevel = collections.defaultdict(list)
            for num, maskList in list(level.items()):
                value = num + rod
                if value > half:
                    continue
                # print(rod, num, value)
                for mask in maskList:
                    newMask = mask | (1 << i)
                    # print(bin(mask), bin(newMask))
                    newLevel[value].append(newMask)
            for key in newLevel:
                level[key].extend(newLevel[key])

        values = sorted(list(level.keys()))
        # for key in values:
        #     print(key, level[key])

        for value in reversed(values):
            maskList = level[value]
            # print(value, maskList)
            for i in range(len(maskList)):
                for j in range(i + 1, len(maskList)):
                    if (maskList[i] & maskList[j]) == 0:
                        # print([bin(mask) for mask in maskList])
                        # print(bin(maskList[i]))
                        # print(bin(maskList[j]))
                        # print(maskList[i] & maskList[j])
                        # s1 = bin(maskList[i])
                        # s2 = bin(maskList[j])
                        # lst1 = [rods[len(s1) - 1 - idx] for idx in range(2, len(s1)) if s1[idx] == '1']
                        # lst2 = [rods[len(s2) - 1 - idx] for idx in range(2, len(s2)) if s2[idx] == '1']
                        # print(lst1, sum(lst1))
                        # print(lst2, sum(lst2))
                        return value
        return 0

# 2nd solution
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:        
        dp = {0: 0}
        for rod in rods:
            for d, v in list(dp.items()):
                dp[d + rod] = max(dp.get(rod + d, 0), v)
                dp[abs(d - rod)] = max(dp.get(abs(d - rod), 0), v + min(d, rod))
        return dp[0]

# 3rd solution
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = dict()
        dp[0] = 0
        
        for rod in rods:
            cur = collections.defaultdict(int)
            for s in dp:
                cur[s+rod] = max(dp[s] + rod, cur[s+rod])
                cur[s] = max(dp[s], cur[s])
                cur[s-rod] = max(dp[s], cur[s-rod])
            dp = cur
        return dp[0]
