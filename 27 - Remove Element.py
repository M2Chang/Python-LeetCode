   def removeElement(nums, val):
        size = len(nums)
        
        count = 0 
        for i in range(size):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1 
        return count
        
        
