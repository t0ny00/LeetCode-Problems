// Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.


#include <iostream>
#include <string>
#include <map>
#include <algorithm>    // std::sort

using namespace std;

// memory: O(n)
// runtime: O(n) 
bool isPermut( string s1, string s2){
  
  if (s1.length() != s2.length() ) return false;
  map<char,int> m;
  
  for (int i = 0 ; i<s1.length();i++){
    if (m.count(s1[i]) == 1) m[s1[i]] = m.find(s1[i])->second + 1;
    else m[s1[i]] = 1;
  }
  
  for (int i = 0; i < s2.length(); i++){
    if (m.count(s2[i]) == 0) return false;
    else{
      auto c = m.find(s2[i]);
      if(c->second > 0) m[s2[i]] = c->second - 1 ; 
      else return false; 
    }
  }
  return true;
}

// memory: O(1)
// runtime: O(n* log n) 
bool isPermutSort (string s1, string s2){
  
  if (s1.length() != s2.length() ) return false;
  
  sort(s1.begin(),s1.end());
  sort(s2.begin(),s2.end());
  
  for (int i = 0; i < s1.length();i++){
    if (s1[i] != s2[i]) return false;
  }
  return true;
}

int main(){
  string s1 = "abodef";
  string s2 = "abdecf";
  cout << boolalpha << isPermutSort(s1,s2) << "\n";
}
