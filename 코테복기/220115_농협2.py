from collections import defaultdict

arr=[(1,4),(1,4),(3,4),(3,4),(4,2),(4,2),(1,5)]
dict = defaultdict(int)
for a in arr:
    print(a)
    if a in dict:
        dict[a] +=1
    else:
        dict[a]=1

count=0
print(dict)
for a in dict.values():
    if a>1:
        count+= a-1

print(count)