#Rules:
# username sould not be more than 12 characters
# username must not contain spaces
# username must not contain digits
while True:
    username = input("Enter a username: ")

    if len(username) > 12:
        print("Username should be less than or equal to 12 characters only!")
    elif not username.find(" ") == -1:
        print("username must not have spaces!")
    elif not username.isalpha():
        print("username msut not contain digits!")
    else:
        print(f"Welcome {username}!!!")
        break