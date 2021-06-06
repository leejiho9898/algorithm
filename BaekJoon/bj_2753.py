year = int(input())
if year % 4 == 0 and ( year % 100 != 0 or year % 400 == 0 ):
    print(1)   
else:
    print(0)

# answer = 0
# if year%4==0:
#     answer=1
#     if year%100==0:
#         answer=0
#         if year%400==0:
#             answer=1
