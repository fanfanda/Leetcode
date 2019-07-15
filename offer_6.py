# class Solution:
#     def minNumberInRotateArray(self, rotateArray):
#         '''在旋转数组中查找最小值'''
#         n = len(rotateArray)
#         if n <= 2: return min(rotateArray)
#         if not n: return 0
#         mid = n // 2
#         if rotateArray[mid] < rotateArray[n - 1]: return self.minNumberInRotateArray(rotateArray[:mid + 1])
#         else: return self.minNumberInRotateArray(rotateArray[mid + 1:])

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0: return 0

        mid = len(rotateArray)//2
        if rotateArray[0] > rotateArray[mid]:
            return self.minNumberInRotateArray(rotateArray[1:mid + 1])
        elif rotateArray[mid] > rotateArray[-1]:
            return self.minNumberInRotateArray(rotateArray[mid:])
        else:
            return rotateArray[0]
array = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
t = Solution()
print(t.minNumberInRotateArray(array))