class Solution:
    def fizzBuzz(self, n):
        ans = []

        for num in range(1, n + 1):

            divis_3 = num % 3 == 0
            divis_5 = num % 5 == 0
            
            if divis_3 and divis_5:
                ans.append("FizzBuzz")
            elif divis_3:
                ans.append("Fizz")
            elif divis_5:
                ans.append("Buzz")
            else:
                ans.append(str(num))

        return ans

