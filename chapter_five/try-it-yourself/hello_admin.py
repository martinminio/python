users = ["martin", "seba", "armando", "ivan" , "tomas", "admin"]
users.clear()
if users:
    for user in users:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again")
else:
     print("We need to find some users!")   

## checking usernames
current_users = ["martin", "seba", "armando", "ivan" , "tomas", "admin"]
new_users = ["martin", "horacio", "natalia"]

for new_user in new_users:
    if new_user in current_users:
        print("Please, enter a new username")
    else:
        print("username available")
        


    
