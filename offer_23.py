class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence: return False
        return self.helper(sequence)

    def helper(self, sequence):
        if len(sequence) <= 1: return True
        cur, count = sequence[-1], 0
        while count < len(sequence) - 1:
            if sequence[count] < cur: count += 1
            else: break
            
        for temp in range(count + 1, len(sequence) - 1):
            if sequence[temp] < cur:
                return False
        return self.helper(sequence[:count]) and self.helper(sequence[count:-1])

t = Solution()
print(t.VerifySquenceOfBST([5, 7, 6, 9, 11, 10, 8]))