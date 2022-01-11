# problem link:- https://leetcode.com/problems/find-the-difference/submissions/
s = "a"
t = "aa"
diff = 0
for char in s:
    diff ^= ord(char)
for char in t:
    diff ^= ord(char)
print(chr(diff))
