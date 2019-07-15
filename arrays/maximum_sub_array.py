import math
def max_crossing_array(arr,low,mid,high):
    left_sum=-math.inf
    sum=0
    max_left=None
    i=mid
    while i>=low:
        sum+=arr[i]
        if sum>=left_sum:
            left_sum=sum
            max_left=i
        i-=1
    right_sum=-math.inf
    max_right=None
    sum=0
    for i in range(mid+1,high+1):
        sum+=arr[i]
        if sum>=right_sum:
            right_sum=sum
            max_right=i
    max_sum=left_sum+right_sum
    return (max_left,max_right,max_sum)
def max_sub_array(arr,low,high):
    if low==high:
        return (low,high,arr[low])
    else:
        mid=math.floor((low+high) / 2)
        left_low,left_high,left_sum=max_sub_array(arr,low,mid)
        right_low,right_high,right_sum=max_sub_array(arr,mid+1,high)
        cross_low,cross_high,cross_sum=max_crossing_array(arr,low,mid,high)
        if left_sum>=right_sum and left_sum>=cross_sum :
            return (left_low,left_high,left_sum)
        elif right_sum>=left_sum and right_sum>=cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)
print(max_sub_array([1, 2, 3, -4, 6],0,4))
