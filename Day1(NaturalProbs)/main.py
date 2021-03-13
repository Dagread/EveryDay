def seqsm(lng):                             #Sequence where we split the smallest one in 70% and 30%
   nums = [100]                             #Initialize array of probabilities, as you can see, now we have only 100%
   for i in range(lng-1):                   #Repeating operation bellow lng times
       num = nums[0]                        #Get the smallest one
       nums[0] = num/10*7                   #Replace it with 70% of what it was
       nums.append(num/10*3)                #Append array with 30% of what smallest one was
       nums = sorted(nums)[::-1]            #Sort it from smallest to biggest
   return(nums)                             #Return array

def seqbg(lng):                             #Sequence where we split the biggest one in 70% and 30%
   nums = [100]                             #Initialize array of probabilities, as you can see, now we have only 100%
   for i in range(lng-1):                   #Repeating operation bellow lng times
       num = nums[len(nums)-1]              #Get the biggest one
       nums[len(nums)-1] = num/10*7         #Replace it with 70% of what it was
       nums.append(num/10*3)                #Append array with 30% of what smallest one was
       nums = sorted(nums)[::-1]            #Sort it from smallest to biggest
   return(nums)                             #Return array

def seq(lng):                               #Sequence where we take average using functions above
   numbg = seqbg(lng)                       #Get sequence where we split biggest
   numsm = seqsm(lng)                       #Get sequence where we split smallest
   nums = [0]*lng                           #Inicialize array where we are going to store values
   for i in range(lng):                     #Cycle through every ellement in arrays
       nums[i] = (numbg[i] + numsm[i])/2    #Get average between first and second arrays
   return(sorted(nums)[::-1])               #Return complete array

def fastsq(lng):                            #The same thing as seq, but more efficient because we are fitting all in two arrays
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

print(fastsq(2))                            #Printing example