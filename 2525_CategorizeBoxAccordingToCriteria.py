class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        dimension = [length, width, height]
        if max(dimension) >= 10000 or length * width * height >= 10**9:
            bulky = True
        else:
            bulky = False
        
        heavy = mass >= 100

        if bulky and heavy:
            return "Both"
        elif bulky:
            return "Bulky"
        elif heavy:
            return "Heavy"
        else:
            return "Neither"