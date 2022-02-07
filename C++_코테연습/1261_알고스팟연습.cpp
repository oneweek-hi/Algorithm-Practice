#include <iostream>
#include <deque>

using namespace std;
int miro[101][101];
int visit[101][101];
int dx[]={0,0,-1,1};
int dy[] ={-1,1,0,0};

int main(){
  int n,m;
  cin >> n >> m;
  for(int i=0; i<n;i++){
    string a;
    cin >> a;
    for(int j=0; j<n; j++){
      miro[i][j]= a[j]-'0';
      visit[i][j]=-1;
    }
  }

  deque<pair<int,int>> q;
  q.push_back(make_pair(0,0));
  visit[0][0]=0;
  while(!q.empty()){
    int x = q.front().first;
    int y = q.front().second;
    q.pop_front();
    for (int k=0; k<4; k++){
      int nx = x+dx[k];
      int ny = y+dy[k];
      if (0 <= nx && nx<n && 0 <= ny && ny<m){
        if (visit[nx][nx] == -1){
          if (miro[nx][ny] == 0){
            visit[nx][ny]=visit[x][y];
            q.push_front(make_pair(nx,ny));
          }else{
            visit[nx][ny]=visit[x][y]+1;
            q.push_back(make_pair(nx,ny));
          }
        }
      }
    }
  }

  cout << visit[n-1][m-1]<<endl;
  

  // for(int i=0; i<n;i++){
  //   for(int j=0; j<n; j++){
  //     cout<< miro[i][j] << " ";
  //   }
  //   cout<< "\n";
  // }




}