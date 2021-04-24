#include "iostream"
#include "vector"
#include "array"
using namespace std;
#define ll long long
#define ar array
int n,k;
vector<ar<int,2>> moves;

bool isValid(int row,int col){ // check it again in case of wrong ans...
  for(auto a : moves){
    if(abs(row - a[0]) == abs(col - a[1]))return false;
  }
  return true;
}

ll foo(int i,int x=0, int y=0){
  if( i== k) return 1;
  ll ans = 0;
  for(int row = x;row<n;row++){
    for(int col = y;col<n;col++){
      if(isValid(row,col)){
		  moves.push_back({row,col});
		  ans += foo(i+1,row+1,col) + foo(i+1,row,col+1);
		  moves.pop_back();
      }
    }
  }
  return ans;
}

int main(){
  cin >> n >> k;
  if(n == k and n == 0)
    return 0;
  ll ans = foo(0);
  cout << ans <<endl;
}
