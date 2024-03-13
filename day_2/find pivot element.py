class Solution(object):
    def pivotInteger(self, n):
        if n == 1:
            return 1  
        elif n == 2:
            return -1  
        a=[]
        for i in range(1,n+1):
            a.append(i)
        
        left_sum = a[0]
        total_sum = sum(a)
        
        for i in range(1, n):
            right_sum = total_sum - left_sum - a[i]
            
            if left_sum == right_sum:
                return i + 1
                
            left_sum += a[i]
        
        return -1
        
    
d=Solution()
n=8
res=d.pivotInteger(n)
print(res)
        
