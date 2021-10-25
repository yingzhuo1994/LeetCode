class Solution:
    # 1st solution
    # O(n) time | O(n) space
    # where n is the total number of the characters
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        result = []
        for k, v in frequency.items():
            result.append(k*v)
        result.sort(key = lambda string: -len(string))
        return "".join(result)


    # 2nd solution
    # O(n) time | O(n) space
    # where n is the total number of the characters
    def frequencySort(self, s: str) -> str:
        result = ''
        bucket = [None for i in range(len(s) + 1)]
        hash_map = Counter(s)
            
        for key, value in hash_map.items():
            if bucket[value] is None:
                bucket[value] = []
            
            bucket[value].append(key)
            
        for i in reversed(range(len(bucket))):
            if bucket[i] is not None:
                for char in bucket[i]:
                    result += char * i
                    
        return result