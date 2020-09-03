
#include "bits/stdc++.h"
using namespace std;
using ll=long long;
using vi=vector<int>;
#define ar array
int n;
int main(){
	vi v(10);
	for(int& a:v)cin >> a;
	int search;
	cin >> search;
	for(int a : v){
		if(a == search){
			cout << "found";
			return;
		}
	}
	cout <<"not found";
}
