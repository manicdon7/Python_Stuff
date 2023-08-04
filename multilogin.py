while True:
    my_dict = {}
    def createaccount():
        choice = input("Are you new to our community?\n if yes press 1\n if no press 2\n")
        if choice == '1':
            signup()
        elif choice == '2':
            signup.login()
        else:
            print("Enter a valid answer")


    def signup():
        
        email_id = input("Enter your email_id :")
        signup_password = input("Enter your Password :")
        category = input("Enter your Category \n1.NGO people \n2.Food people\n") 
        my_dict['email_id'] = email_id
        my_dict['signup_password'] = signup_password
        my_dict['category'] = category
        
        
        def login():
                login_id = input("enter your email:")
                password = input("Enter your password:")
                if login_id in email_id and password in signup_password:
                    if "1" in category:       
                        NGO_login()
                    elif "2" in category:
                        Food_login()
        login()
            
            
                
            
    def NGO_login():
        NGO = {}
        NGO_Name = input("Enter NGO Name:")
        location = input("Enter NGO Location:")
        peoples = input("Enter Number of people in NGO's care:")
        web_link = input("Enter you NGO's link:")
        NGO['NGO_Name']=NGO_Name
        NGO['location']=location
        NGO['peoples']=peoples
        NGO['web_link']=web_link
        print("setup successful!")
        print("you are in NGO site")
        
    def Food_login():
        food = {}
        Hotel_Name = input("Enter restaurant Name:")
        location = input("Enter restuarant Location:")
        Type = input("Hotel type veg or non-veg:")
        web_link = input("Enter you restaurant's link:")
        food['Hotel_Name'] = Hotel_Name
        food['location'] = location
        food['Type'] = Type
        food['web_link'] = web_link
        
        
        print("setup successful!")
        
    def createaccount():
        choice = input("Are you new to our community?\n if yes press 1\n if no press 2\n")
        if choice == '1':
            signup()
        elif choice == '2':
            login1()
            
        else:
            print("Enter a valid answer")
            
            
    def login1():
                login_id = input("enter your email:")
                password = input("Enter your password:")
                if login_id and password in my_dict:
                    print(my_dict["category"])
                
                    
            
    createaccount()
