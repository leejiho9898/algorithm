h,m = input().split()
h=int(h)
m=int(m)

if m>=45 : m=m-45
elif m < 45 and h>0 :
    m=m+15
    h=h-1
else:
    h=23
    m=m+15

print(h,m)