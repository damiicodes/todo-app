#
# while True:
#     password = input('Please input your password or type Quit to end: ')
#     password = password.strip()
#     check_uppercase = ''
#     for char in password:
#         if char.isupper():
#             check_uppercase = 'uppercase'
#
#     if len(password) < 8:
#         print('Your password is too short')
#     if check_uppercase != 'uppercase':
#         print('You need an upper case character')
#
#     elif password == 'Quit':
#         break
import string

# while True:
#     password = input('Please input your password or type Quit to end: ')
#     password = password.strip()
#     check_uppercase = ''
#     for char in password:
#         if char.isupper():
#             check_uppercase = 'uppercase'
#
#     if len(password) < 8 or check_uppercase != 'uppercase':
#         if len(password) < 8:
#             print('Your password is too short')
#         if check_uppercase != 'uppercase':
#             print('You need an upper case character')
#     elif password == 'Quit':
#         break

while True:
    password = input('Please input your password or type Quit to end: ')
    password = password.strip()

    if password == 'Quit':
        break

    check_uppercase = False
    for char in password:
        if char.isupper():
            check_uppercase = True
            break

    check_number = False
    for char in password:
        if char.isdigit():
            check_number = True
            break

    check_special_character = False
    for char in password:
        if char in string.punctuation:
            check_special_character = True
            break

    if len(password) < 8:
        print('Your password is too short')
    if not check_uppercase:
        print('You need an uppercase character')
    if not check_number:
        print('You need a number in your password')
    if not check_special_character:
        print('You need to insert a special character in your password')
    if len(password) >= 8 and check_uppercase and check_number and check_special_character:
        print(f'Your password {password} has been accepted')
        break



# import string
#
# while True:
#     password = input('Please input your password or type Quit to end: ')
#     password = password.strip()
#
#     if password == 'Quit':
#         break
#
#     check_uppercase = False
#     check_number = False
#     check_special_character = False
#
#     for char in password:
#         if char.isupper():
#             check_uppercase = True
#         elif char.isdigit():
#             check_number = True
#         elif char in string.punctuation:
#             check_special_character = True
#
#     if len(password) < 8:
#         print('Your password is too short')
#     if not check_uppercase:
#         print('You need an uppercase character')
#     if not check_number:
#         print('You need a number in your password')
#     if not check_special_character:
#         print('You need to insert a special character in your password')
#     else:
#         print(f'Your password "{password}" has been accepted')
