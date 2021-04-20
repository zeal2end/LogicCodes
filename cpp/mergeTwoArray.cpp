// WAP to assign some values in two array and merge them into third array
#include "bits/stdc++.h"
using namespace std;
using ll=long long;
using vi=vector<int>;
#define ar array
int n,m;
int main(){
	cin >> n >> m;
	vi v(n+m);
	for(int& a: v)cin >> a;
	sort(v.begin(),v.end());
	for(int a: v)cout << a << " ";
}
