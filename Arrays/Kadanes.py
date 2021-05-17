def maxSubArraySum(a,size):
        curr_max = a[0]
        maxsofar = a[0]
        
        for i in range(1,size):
            curr_max = max(a[i], curr_max + a[i])
            maxsofar = max(curr_max, maxsofar)
        return maxsofar

print(maxSubArraySum([1,3,4,5,2,7,-4,-8,3,4],10))