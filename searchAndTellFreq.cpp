
#include "bits/stdc++.h"
using namespace std;
using ll=long long;
using vi=vector<int>;
#define ar array
int n;
int main(){
	vi v(5);
	for(int& a: v)cin >> a;
	int k;
	cin >> k;
	int cnt =0;
	for(int a: v)cnt+= a == k;
	cout << (cnt? cnt: -1);
}
