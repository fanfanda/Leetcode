from collections import defaultdict
class Solution:
    def __init__(self):
        self.allstring = defaultdict(int)
        self.ch = []
    def FirstAppearingOnce(self):
        if self.allstring is None:
            return '#'
        for i in self.ch:
            if self.allstring[i] == 1:
                return i 
        return '#'
    def Insert(self, char):
        self.ch.append(char)
        self.allstring[char] += 1