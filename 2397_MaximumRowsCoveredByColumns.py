class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = len(matrix), len(matrix[0])
        if numSelect == n:
            return m
        ans = 0
        rows = []
        extra = 0
        for i in range(m):
            val = 0
            for j in range(n):
                if matrix[i][j] == 1:
                    val |= 1 << j
            if val == 0:
                extra += 1
            else:
                rows.append(val)

        left = n - numSelect
        def getMask(k, n):
            print(k, n)
            if k == n:
                return [(1 << k) - 1]
            if k > n or k < 1 or n < 1:
                return [0]
            masks = []
            for i in range(n - k + 1):
                mask = [(1 << (n - 1 - i)) | val for val in getMask(k - 1, n - 1 - i)]
                masks.extend(mask)

            return masks

        for mask in getMask(left, n):
            count = 0
            for row in rows:
                if mask & row:
                    continue
                count += 1
            ans = max(ans, count)
        return ans + extra
