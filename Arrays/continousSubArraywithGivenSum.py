def subArraySum(arr, n, s): 

    for i in range(n):
        curr_sum  = arr[i]
        j = i + 1
        while j <= n:

            if curr_sum == s:
                return [i+1,j]
        
            if curr_sum > s or j == n:
                break

            curr_sum = curr_sum + arr[j]

            j+=1

    return [-1]

