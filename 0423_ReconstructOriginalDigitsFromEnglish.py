# 1st solution
# O(n) time | O(n) space
class Solution:
    def originalDigits(self, s: str) -> str:
        lst = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        count = Counter(s)
        numbers = [0 for _ in range(10)]
        sequences = [["z", 0], ["x", 6], ["g", 8],["w", 2], ["t", 3], ["r", 4], ["f", 5], ["s", 7], ["i", 9], ["o", 1]]
        for ch, number in sequences:
            numbers[number] = self.count_one_number(count, ch, number, lst)
        ans = [str(i) * numbers[i] for i in range(10)]
        return "".join(ans)
    
    def count_one_number(self, count, key_ch, number, lst):
        n = 0
        if count[key_ch] > 0:
            n = count[key_ch]
            ch_count = Counter(lst[number])
            for ch in ch_count:
                count[ch] -= ch_count[ch] * n
        return n