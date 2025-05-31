from datetime import datetime
import random

def registration(name,surname,age,creat_date,last_update,username,password):
    pass1=input('enter your pass again for checking--> ')
    if pass1!=password:
        print("wrong input")
        return 0
    with open('file.txt','a') as file:
        file.write(f'{name}/{surname}/{age}/{creat_date}/{last_update}/{username}/{password}/\n')
    print('you registered sucsessifully now you can log in to your own account!!')

def login(username,password ):
    with open('file.txt','r') as file:
        lines=file.readlines()
    for ents in lines:
        lst1=ents.split('/')
        if lst1[5]==username and lst1[6]==password:
            print('you logged in sucsessifully  ')
            while True:
                print(f'''
            Welcome {lst1[5]} to your own account
your name    -->  {lst1[0]}
your surname -->  {lst1[1]}
your age     -->  {lst1[2]}

your registration date in our platform --> {lst1[3]}
your last update here--> {lst1[4]}

''')
                x=int(input('''
what do you want to do? 
1 -- >  update your accound
2 -- >  logout your account
3 -- >  delete your account
'''))
                if x==1:
                    name=input('enter new name  --> ')
                    surname=input('enter new surname --> ')
                    age=input('enternew age --> ')
                    last=datetime.now()
                    lst1[0]=name
                    lst1[1]=surname
                    lst1[2]=age
                    lst1[4]=str(last)
                    lines.remove(ents)
                    ents='/'.join(lst1)
                    lines.append(ents)
                    with open('file.txt','w') as file:
                            file.writelines(lines)
                    print('Now your account  updated sucsessifuly')

                if x==2:
                    print('you logged out')
                    return 0
                if x==3:
                    passw=input('enter your password --> ' )
                    if passw==password:
                        lines.remove(ents)
                        with open('file.txt','w') as file:
                            file.writelines(lines)
                        print('your account deleted for ever ')
                        return 1
                    else :
                        print('wrong password')
        else:
            print('wrong username or password try again')

def forgot_password(username):
    n=str(random.randint(1000,9999))
    with open('passwords.txt','w+') as file:
        file.write(n)
    ps= input('enter 4-digit password from passwords.txt --> ')
    if n==ps:
        with open('file.txt','r') as file:
            lines=file.readlines()
        for ents in lines:
            lst1=ents.split('/')
            if lst1[5]==username:
                new_pass=input('enter new password --> ')
                new_pass2=input('enter new password again --> ')
                if new_pass==new_pass2:
                    lst1[6]=new_pass
                    lines.remove(ents)
                    ents='/'.join(lst1)
                    lines.append(ents)
                    with open('file.txt','w')as file:
                        file.writelines(lines)
                        print('your password ')
                        return 'hello'
                print('passwords are not equal ')
            print('user not found ')
            return 'hello'

        



while True:
    try:
        n=int(input("""
WELCOME TO YOUR PROFIL IN GOOGLE
choose your option 
1 --> registration to Google
2 --> login in Google 
3 --> forgot your Google password 
-------->   """))
        if n==1:
            registration(
                input('enter your name     --> '),
                input('enter your surname  --> '),
                input('enter your age  --> '),
                datetime.now(),
                datetime.now(),
                input('enter your username --> '),
                input('enter your pasword  --> '),
                
            )
        if n==2:
            login(input('enter your username in Google--> '),input('enter your password for Google --> '))
        if n==3:
            forgot_password(input('enter your username in Google--> '))
    except Exception as ex:
        print(ex)