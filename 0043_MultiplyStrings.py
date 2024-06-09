# 1st solution
# O(m(m+n)) time | O(m + n) space
# where n and m are the number of elements in num1 and num2 strings.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = [0] * (len(num1) + len(num2))
        tenbit = 0
        for i in reversed(range(len(num2))):
            num = int(num2[i])
            curResult = self.multification(num, num1)
            for i in range(tenbit):
                curResult.append(0)
            self.addition(result, curResult[::-1])
            tenbit += 1 
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return "".join([str(result[i]) for i in reversed(range(len(result)))])
    
    def multification(self, num, s):
        result = [0] * (len(s) + 1)
        last = 0
        for i in reversed(range(len(s))):
            cur = num * int(s[i]) + last
            q = cur // 10
            r = cur % 10
            result[i + 1] = r
            last = q
        result[0] = last
        if last == 0:
            return result[1:]
        else:
            return result
        
    def addition(self, result, curResult):
        r = 0
        last = 0
        i = 0
        while i < len(result):
            a = curResult[i] if i < len(curResult) else 0
            b = result[i]
            curSum = a + b
            if curSum + last >= 10:
                r = 1
                curSum -= 10
            else:
                r = 0
            result[i] = curSum + last
            last = r
            i += 1
            
# 2nd solution
# O(m(m+n)) time | O(m + n) space
# where n and m are the number of elements in num1 and num2 strings.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": 
            return "0"
        
        # Reverse both numbers.
        first_number = num1[::-1]
        second_number = num2[::-1]
        
        # To store the multiplication result of each digit of secondNumber with firstNumber.
        N = len(first_number) + len(second_number)
        answer = [0] * N

        # Multiply each digit in second_number by the first_number
        # and add each result to answer
        for index, digit in enumerate(second_number):
            curResult = self.multiplyOneDigit(first_number, digit, index)
            answer = self.addStrings(curResult, answer)

        # Pop excess zero from the end of answer (if any).
        if answer[-1] == 0:
            answer.pop()

        # Ans is in the reversed order.
        # Reverse it to get the final answer.
        answer.reverse()
        return ''.join(str(digit) for digit in answer)
    
    def multiplyOneDigit(self, first_number: str, digit2: str, num_zeros: int):
        # Insert 0s at the beginning based on the current digit's place.
        currentResult = [0] * num_zeros
        carry = 0

        # Multiply firstNumber with the current digit of secondNumber.
        num = int(digit2)
        for digit1 in first_number:
            multiplication = int(digit1) * num + carry
            # Set carry equal to the tens place digit of multiplication.
            carry = multiplication // 10
            # Append the ones place digit of multiplication to the current result.
            currentResult.append(multiplication % 10)

        if carry != 0:
            currentResult.append(carry)
        return currentResult
    
    def addStrings(self, result: list, answer: list) -> list:
        carry = 0
        i = 0
        new_answer = []
        for digit1, digit2 in zip_longest(result, answer, fillvalue=0):
            # Add current digits of both numbers.
            curr_sum = digit1 + digit2 + carry
            carry = curr_sum // 10
            # Append last digit of curr_sum to the answer.
            new_answer.append(curr_sum % 10)
            i += 1

        return new_answer

# 3rd solution
# O(mn) time | O(m + n) space
# where n and m are the number of elements in num1 and num2 strings.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize answer as a string of zeros of length N.
        N = len(num1) + len(num2)
        answer = [0] * N
        
        # Reverse num1 and num2
        first_number = num1[::-1]
        second_number = num2[::-1]
        
        for place2, digit2 in enumerate(second_number):
            # For each digit in second_number multiply the digit by all digits in first_number.
            for place1, digit1 in enumerate(first_number):
                # The number of zeros from multiplying to digits depends on the place
                # of digit2 in second_number and the place of the digit1 in first_number.
                num_zeros = place1 + place2
                
                # The digit currently at position numZeros in the answer string
                # is carried over and summed with the current result.
                carry = answer[num_zeros]
                multiplication = int(digit1) * int(digit2) + carry
                
                # Set the ones place of the multiplication result.
                answer[num_zeros] = multiplication % 10
                
                # Carry the tens place of the multiplication result by 
                # adding it to the next position in the answer array.
                answer[num_zeros + 1] += multiplication // 10
        
        # Pop the excess 0 from the end of answer.
        if answer[-1] == 0:
            answer.pop()
            
        return ''.join(str(digit) for digit in reversed(answer))


# 4th solution
# O(mn) time | O(m + n) space
# where n and m are the number of elements in num1 and num2 strings.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        n = len(num1)
        m = len(num2)
        res = [0] * (n + m)
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                a = int(num1[i])
                b = int(num2[j])
                r = a * b + res[i + j + 1]
                res[i + j + 1] = r % 10
                res[i + j] += r // 10
        
        start = 1 if res[0] == 0 else 0
        
        return "".join(str(res[i]) for i in range(start, len(res)))