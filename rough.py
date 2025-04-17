class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()
        
    def menu(self):
        user_input = input("""Welome to Chatbook!! How would you like to proceed?\n 
                           1. Press 1 to signup\n
                           2. Press 2 to signin\n
                           3. Press 3 to write a post\n
                           4. Press 4 to message a friend\n
                           5. Press anyother key to exit\n
                           """)
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        else:
            exit() 
            
            
obj = chatbook()
