def get():
    with open('file.txt','r') as fil:
        print(fil.read())
def add(st):
    with open('file.txt','a') as fil:
        fil.write(st+'\n')
def uptdate(n,neword):
    with open('file.txt','r') as file:
        lines=file.readlines()
        try:
            for i in range(len(lines)):
                if i==n-1:
                    lines[i]=neword+'\n'
        except Exception as ex:
            print(ex)
            return 1
    with open('file.txt','w') as file:
        file.writelines(lines)
def delete(n):
    with open('file.txt','r') as file:
        lines=file.readlines()
        try:
            for i in range(len(lines)):
                if i==n-1:
                    lines[i ]= '\n'
        except Exception as ex:
            print(ex)
            return 1
        
    with open('file.txt','w') as file:
        file.writelines(lines)
        





while True:
    n=int(input('''
Hello welcome to list of this week lessons
Chouse your options:
                

1--------> Get
2--------> Add 
3--------> Update
4--------> Delete
                
'''))
    if n==1:
        get()
    if n==2:
        add(input('Enter subject to add--->'))
    if n==3: 
        uptdate(int(input('Enter num of subject for ubdate--->')),input('enter new name of subject--->'))
        'Sucesfuly Updated'
    if n==4:
        delete(int(input('Enter num of subject for ubdate--->')))

