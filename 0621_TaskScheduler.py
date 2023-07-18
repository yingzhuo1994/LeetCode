# 1st solution
# O(k) time | O(1) space
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        Most_freq = freq.most_common()[0][1]
        Found_most = sum([freq[key] == Most_freq for key in freq])
        return max(len(tasks), (Most_freq - 1) * (n + 1) + Found_most)

# 2nd solution
# O(kn) time | O(1) space
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        curr_time, stack = 0, []
        for v in Counter(tasks).values():
            heappush(stack, -v)

        while stack:
            temp = []
            for _ in range(n + 1):
                curr_time += 1
                if stack:
                    x = heappop(stack)
                    if x != -1:
                        temp.append(x + 1)
                
                if not stack and not temp:
                    break

            for item in temp:
                heappush(stack, item)
        return curr_time