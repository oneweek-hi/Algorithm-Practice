#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> arr(n);
    vector<int> d(n);
    for (int i =0; i<n; i++){
        cin >> arr[i];
    }

    for(int i=0; i < n; i++){
        d[i] = arr[i];
        if(i == 0){
            continue;
        }
        for (int j=0; j<=i; j++){
            if (arr[i] > arr[j] && d[j]+arr[i] >d[i]){
                d[i] = d[j]+arr[i];
        }

        } 
    }

    int ans = *max_element(d.begin(),d.end());
    // int result = max_element(d.begin(),d.end());
    int index = max_element(d.begin(),d.end()) - d.begin();
    cout << ans << '\n';
        for (int i =0; i<n; i++){
        cout << d[i] << ' ';
    }
    cout << '\n';
    sort(d.begin(), d.end()); 
        for (int i =0; i<n; i++){
        cout << d[i] << ' ';
    }
    sort(d.begin(), d.end(), greater<int>());
    cout << '\n';
            for (int i =0; i<n; i++){
        cout << d[i] << ' ';
    }
    cout << '\n';
    cout << "index: "<<index << '\n';
    return 0;
    

}