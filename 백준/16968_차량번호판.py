n = input()

c = 26
d = 10
length= len(n)
cal= [0]*length
for i in range(length):
    if n[i] == "c":
        if i != 0:
            if n[i-1] == "c":
                cal[i] = c -1
            else:
                cal[i] = c
        else:
            cal[i] = c
    else:
        if i != 0:
            if n[i-1] == "d":
                cal[i] = d -1
            else:
                cal[i] = d
        else:
            cal[i] = d

result=1
for i in range(length):
    result *= cal[i]

print(result)