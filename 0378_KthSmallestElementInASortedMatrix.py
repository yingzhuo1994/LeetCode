# 1st solution
# O(Nlog(N)) time | O(N) space
# where N is the total number of the elements
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst = []
        for line in matrix:
            lst.extend(line)
        lst.sort()
        return lst[k - 1]

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # The median-of-medians selection function.
        def pick(a, k):
            if k == 1:
                return min(a)
            groups = (a[i:i+5] for i in range(0, len(a), 5))
            medians = [sorted(group)[len(group) // 2] for group in groups]
            pivot = pick(medians, len(medians) // 2 + 1)
            smaller = [x for x in a if x < pivot]
            if k <= len(smaller):
                return pick(smaller, k)
            k -= len(smaller) + a.count(pivot)
            return pivot if k < 1 else pick([x for x in a if x > pivot], k)

        # Find the k1-th and k2th smallest entries in the submatrix.
        def biselect(index, k1, k2):

            # Provide the submatrix.
            n = len(index)
            def A(i, j):
                return matrix[index[i]][index[j]]
            
            # Base case.
            if n <= 2:
                nums = sorted(A(i, j) for i in range(n) for j in range(n))
                return nums[k1-1], nums[k2-1]

            # Solve the subproblem.
            index_ = list(index[::2]) + list(index[n-1+n%2:])
            k1_ = (k1 + 2*n) // 4 + 1 if n % 2 else n + 1 + (k1 + 3) // 4
            k2_ = (k2 + 3) // 4
            a, b = biselect(index_, k1_, k2_)

            # Prepare ra_less, rb_more and L with saddleback search variants.
            ra_less = rb_more = 0
            L = []
            jb = n   # jb is the first where A(i, jb) is larger than b.
            ja = n   # ja is the first where A(i, ja) is larger than or equal to a.
            for i in range(n):
                while jb and A(i, jb - 1) > b:
                    jb -= 1
                while ja and A(i, ja - 1) >= a:
                    ja -= 1
                ra_less += ja
                rb_more += n - jb
                L.extend(A(i, j) for j in range(jb, ja))
                
            # Compute and return x and y.
            x = a if ra_less <= k1 - 1 else \
                b if k1 + rb_more - n*n <= 0 else \
                pick(L, k1 + rb_more - n*n)
            y = a if ra_less <= k2 - 1 else \
                b if k2 + rb_more - n*n <= 0 else \
                pick(L, k2 + rb_more - n*n)
            return x, y

        # Set up and run the search.
        n = len(matrix)
        start = max(k - n*n + n-1, 0)
        k -= n*n - (n - start)**2
        return biselect(range(start, min(n, start+k)), k, k)[0]

# 3rd solution
# O(nlog(A)) time | O(n) space
# where A is the difference between the maximum and minimum in the matrix.
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def enough(value):
            count = 0
            for row in matrix:
                idx = bisect.bisect_right(row, value)
                count += idx
            return count < k
        
        smallest = matrix[0][0]
        largest = matrix[-1][-1]
        
        ans = smallest
        while smallest <= largest:
            value = smallest + (largest - smallest) // 2
            if enough(value):
                smallest = value + 1
            else:
                ans = value
                largest = value - 1
        return ans