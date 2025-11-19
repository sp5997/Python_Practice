# Password Strength Checker
# Check if password is weak, Medium or Strong , Critera --> <6 char (weak); 6-10char (medium); >10 char(strong)
password = (input('Enter your password:'))

if len(password)<6:
    print('Password is weak')
elif len(password)<=10:
    print('Password is medium')
else:
    print('password is strong')