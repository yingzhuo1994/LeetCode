# 1st solution
# O(n*log(n)) time | O(1) space
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # binary search over the length of substring
        # lo contains the valid value, and hi contains the
        # invalid value
        lo = 1
        hi = len(s) + 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            # can we make a valid substring of length `mid`?
            if self.__can_make_valid_substring(s, mid, k):
                # explore the right half
                lo = mid
            else:
                # explore the left half
                hi = mid

        # length of the longest substring that satisfies
        # the given condition
        return lo

    def __can_make_valid_substring(self, s: str, substring_length: int, k: int):
        # take a window of length `substring_length` on the given
        # string, and move it from left to right. If this window
        # satisfies the condition of a valid string, then we return
        # true
        freq_map = {}
        max_frequency = 0
        start = 0
        for end in range(len(s)):
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1

            # if the window [start, end] exceeds substring_length
            # then move the start pointer one step toward right
            if end + 1 - start > substring_length:
                # before moving the pointer toward right, decrease
                # the frequency of the corresponding character
                freq_map[s[start]] -= 1
                start += 1

            # record the maximum frequency seen so far
            max_frequency = max(max_frequency, freq_map[s[end]])
            if substring_length - max_frequency <= k:
                return True

        # we didn't get a valid substring of the given size
        return False

# 2nd solution
# O(26n) time | O(1) space
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        all_letters = set(s)
        max_length = 0

        # iterate over each unique letter
        for letter in all_letters:
            start = 0
            count = 0

            # initialize a sliding window for each unique letter
            for end in range(len(s)):
                if s[end] == letter:
                    # if the letter matches, increase the count
                    count += 1

                # bring start forward until the window is valid again
                while not self.__is_window_valid(start, end, count, k):
                    if s[start] == letter:
                        # if the letter matches, decrease the count
                        count -= 1
                    start += 1

                # at this point the window is valid, update max_length
                max_length = max(max_length, end + 1 - start)

        return max_length

    def __is_window_valid(self, start: int, end: int, count: int, k: int):
        return end + 1 - start - count <= k