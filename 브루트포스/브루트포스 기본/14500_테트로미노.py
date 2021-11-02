n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

ans=0
for i in range (n):
    for j in range (m):
        #일자막대기
        if j+3<m:
            temp= a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i][j+3]
            if ans < temp:
                ans = temp
        if i+3<n:
            temp =a[i][j] + a[i+1][j] + a[i+2][j] + a[i+3][j]
            if ans < temp:
                ans = temp
        #정사각형
        if j+1<m and i+2<n:
            temp =a[i][j]+a[i][j+1]+a[i+1][j]+a[i+1][j+1]
            if ans < temp:
                ans = temp

        #니은모양
        if j+1<m and i+2<n:
            temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j+1]
            if ans < temp:
                ans = temp
        if j+1<m and i+2<n:
            temp = a[i][j+1] + a[i+1][j+1] + a[i+2][j+1] + a[i+2][j]
            if ans < temp:
                ans = temp
        #기역모양
        if j+1<m and i+2<n:
            temp = a[i][j+1] + a[i][j] + a[i+1][j] + a[i+2][j]
            if ans < temp:
                ans = temp
        if j+1<m and i+2<n:
            temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+2][j+1]
            if ans < temp:
                ans = temp
        #누운 니은
        if j+2<m and i+1<n:
            temp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+1][j+2]
            if ans < temp:
                ans = temp
        if j + 2 < m and i + 1 < n:
            temp = a[i+1][j] + a[i+1][j+1] + a[i+1][j+2] + a[i][j+2]
            if ans < temp:
                ans = temp
        # 누운 기역
        if j + 2 < m and i + 1 < n:
            temp = a[i+1][j] + a[i][j] + a[i][j+1] + a[i][j+2]
            if ans < temp:
                ans = temp
        if j + 2 < m and i + 1 < n:
            temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+2]
            if ans < temp:
                ans = temp

        #가운데 가로 위
        if j + 2 < m and i + 1 < n:
            temp = a[i+1][j] + a[i+1][j+1] + a[i][j+1] + a[i+1][j+2]
            if ans < temp:
                ans = temp
        if j + 2 < m and i + 1 < n:
            temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i][j+2]
            if ans < temp:
                ans = temp

        #가운데 세로 위
        if j + 1<m and i + 2<n:
            temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+1][j+1]
            if ans < temp:
                ans = temp
        if j + 1<m and i + 2<n:
            temp = a[i][j+1] + a[i+1][j+1] + a[i+1][j] + a[i+2][j+1]
            if ans < temp:
                ans = temp

        #세운 물결
        if j + 1<m and i + 2<n:
            temp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+2][j+1]
            if ans < temp:
                ans = temp
        if j + 1 < m and i + 2 < n:
            temp = a[i][j+1] + a[i+1][j+1] + a[i+1][j] + a[i+2][j]
            if ans < temp:
                ans = temp

        #누운 니은
        if j+2<m and i+1<n:
            temp = a[i+1][j] + a[i+1][j+1] + a[i][j+1] + a[i][j+2]
            if ans < temp:
                ans = temp
        if j + 2 < m and i + 1 < n:
            temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+1][j+2]
            if ans < temp:
                ans = temp

print(ans)