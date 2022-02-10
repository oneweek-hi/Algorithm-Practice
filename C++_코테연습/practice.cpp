#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
using namespace std;

int main(){
    vector<int> v1(7,0);
    vector<vector<int> > v2(7, vector<int>(5,0));

    string s1 = "100";
    int n1 = stoi(s1, nullptr, 2);
    int n2 = stoi(s1, nullptr, 10);
    s1= to_string(n1);
    string s2= to_string(n2);
    
    cout << "s2: "<< s2 << endl;
    cout << "s1: "<< s1 << endl;
    reverse(s2.begin(), s2.end());
    cout << "reverse s2: "<< s2 << endl;
    

    fill(v1.begin(), v1.end(), 10);
    for (int i=0; i< v1.size(); i++){
        cout << v1[i] << " ";
    }
    v1[6] = 100;
    v1[2] = 3;
    cout << *max_element(v1.begin(), v1.end()) << "\n";
    cout << *min_element(v1.begin(), v1.end()) << "\n";
    cout << "max_index: " << max_element(v1.begin(), v1.end()) - v1.begin() << "\n";
    cout << "mix_index: " << min_element(v1.begin(), v1.end()) - v1.begin() << "\n";

    v1 = {2,5,7};
    for (int i=0; i< v1.size(); i++){
        cout << v1[i] << " ";
    }
    cout <<"\n";
    // vector<int> v4 = {3,5,7};
    vector<int> v = { 1, 2, 3, 7, 5}; 
    
    auto it = find(v.begin(), v.end(), 7);
    if(it != v1.end()) cout << *it << " "<< it - v1.begin() << endl;
    else cout << "not found" << endl;

    v.erase(v.begin()+3);
    for (int i=0; i< v.size(); i++){
        cout << v[i] << " ";
    }
    cout <<"\n";
    v.erase(remove(v.begin(), v.end(), 2), v.end());

    for (int i=0; i< v.size(); i++){
        cout << v[i] << " ";
    }

    s1 = "hello";
    string s3 = s1.substr(0,3);
    string s4 = s1.substr(2,5);
    cout<<"\n";
    cout<<s3 <<"\n";
    cout<<s4 <<"\n";
    
    map<string, int> m;
    m.insert(make_pair("a",1));
    m.insert({"b",2});
    m["c"] =3;
    cout<< m["a"] <<"\n";
    if (m.empty()) cout << "empty" << endl;
    if (m.find("c") != m.end()) cout << m.find("c")->second << endl; // 키 값 유무 확인

    for (auto it=m.begin(); it != m.end(); it ++){
      cout << it->first<< " "<< it->second<< endl;
    }

    for ( auto it:m){
      cout << it.first<< " "<< it.second<< endl;
    }

    int a =2;
    int b= 2.5;

    min(a,b);
    max(a,b);
    cout << ceil(3.14) <<"\n";
    cout << floor(1.89)<<"\n";
    cout << abs(-123)<<"\n";
    cout << fabs(20)<<"\n";
    cout << pow(2,4)<<"\n";
    cout << sqrt(4)<<"\n";

    stack<int> st;
    st.push(1);
    st.push(2);
    int z = st.top();
    st.pop();
    st.size();
    cout << st.empty() <<endl;


    queue<int> q;
    q.push(5);
    q.push(10);
    q.push(15);
    q.pop();
    cout << q.front() <<endl;
    cout << q.back() <<endl;
    cout <<q.size()<<endl;
    cout << !q.empty() << endl;

    





    
    





    


    // auto it = find(v1.begin(), v1.end(),3);
    // if(it != v1.end()) cout << *it << endl;
    // else cout << "not found" << endl;   
}