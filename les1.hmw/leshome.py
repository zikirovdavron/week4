#task1
# import random
# lst=[]
# cnt=0
# while True:
#     a=random.randint(1,20)
#     if a%2==0:
#         cnt+=1
#         if cnt==10:
#             break
#         lst.append(a)
# print(lst)



#task2
# import random
# lst=[]
# cnt=0
# for i in range(100):
#     a=random.random()
#     if 0.3<=a<=0.7:
#         cnt+=1
# print(cnt)

#task3
# import random
# lst = ['Ali', 'Zarina', 'Bobur', 'Madina', 'Rustam', 'Olim', 'Malika', 'Orzu', 'Lola', 'Samad']
# lst2=[]
# for i  in range(3):
#     a=random.choice(lst)
#     lst2.append(a)
# print(lst2)

#task4
# import random
# lst = ['apple', 'banana', 'grape', 'orange', 'lemon']
# for i  in range(3):
#     random.shuffle(lst)
#     print(lst)

#task5
# import random
# lst = [1,2,3,4,5,6,7,8,9,10]
# lst2=[]
# random.shuffle(lst)
# for i  in range(3):
#     a=random.choice(lst)
#     lst2.append(a)
    

# print(lst2)

#task6
# import random
# lst=[]
# cnt=0
# while True:
#     a=random.randint(1,99)
#     if a%2!=0:
#         cnt+=1
#         lst.append(a)
#         if cnt==7:
#             break
    
# lst.sort()
# lst.reverse()
# print(lst)

#task7
# import random
# lst=[]
# cnt=0
# s=0
# cnt=0
# while True:
#     a=random.randint(1,10)
#     if a%2!=0:
#         s+=a
#         cnt+=1
#         lst.append(a)
#         if cnt==10:
#             break
    
# n=s/cnt
# print(lst)
# print(f'sredniy:{n}')

#task8
# import random
# lst=[]
# cnt=0
# cnt2=0
# s=0
# cnt=0
# while True:
#     a=random.randint(1,100)
#     cnt+=1
#     lst.append(a)
#     if cnt==20:
#         break
# print(lst)
# lst2=[]
# while True:
#     b=random.choice(lst)
#     lst2.append(b)
#     s+=b
#     cnt2+=1
#     if cnt2==5:
#         break
# print(lst2)
# print(f'sum:{s}')

#task9
import random
cr=0
cg=0
cb=0
lst=['red','green','blue']
for i in range(1000):
    a=random.choices(lst[5,3,2])
    if a==['red']:
        cr+=1
    if a==['green']:
        cg+=1
    if a==['blue']:
        cb+=1
print(f'red:{cr}')
print(f'green:{cg}')
print(f'blue:{cb}')
    