// Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

#include <iostream>
#include <string>
#include <map>
#include <algorithm>    // std::sort

using namespace std;
// memory: O(n)
// runtime: O(n) 
bool isUnique( string s){
  map<char,bool> m;
  for (int i = 0 ; i<s.length();i++){
    if (m.count(s[i]) == 1) return false;
    m.insert(pair<char,bool>(s[i],true));
  }
  return true;
}
  
// memory: O(1)
// runtime: O(n*log n)
bool isUniqueSort (string s){
  sort(s.begin(),s.end());
  for (int i = 0; i < s.length()-1;i++){
    if (s[i] == s[i+1]) return false;
  }
  return true;
}

int main(){
  string s = "abvcds";
  cout << boolalpha << isUnique(s) << "\n";
  cout << boolalpha << isUniqueSort(s) << "\n";
}
