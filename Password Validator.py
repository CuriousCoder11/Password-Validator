#Password Validator
'''
This program will tell the user about how much strong their password is...
'''
user_input = input("Enter your password (please make sure it is strong enough): ")
while True:
    if len(user_input) <= 5:
        print("Password Strength: Weak")
        print("Please make your password more strong...")
        break;
    elif len(user_input) <= 10:
        print("Password Strength: Medium")
        print("Please make your password more strong if you want to...")
        break;
    elif len(user_input) > 10:
        print("Password Strength: strong")
        print("Your password is strong enough...")
        break;
    else:
        print("Please check your password/input...!") or print("AN ERROR HAS OCCURED WHILE VALIDATING YOUR PASSWORD...!")
        break;