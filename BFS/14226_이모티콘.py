from collections import deque
#BFS는 정점과 간선이 무엇인지 정확히 정하고 가야한다.
# x= 화면 이모티콘 갯수, y=클립보드 이모티콘 갯수

max =2000
n = int(input())
arr=[[0]*max for _ in range(max)]


window = deque()
clip = deque()

window.append(1)
clip.append(0)

while window:
    x = window.popleft()
    y = clip.popleft()

    if x == n:
        print(arr[x][y])
        break
        #화면에 있는 이모티콘 복사
    if -1< y+x <max and arr[x][x] == 0:
        arr[x][x]= arr[x][y] +1
        window.append(x)
        clip.append(x)

        #클립보드에 있는 이모티콘을 화면에 복사
    if -1< x+y <max and arr[y+x][y] ==0:
        arr[y+x][y]= arr[x][y] +1
        window.append(x+y)
        clip.append(y)

        #화면 아이콘 하나 삭제
    if -1 < x-1 < max and arr[x-1][y] ==0 :
        arr[x-1][y]= arr[x][y] +1
        window.append(x-1)
        clip.append(y)



# for i in range(10):
#     print(' '.join(map(str, arr[i])))

