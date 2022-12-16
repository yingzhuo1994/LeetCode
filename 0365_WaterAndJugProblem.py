# 1st solution, BFS
# O(n^2) time | O(n^2) space
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        elif jug2Capacity + jug2Capacity == targetCapacity:
            return True
        if jug1Capacity == jug2Capacity:
            return targetCapacity == jug1Capacity
        if jug1Capacity > jug2Capacity:
            jug1Capacity, jug2Capacity = jug2Capacity, jug1Capacity
        
        stack = deque([[0, 0]])
        visited = set([(0, 0)])
        while stack:
            x, y = stack.popleft()
            if x + y == targetCapacity:
                return True
            if x > 0 and (0, y) not in visited:
                stack.append([0, y])
                visited.add((0, y))
            if y > 0 and (x, 0) not in visited:
                stack.append([x, 0])
                visited.add((x, 0))
            if (jug1Capacity, y) not in visited:
                stack.append([jug1Capacity, y])
                visited.add((jug1Capacity, y))
            if (x, jug2Capacity) not in visited:
                stack.append([x, jug2Capacity])
                visited.add((x, jug2Capacity))
            if x + y > jug2Capacity:
                pair = (x + y - jug2Capacity, jug2Capacity)
            else:
                pair = (0, x + y)
            if pair not in visited:
                stack.append(pair)
                visited.add(pair)

            if x + y > jug1Capacity:
                pair = (jug1Capacity, x + y - jug1Capacity)
            else:
                pair = (x + y, 0)
            if pair not in visited:
                stack.append(pair)
                visited.add(pair)

        return False

# 2nd solution
# O(1) time | O(1) space
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        # Explanation: 
        # Key idea is that z litres is measurable using jugs of size x and y only if , z is a linear combination of x and y.
        # Reasoning for key idea : 
        # basically only options we have to solve the issue is - 
        # either pour water of amount x or y (which is positive multiplication constant on x or y) 
        # or a choice of emptying x or y (which is negative multiplication constant on x or y). 
        # hence for z to be measurable by x and y, z has to be 
        # z = sx+ly (where s and l are integer constants, we dont need to know s and l to solve our problem :))

        # So, in positive case where, z = kx + ly where k and l are constants, z is measurable. 
        # Now, if g is gcd of x and y, then z = kag + lbg where a and b are constants 
        # So, z = (ka+lb)g -> which suggests z must be divisible by g in order for z to be measurable by x and y. 
        # AND 
        # x + y must be equal or greater than z, otherwise we can fill up x and y both, but still they will sum up less than z. 
        # Hence, z won't be measurable if x + y < z
        # using that logic, we can say answer is:
        # return true if z % gcd(x, y) == 0 and x + y >= z
        
        def gcd(x, y):
            #Using Euclid's algorithm - https://en.wikipedia.org/wiki/Greatest_common_divisor
            if x < y : 
                x, y = y, x
            while x != y and y != 0 :
                remainder = x % y 
                x = y
                y = remainder
            return x
        x, y, z = jug1Capacity, jug2Capacity, targetCapacity
        g = gcd(x, y)
        #print("gcd: ", g)
        if g == 0:
            return z == 0
        
        return (x+y) >= z and z % g == 0 