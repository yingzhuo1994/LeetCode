class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.fs = {}
        self.cs = defaultdict(list)
        for f, c, r in zip(foods, cuisines, ratings):
            self.fs[f] = [r, c]
            heappush(self.cs[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        f = self.fs[food]
        heappush(self.cs[f[1]], (-newRating, food))  # 直接添加新数据，后面 highestRated 再删除旧的
        f[0] = newRating

    def highestRated(self, cuisine: str) -> str:
        h = self.cs[cuisine]
        while -h[0][0] != self.fs[h[0][1]][0]:  # 堆顶的食物评分不等于其实际值
            heappop(h)
        return h[0][1]