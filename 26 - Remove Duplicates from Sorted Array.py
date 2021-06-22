def removeDuplicates(nums):
  size = len(nums)
        
  count = 0
  for i in range(1,size):
    if nums[i] != nums[count]:
      nums[count + 1] = nums[i]
      count +=1
      print(nums)
    return count + 1
     
    
nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)
