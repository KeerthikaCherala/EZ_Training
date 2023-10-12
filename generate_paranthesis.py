def generate(n):
    res=[]
    def backtrack(s,opencount=0,closecount=0):
        if n==opencount==closecount:
            res.append(s)
        if opencount<n:
            backtrack(s+'(',opencount+1,closecount)
        if closecount<opencount:
            backtrack(s+')',opencount,closecount+1)
        return res
    return backtrack(s=" ")
n=int(input())
res=generate(n)
print(res)
