from oauth2client.service_account import ServiceAccountCredentials

s='Govardhan'
print("output",s[-0],s[0],s[-1],s[-2])
print(s[1:40])
print(s[:40])
print(s[:])
print(s*3)
print(len(s))
for i in s : print(i)
l=list(range(10,30))
for n in l:print(n)
print(l)
d={101:'durga',102:'ravi',103:'shiva'}
d[103]='Govardhan'
d[100]='Chaitu'
print(d)

list=[1,2,3,3,4,5,6,7,7,7,8,1,2,3,5]
unique_list=[]
duplicate_list=[]
for n in list:
    if n not in unique_list:
        unique_list.append(n)
    else:
        duplicate_list.append(n)

print(f'unique list {unique_list}')
print(f'unique list {duplicate_list}')





