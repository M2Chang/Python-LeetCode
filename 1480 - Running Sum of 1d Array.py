def runningSum(nums):
    
        size = len(nums)
        sumhold = 0
        sumlist = []
        
        for i in range(size):
            sumhold += nums[i]
            
            sumlist.append(sumhold)
            
        return sumlist
