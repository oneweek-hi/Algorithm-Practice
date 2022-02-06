#include <vector>
#include <iostream>
#include <algorithm>
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

    // v1 = {3,5,7,0,0,0,0};
    // vector<int> v4 = {3,5,7};
    vector<int> v = { 1, 2, 3, 4, 5}; 

    // auto it = find(v1.begin(), v1.end(),3);
    // if(it != v1.end()) cout << *it << endl;
    // else cout << "not found" << endl;   
}