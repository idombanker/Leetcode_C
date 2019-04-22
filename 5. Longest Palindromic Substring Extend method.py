class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        longest common substring of the strings
        
        Expand Around Center
        
        palindrome mirrors around its center.
        a palindrome can be expanded from its center
        there are 2n -1 such centers.
        
        
        时间复杂度是n^2 空间复杂度是1
        
        
        
        """
        s = list(s)
        n = len(s)
        
        # 需要区分子序列长度是奇数还是偶数的情况，
        # 偶数的话even，中心点定位i 和i－1
        # 奇数的话odd，中心店定为i 
        
        # 最外层的循环，遍历序列的每个元素，然后在每一次循环考察两种中心的情况
        # 需要设置一个low 和 high　来作为第二层遍历的指针
        # 同样需要设置一个maxLength = high - low + 1 来记录长度
        # 一个start来记录返回的target
        
        # 注意：maxLength 要设置为１，否则不能返回长度为１的子序列
        maxLength = 1
        start = 0
        for i in xrange(1,n):
            # 从１开始，因为偶数序列中心设置为i 和i － 1
            #　俩中心情况：
            low = i -1
            high = i
            while low >= 0 and high < n and s[low]==s[high]:
                
                if high - low + 1 > maxLength:
                    maxLength = high - low + 1
                    start = low
            
                low -= 1
                high += 1
            
            low = i - 1
            high = i + 1
            
            while low >= 0 and high < n and s[low] == s[high]:
                
                if high - low + 1 > maxLength:
                    maxLength = high - low + 1
                    start = low
                low -= 1
                high += 1
            
        
            
              
        target = s[start:maxLength+start]

        if len(target)>0:
            target = ''.join(target)
        else:
            target = ""  
        return target
        
        
