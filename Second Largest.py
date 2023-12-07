class Solution:
    def print2largest(self,a, n):
        a.sort(reverse=True)
        M = a[0]
        for i in range(n):
            if a[i] != M :
                return a[i]
        return -1
