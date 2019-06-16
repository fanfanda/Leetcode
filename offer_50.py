class Solution:
    def multiply(self, A):
        # write code here
        B = [1 for i in range(len(A))]
        for i in range(1,len(A)):
            B[i] = B[i-1]*A[i-1]
        temp = 1 
        for i in range(len(B)-2,-1,-1):
            temp *= A[i+1]
            B[i] *= temp
        return B