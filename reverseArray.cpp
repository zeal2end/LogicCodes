
#include "bits/stdc++.h"
using namespace std;
using ll=long long;
using vi=vector<int>;
#define ar array
int n;
int main(){
	cin >> n;
	vi v(n);
	for(int& a: v)cin >> a;
	reverse(v.begin(),v.end());
	for(int a: v)cout << a << " ";

}
