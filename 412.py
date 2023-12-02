class Solution(object):
    def fizzBuzz(self, n):
        ans=[]
        for i in range(1,n+1):
            k=''
            if i%3==0:
                k=k+"Fizz"
            if i%5==0:
                k=k+"Buzz"
            if k=='':
                ans.append(str(i))
            if k!="":
                ans.append(k)
        return ans