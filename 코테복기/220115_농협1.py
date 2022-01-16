n=input()

num=[0,9,8,7,6,5,4,3,2,1]
abc=['a','b','c','d','e','f','g','h','i','j','k','l',
   'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

result=''
for i in range(len(n)):
    if 'a' <= n[i] <= 'z':
        for j in range(len(abc)):
            if n[i] == abc[j]:
                result += str(abc[26-j-1])

    elif 'A' <= n[i] <= 'Z':
        for j in range(len(abc)):
            if n[i].lower() == abc[j]:
                result += str(abc[(j+1)%26].upper())

    else:
        result += str(num[int(n[i])])

print(result)




