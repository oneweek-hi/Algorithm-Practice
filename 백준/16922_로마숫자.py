n = int(input())
unique = set([])

for i in range(n+1):
    for j in range(n+1-i):
        for k in range(n+1-i-j):
            unique.add(1*i+5*j+10*k+50*(n-i-j-k))

print(len(unique))