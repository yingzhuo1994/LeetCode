# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        books.append([0, 0])
        minHeights = [float("inf") for _ in range(n + 1)]
        minHeights[-1] = 0
        for i in range(n):
            maxHeight = 0
            curWidth = 0
            for j in reversed(range(i + 1)):
                curWidth += books[j][0]
                if curWidth <= shelfWidth:
                    maxHeight = max(maxHeight, books[j][1])
                    minHeights[i] = min(minHeights[i], minHeights[j - 1] + maxHeight)
                else:
                    break
        return minHeights[n-1]
