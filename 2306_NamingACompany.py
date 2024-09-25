# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        dic = defaultdict(set)
        for idea in ideas:
            dic[idea[1:]].add(idea[0])
        
        ans = 0
        keys = list(dic.keys())
        for i in range(len(keys)):
            for j in range(i):
                suffix1 = keys[i]
                suffix2 = keys[j]
                for ch1 in dic[suffix1]:
                    if ch1 in dic[suffix2]:
                        continue
                    for ch2 in dic[suffix2]:
                        if ch2 in dic[suffix1]:
                            continue
                        ans += 2
        return ans

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # Group idea by their initials.
        initial_groups = [set() for _ in range(26)]
        for idea in ideas:
            initial_groups[ord(idea[0]) - ord('a')].add(idea[1:])
        
        answer = 0
        # Calculate number of valid names from every pair of groups.
        for i in range(25):
            for j in range(i + 1, 26):
                # Get the number of mutual suffixes.
                num_of_mutual = len(initial_groups[i] & initial_groups[j]) 
                
                # Valid names are only from distinct suffixes in both groups.
                # Since we can swap a with b and swap b with a to create two valid names, multiple answer by 2.
                answer += 2 * (len(initial_groups[i]) - num_of_mutual) * (len(initial_groups[j]) - num_of_mutual)
                
        return answer

# 3rd solution
# O(n) time | O(n) space
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        size = [0] * 26  # 集合大小
        intersection = [[0] * 26 for _ in range(26)]  # 交集大小
        groups = defaultdict(list)  # 后缀 -> 首字母列表
        for s in ideas:
            b = ord(s[0]) - ord('a')
            size[b] += 1  # 增加集合大小
            g = groups[s[1:]]
            for a in g:  # a 是和 s 有着相同后缀的字符串的首字母
                intersection[a][b] += 1  # 增加交集大小
                intersection[b][a] += 1
            g.append(b)

        ans = 0
        for a in range(1, 26):  # 枚举所有组对
            for b in range(a):
                m = intersection[a][b]
                ans += (size[a] - m) * (size[b] - m)
        return ans * 2  # 乘 2 放到最后