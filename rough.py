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
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit() 
            
            
    def signup(self):
        email = input("Enter your email here --> ")
        password = input("Enter your password here --> ")
        self.username = email
        self.password = password
        print("You have signed up successfully!")
        print("\n")
        self.menu()
         
         
    def signin(self):
        if self.username=="" and self.password=="":
            print("Please signup first by pressing 1 in the menu")
        else:
            username = input("Enter your email herer --> ")
            password = input("Enter your password here --> ")
            if self.username == username and self.password == password:
                print("You have signed in successfully!!")
                self.loggedin = True
            else:
                print("Please input correct credentials")
        print("\n")
        self.menu()
        
    
    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your message here: ")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()
        
        
    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter your message here--> ")
            frnd = input("Whom to send the msg? ")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()     
              
obj = chatbook()
