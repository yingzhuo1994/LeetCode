class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        count = Counter(queryIP)
        if "." in count:
            isPossIPv4 = True
        else:
            isPossIPv4 = False
        
        if ":" in count:
            isPossIPv6 = True
        else:
            isPossIPv6 = False

        if isPossIPv4 and isPossIPv6:
            return "Neither"
        elif isPossIPv4:
            nums = queryIP.split(".")
            if len(nums) != 4:
                return "Neither"
            for num in nums:
                if len(num) == 0:
                    return "Neither"
                if not all(ch.isdigit() for ch in num):
                    return "Neither"
                val = int(num)
                if len(str(val)) != len(num) or val > 255:
                    return "Neither"
            return "IPv4"
        elif isPossIPv6:
            nums = queryIP.split(":")
            if len(nums) != 8:
                return "Neither"
            for num in nums:
                if len(num) == 0 or len(num) > 4:
                    return "Neither"
                if not all(ch.isdigit() or ch.lower() in {"a", "b", "c", "d", "e", "f"} for ch in num):
                    return "Neither"
            return "IPv6"
        else:
            return "Neither"