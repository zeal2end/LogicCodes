#include<iostream>
#include "vector"
using namespace std;
int main(){
	int n;
	cin >> n;
	long sum = 0;
	for(int i= 0;i<n;i++){
		int a;
		cin >> a;
		sum+=a;
	}
	cout << sum;


}
