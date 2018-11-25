
def sign_up():
    if(check_user_name()== -1):
        print('name already exist')
    else:
        users_object  = open(path_users_passwords, "a")
        users_object.write('\n'+name+'-'+password)
        users_object  = open(path_users_passwords, "r")
        for line in users_object:
            print(line)
    
    users_object.close()
    
def log_in():
    users_object = open(path_users_passwords, "r") 
    for line in users_object:
        print(line)
    #print('The identification process passed successfully')
    users_object.close()        

def check_user_name():
    f  = open(path_user_names, "r")
    for line in f:
        if(line == name):
            return -1
    return 1
    f.close()
    
print('choose option number:')
path_users_passwords=r'\Users\sapir\Desktop\users-passwords.txt'
path_user_names=r'\Users\sapir\Desktop\user-names.txt'
print('1.log in')
print('2.sign up')
kelet = input()
print('enter name')
name = input()
print('enter password')
password = input()
if(kelet=='2'):
   sign_up()

if(kelet=='1'):
    log_in()

