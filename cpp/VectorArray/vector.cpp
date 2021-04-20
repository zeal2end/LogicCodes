#include "iostream"
#include "DynamicArray.h"

using namespace std;
#define darr DynamicArray
int main(){
	DynamicArray<int> vec;
	//vec.push_back(5);
	int arr[10];
	for(int i = 0;i<10;i++){
		arr[i] = i;
		vec.push(i);
	cout << vec.at(i) << endl;
	}



	return 0;
}
