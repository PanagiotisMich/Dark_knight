Username=input('What is your username:')
Password=input('What is your password:')
password_lenth=len(Password)
hidden_password='*'*password_lenth
print(f'{Username} your Password {hidden_password} is {password_lenth}')