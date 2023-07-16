# 1st solution, TLE
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        new_people = []
        for i, skills in enumerate(people):
            new_skills = [skill for skill in skills if skill in req_skills ]
            if len(new_skills) > 0:
                new_people.append([i, new_skills])
        
        n = len(new_people)
        def dfs(idx, k, lst, dic):
            if idx >= n or k == 0:
                return all(dic.values())
            
            newDic = dic.copy()
            _, skills = new_people[idx]
            for skill in skills:
                newDic[skill] = True
            lst.append(idx)
            if dfs(idx + 1, k - 1, lst, newDic):
                return True
            lst.pop()
            if dfs(idx + 1, k, lst, dic):
                return True
            return False
            
        left = 1
        right = n
        ans = []
        while left <= right:
            mid = left + (right - left) // 2
            lst = []
            dic = {skill: False for skill in req_skills}
            if dfs(0, mid, lst, dic):
                ans = lst
                right = mid - 1
            else:
                left = mid + 1
        return [new_people[idx][0] for idx in ans]
        


