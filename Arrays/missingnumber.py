def MissingNumber(array,n):
        sumi = sum(array)
        target_sum = int(n*(n+1)/2)
        return target_sum - sumi

print(MissingNumber([1,2,4,5,6],6))