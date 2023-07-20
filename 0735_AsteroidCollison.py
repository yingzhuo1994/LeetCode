# 1st solution
# O(n) time | O(n) space
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack or stack[-1] < 0 or asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and stack[-1] < -asteroid:
                    stack.pop()
                if stack:
                    if stack[-1] > 0:
                        if stack[-1] == - asteroid:
                            stack.pop()
                    else:
                        stack.append(asteroid)
                else:
                    stack.append(asteroid)
        return stack