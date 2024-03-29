# 1st solution, Max Heap
# O(n*log(k)) time | O(k) space
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for x, y in points:
            dist = x**2 + y**2
            heappush(hp, [-dist, [x, y]])
            if len(hp) > k:
                heappop(hp)
        return [elem[1] for elem in hp]

# 2nd solution, Binary Search, image there is a circle boundary which contains the k closest points
# O(n) time | O(n) space
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Precompute the Euclidean distance for each point
        distances = [self.euclidean_distance(point) for point in points]
        # Create a reference list of point indices
        remaining = [i for i in range(len(points))]
        # Define the initial binary search range
        low, high = 0, max(distances)
        
        # Perform a binary search of the distances
        # to find the k closest points
        closest = []
        while k:
            mid = low + (high - low) / 2
            closer, farther = self.split_distances(remaining, distances, mid)
            if len(closer) > k:
                # If more than k points are in the closer distances
                # then discard the farther points and continue
                remaining = closer
                high = mid
            else:
                # Add the closer points to the answer array and keep
                # searching the farther distances for the remaining points
                k -= len(closer)
                closest.extend(closer)
                remaining = farther
                low = mid
                
        # Return the k closest points using the reference indices
        return [points[i] for i in closest]

    def split_distances(self, remaining: List[int], distances: List[float],
                        mid: int) -> List[List[int]]:
        """Split the distances around the midpoint
        and return them in separate lists."""
        closer, farther = [], []
        for index in remaining:
            if distances[index] <= mid:
                closer.append(index)
            else:
                farther.append(index)
        return [closer, farther]

    def euclidean_distance(self, point: List[int]) -> float:
        """Calculate and return the Euclidean distance."""
        return sqrt(point[0] ** 2 + point[1] ** 2)

# 3rd solution, QuickSelect
# O(n) time | O(n) space
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quick_select(points, k)
    
    def quick_select(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Perform the QuickSelect algorithm on the list"""
        left, right = 0, len(points) - 1
        pivot_index = len(points)
        while pivot_index != k:
            # Repeatedly partition the list
            # while narrowing in on the kth element
            pivot_index = self.partition(points, left, right)
            if pivot_index < k:
                left = pivot_index
            else:
                right = pivot_index - 1
        
        # Return the first k elements of the partially sorted list
        return points[:k]
    
    def partition(self, points: List[List[int]], left: int, right: int) -> int:
        """Partition the list around the pivot value"""
        pivot = self.choose_pivot(points, left, right)
        pivot_dist = self.squared_distance(pivot)
        while left < right:
            # Iterate through the range and swap elements to make sure
            # that all points closer than the pivot are to the left
            if self.squared_distance(points[left]) >= pivot_dist:
                points[left], points[right] = points[right], points[left]
                right -= 1
            else:
                left += 1
        
        # Ensure the left pointer is just past the end of
        # the left range then return it as the new pivotIndex
        if self.squared_distance(points[left]) < pivot_dist:
            left += 1
        return left
    
    def choose_pivot(self, points: List[List[int]], left: int, right: int) -> List[int]:
        """Choose a pivot element of the list"""
        return points[left + (right - left) // 2]
    
    def squared_distance(self, point: List[int]) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2

# 4th soltuion, Binary Seach + Quick Select
# O(n) time | O(n) space
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [self.getDistance(point) for point in points]

        low, high = 0, max(distance)
        L, R = 0, len(points) - 1
        while low < high:
            mid = low + (high - low) // 2
            left, right = L, R
            while left <= right:
                if distance[left] <= mid:
                    left += 1
                else:
                    self.swap(distance, left, right)
                    self.swap(points, left, right)
                    right -= 1
            if left < k :
                low = mid + 1
                L = left
            elif left > k :
                high = mid
                R = left
            else:
                break
              
        return points[:k]
                   
    
    def swap(self, arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]
    
    def getDistance(self, point):
        x, y = point[0], point[1]
        return x**2 + y**2

# 5th solution, recursive quick-selection
# O(n) time | O(n) space
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [self.getDistance(point) for point in points]
        self.quickSelect(distances, points, 0, len(points) - 1, k)
        return points[:k]
            
    
    def getDistance(self, point):
        x, y = point[0], point[1]
        return x**2 + y**2
    
    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]
    
    def quickSelect(self, distances, points, left, right, k):
        pivot = distances[left]
        L, R = left, right
        idx = L
        while idx <= R:
            if distances[idx] < pivot:
                self.swap(distances, idx, L)
                self.swap(points, idx, L)
                idx += 1
                L += 1
            elif distances[idx] > pivot:
                self.swap(distances, idx, R)
                self.swap(points, idx, R)
                R -= 1
            else:
                idx += 1
        if k <= L:
            self.quickSelect(distances, points, left, L - 1, k)
        elif k > idx:
            self.quickSelect(distances, points, idx, right, k)
        else:
            return