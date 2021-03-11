def seqsm(lng):
   nums = [100]
   for i in range(lng-1):
       num = nums[0]
       nums[0] = num/10*7
       nums.append(num/10*3)
       nums = sorted(nums)[::-1]
   return(nums)

def seqbg(lng):
   nums = [100]
   for i in range(lng-1):
       num = nums[len(nums)-1]
       nums[len(nums)-1] = num/10*7
       nums.append(num/10*3)
       nums = sorted(nums)[::-1]
   return(nums)

def seq(lng):
   numbg = seqbg(lng)
   numsm = seqsm(lng)
   nums = [0]*lng
   for i in range(lng):
       nums[i] = (numbg[i] + numsm[i])/2
   return(sorted(nums)[::-1])

def fastsq(lng):
   nums = [0]*lng
   nums1, nums2 = [100], [100]
   for i in range(lng-1):
       num = nums2[len(nums2)-1]
       nums2[len(nums2)-1] = num/10*7
       nums2.append(num/10*3)
       nums2 = sorted(nums2)[::-1]
       num = nums1[0]
       nums1[0] = num/10*7
       nums1.append(num/10*3)
       nums1 = sorted(nums1)[::-1]
   for i in range(lng):
       nums[i] = (nums1[i] + nums2[i])/2
   return(sorted(nums)[::-1])

print(fastsq(2))