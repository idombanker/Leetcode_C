class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []:
            return False
        a = [nums[0]]
        for index,i in enumerate(nums):
            if  len(a) == 1:
                if i <= a[0]:
                    a[0] = i
                else:
                    a.append(i)
            elif len(a) == 2:
                if i > a[1]:
                    return True
                    
                elif i <= a[1] and i > a[0]:
                    a[1] = i

                else:
                    a[0] = i
        return False
                        