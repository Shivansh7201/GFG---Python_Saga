class Solution:

    def minValue(self, a, b, n):

        a.sort()

        b.sort(reverse=True)

        return sum( (a[i] * b[i]) for i in range(n))





