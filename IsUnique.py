# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# memory: O(n)
# runtime: O(n) 
def isUniqueWithMap(s):
  m = {}
  for i in s:
    if (i in m): return False
    m[i]='1'
  return True
  
print(isUniqueWithMap("abcdd"))

# memory: O(1)
# runtime: O(n*log n)
def isUniqueNoMap( s ):
  s = sorted(s)
  for i in range(len(s)-1):
    if (s[i] == s[i+1]): return False
  return True

print(isUniqueNoMap("abccd"))
