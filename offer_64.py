class Solution:
    def maxInWindows(self, num, size):
        # write code here
        maxqueue = []
        res = []
        n = len(num)
        if n == 0 or n < size or size == 0:
            return res
        for i in range(n):
            if maxqueue and i - size >= maxqueue[0]:
                # 判断队首元素是否已经在窗口之外了，如果是，队首元素出队
                maxqueue.pop(0)
            while maxqueue and num[i] >= num[maxqueue[-1]]:
            # 运行到这一步，队列里的元素，其对应的num中的数，都在这个滑动窗口里的
            # 因此，如果num后面的数比前面的数大，那么前边的数，就不可能在成为最大值了，
            # 因为窗口是往右移动的，只要在窗口的范围内，包含前面的数，就一定包含后面的数，
            # 但是包含后面的数，不一定包含前面的数。
            # 因此要将在队列中的，比num[i]小的num前面的数的下标出队。
            # 因为他不可能成为最大值了。
                maxqueue.pop()
            maxqueue.append(i)       
            # i入队，如果队列中存在的元素对应的数都比num[i]大，将i入队就行，
            # 因为当前边的元素都不在窗口内时，num[i]可能是窗口内元素的最大值。
            if maxqueue and i >= size - 1:
            # 因为窗口的长度是size，所以前size-1个元素不进行处理
                res.append(num[maxqueue[0]]) 
                # 因为上一个循环，队首元素对应的数一定是最大的。
                # 将队首对应的元素压入结果中，这一步元素不出队，
                # 因为队首元素不一定是窗口的左边界，下一次移动窗口，
                # 队首元素还可能在窗口中，而且是最大的。
        return res
