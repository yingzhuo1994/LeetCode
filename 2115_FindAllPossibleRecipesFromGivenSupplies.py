# 1st solution
# O(n) time | O(n) space
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {}
        graph_rev = {}
        for recipe, ingredient in zip(recipes, ingredients):
            if recipe not in graph:
                graph[recipe] = []
            for item in ingredient:
                graph[recipe].append(item)
                if item not in graph_rev:
                    graph_rev[item] = []
                graph_rev[item].append(recipe)
        level = supplies
        ans = []
        while level:
            newLevel = set()
            for item in level:
                if item in graph_rev:
                    for recipe in graph_rev[item]:
                        graph[recipe].remove(item)
                        if len(graph[recipe]) == 0:
                            newLevel.add(recipe)
            level = newLevel
            ans += list(level)
        return ans