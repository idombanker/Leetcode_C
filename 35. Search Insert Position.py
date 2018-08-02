class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        if target < nums[left]:
            return left
        if target > nums[right]:
            return right + 1
        counter = 0
        while(left < right):
            counter += 1
            print counter
            mid = (left + right)/2
            print "left:"
            print left
            print "right:"
            print right
            print "mid:"
            print mid
            print "\n"
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1 
        return mid

a = Solution()
print a.searchInsert([1,3,5,6],2)

