class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        nodes = [Node(card) for card in cards]

        def calculation(array):
            if len(array) == 1:
                return array
            
            ans = []
            for i in range(1, len(array)):
                for first in calculation(array[:i]):
                    for second in calculation(array[i:]):
                        # print(first, second)
                        ans.extend(first.operations(second))
            if len(array) == 4:
                for middle in calculation(array[1:3]):
                    ans.extend(calculation([array[0], middle, array[-1]]))

            return ans
        
        array = self.getPermuation(nodes)
        for lst in array:
            values = calculation(lst)
            for node in values:
                if node.getValue() == 24:
                    return True

        return False
    
    def getPermuation(self, array):
        if len(array) == 1:
            return [array]
        ans = []
        for i in range(len(array)):
            ans.extend([[array[i]] + lst for lst in self.getPermuation(array[:i] + array[i+1:])])
        return ans


class Node:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
    
    def __repr__(self):
        return f"<{self.numerator}, {self.denominator}>"

    def times(self, other):
        return Node(self.numerator * other.numerator, self.denominator * other.denominator)

    def devide(self, other):
        return Node(self.numerator * other.denominator, self.denominator * other.numerator)

    def plus(self, other):
        return Node(self.numerator * other.denominator + self.denominator * other.numerator, self.denominator * other.denominator)

    def minus(self, other):
        return Node(self.numerator * other.denominator - self.denominator * other.numerator, self.denominator * other.denominator)
    
    def operations(self, other):
        return [self.times(other), self.devide(other), self.plus(other), self.minus(other)] 
    
    def getValue(self):
        if self.denominator == 0:
            return float("inf")
        return self.numerator / self.denominator
