def hammingDistance( x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = list(bin(x))[2:]
        y = list(bin(y))[2:]
        count = 0
        
        for i in range(0,min(len(x),len(y))-1):
            if x[len(x)-1-i]!=y[len(y)-1-i]:
                count+=1
        print(count)
        
        if min(len(x),len(y))==1:
            if x[-1]!=y[-1]:
                count+=1

        print (count)

        count=abs(len(x)-len(y))+count
        return count

print(hammingDistance(1,4))

