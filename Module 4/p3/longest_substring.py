s=input()
max_str=""
for j in range(len(s)):
    sub_str=""
    t=s[j]
    for i in range(j,len(s)):
        if t<=s[i]:
            t=s[i]
            sub_str+=t
        else:
            break
    if len(max_str) < len(sub_str):
        max_str=sub_str
            
print(max_str)


        
        
