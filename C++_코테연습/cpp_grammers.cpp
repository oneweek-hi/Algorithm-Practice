#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <cmath>


using namespace std;
int main(){

  // 벡터 선언
  vector<int> v1(7, 0); //v1(벡터크기, 초기값)
  vector<vector<int>> v2(7, vector<int>(5, 0)); //v2(벡터크기, vector<타입>(벡터크기, 값))

  // 문자열 정수 변환 - stoi, stol, to_string  #include <string>
  string s1 = "100";
  int n1 = stoi(s1, nullptr, 2);  // x=stoi(문자열변수명, nullptr, 2/10/16 등 진수);
  s1 = to_string(n1);

  // 문자열 역정렬 - reverse
  reverse(s1.begin(), s1.end());
  cout << s1 <<endl;

  // 특정 값으로 벡터 채우기 - fill, 직접선언
  fill(v1.begin(), v1.end(), 10);
  v1 = {3,5,7};

  // 벡터 최댓값 최솟값 - max_element, min_element
  cout << *max_element(v1.begin(), v1.end()) << endl; // iterator 변수형으로 반환하므로 * 붙여 값 얻음
  cout << *min_element(v1.begin(), v1.end()) << endl;

  // 벡터에서 특정 값 찾기, 존재여부 - find iterator 값으로 반환
  auto it = find(v1.begin(), v1.end(), 3);
  if(it != v1.end()) cout << *it << endl;
  else cout << "not found" << endl;

  // 벡터에서 특정 인덱스 값 지우기 - erase, erase(remove)
  v1.erase(v1.begin() + 1); // 벡터명.erase(지울 인덱스)
  v1.erase(remove(v1.begin(), v1.end(), 7), v1.end());  // 특정 원소값 지울 때

  // 문자열 자르기 - substr
  s1 = "hello";
  string s2 = s1.substr(0,3); // 문자열이름.substr(시작점, n개길이);
  cout << s2 << endl;

  // 해시 맵
  map<string, int> m;
  m.insert(make_pair("a", 1));
  m.insert({"b", 2});
  m["c"] = 3;
  m.erase("a");
  if (m.empty()) cout << "empty" << endl;
  if (m.find("b") != m.end())
    cout << m.find("b")->second << endl; // 키 값 유무 확인

  // cmath 활용
  int a = 2;
  int b = 2.5;
  min(a, b);
  max(a, b);
  ceil(b);
  floor(b);
  abs(a);
  fabs(b);
  pow(a, b);  // a^b 값을 리턴
  sqrt(a);  // 루트 a 리턴

  // stack 활용
  stack<int> st;
  st.push(1);
  st.push(2);
  a = st.top();
  st.pop();
  st.size();
  cout << st.empty() << endl;

  // queue 활용
  queue<int> q;
  q.push(5);
  q.push(10);
  q.push(15);
  q.pop();
  q.front();
  q.back();
  q.size();
  cout << q.empty() << endl;

  return 0;
}
