class Solution:
    # 1st solution
    # O(nlogn) time | O(n) space
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
    
    # 2nd solution
    # O(n) time | O(1) space
    def wiggleSort(self, nums: List[int]) -> None:
        def nsmallest(nums,n):            
            start,end=0,len(nums)-1
            while True:
                pivot=nums[random.randint(start,end)]
                i,j,k=start,end,start
                while k<=j:
                    if nums[k]<pivot:
                        nums[i],nums[k]=nums[k],nums[i]
                        i+=1
                        k+=1
                    elif nums[k]>pivot:
                        nums[j],nums[k]=nums[k],nums[j]
                        j-=1
                    else:
                        k+=1
                if i<=n-1<=j:
                    return pivot
                elif n-1<i:
                    end=i-1
                else:
                    start=i+1
        n=len(nums)
        mid=nsmallest(nums,(n+1)//2)
        mapIdx=lambda i:(1+2*i)%(n|1)
        i,j,k=0,n-1,0
        while k<=j:
            if nums[mapIdx(k)]>mid:
                nums[mapIdx(k)],nums[mapIdx(i)]=nums[mapIdx(i)],nums[mapIdx(k)]
                i+=1
                k+=1
            elif nums[mapIdx(k)]<mid:
                nums[mapIdx(k)],nums[mapIdx(j)]=nums[mapIdx(j)],nums[mapIdx(k)]
                j-=1
            else:
                k+=1