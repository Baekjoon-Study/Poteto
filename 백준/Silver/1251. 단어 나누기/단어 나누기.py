a = list(input())  
ans = []  
tmp = []  

for i in range(1, len(a) - 1):  
  for j in range(i + 1, len(a)):  
    b = a[:i][::-1]  
    c = a[i:j][::-1]  
    d = a[j:][::-1]  
    tmp.append(b + c + d)  

for k in tmp:  
  ans.append(''.join(k))  
print(sorted(ans)[0])  
