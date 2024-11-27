def calc_mean(nums):
    total = 0
    for i in nums:
        total = total + i
    return(total/len(nums))

def calc_median(nums):    
    # sort input
    nums.sort()
    # if even number, then find middle two positions
    if len(nums) % 2 == 0:
        upper = nums[int(len(nums)/2)]
        lower = nums[int((len(nums) - 2)/2)]
        # Calculate median
        median = (upper + lower)/2
    else:
        # Assuming list of odd length, take middle position as median
        median = nums[int((len(nums)-1)/2)]
    # Return output
    return(median)
    
