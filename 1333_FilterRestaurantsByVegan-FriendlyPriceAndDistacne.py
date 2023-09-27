# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        results = []
        for id, rating, isFriendly, price, distance in restaurants:
            if (not veganFriendly or isFriendly == veganFriendly) and price <= maxPrice and distance <= maxDistance:
                results.append([id, rating])
        results.sort(key = lambda v: [-v[1], -v[0]])
        return [result[0] for result in results]