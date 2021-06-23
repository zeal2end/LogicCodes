#include "bits/stdc++.h"
using namespace std;
using ll=long long;
using vi=vector<int>;
#define ar array
int n,average;
int main(){
	//good
	cin >> n;
	for(int i = 0;i<n;i++){
		int a;
		cin >> a;
		average += a;
	}
	cout << average/n;
}
