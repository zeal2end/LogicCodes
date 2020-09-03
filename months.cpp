#include "bits/stdc++.h"
using namespace std;
using ll=long long;
using vi=vector<int>;
#define ar array
int n;
int main(){
	cin >> n;
	if(n == 2){
		cout << 28;
	}else if(n == 4 || n == 6 || n == 9 || n == 11){cout << 30;}
	else cout << 31;
}
