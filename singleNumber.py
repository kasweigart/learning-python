# List operation solution
#
class Solution:
    def singleNumber(self, nums):
        no_dupe_list = []
        for i in nums:
            if i not in no_dupe_list:
                no_dupe_list.append(i)
            else:
                no_dupe_list.remove(i)
        return no_dupe_list.pop()

# Bit manipulation
#
class SolutionB:
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result ^= i
        return result