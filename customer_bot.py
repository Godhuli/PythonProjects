# Customer Bot Project

# Creating customer service bot function


def cs_service_bot():
    # Replace `pass` with your code
    response = input('Hello! Welcome to the DNS Cable Company \'s Service Portal. Are you a new or existing customer?\n'
                     '[1] New Customer\n'
                     '[2] Existing Customer')
    if response == "1":
        new_customer()
    elif response == "2":
        existing_customer()
    else:
        print(" Sorry, we didn't understand you selection.")
        #cs_service_bot()


def existing_customer():
    # Replace `pass` with your code
    print()
    response = input(
        'What kind of support do you need?\n'
        '[1] Television Support\n'
        '[2] Internet Support\n'
        '[3] Speak to a support representative.')
    if response == "1":
        television_support()
    elif response == "2":
        internet_support()
    elif response == "3":
        internet_support()
    else:
        print()
        print("Sorry, we didn't understand your selection.")
        existing_customer()


def new_customer():
    # Replace `pass` with your code
    print()
    response = input('We\'re excited to have you join the DNS family, how can we help you? Select\n'
                     '[1]Sign up for service.\n'
                     '[2] Schedule a home visit.\n'
                     '[3] Speak to a sales representative.')
    if response == "1":
        sign_up()
    elif response == "2":
        home_visit()
    elif response == "3":
        live_rep("sales")
    else:
        print("Sorry, we didn't understand your selection.")
        new_customer()


def television_support():
    # Replace `pass` with your code
    print()
    response = input(
        'What is the nature of your problem?:\n'
        '[1] I can\'t access certain channels.\n'
        '[2] My picture is blurry.\n'
        '[3] I keep losing service.\n'
        '[4] Other issues.')
    if response == "1":
        print("Please check the channel lists at DefinitelyNotSinister.com.\n"
              "If the channel you cannot access is there, please contact a live representative.")
        did_that_help()
    elif response == "2":
        print("Try adjusting the antenna above your television set.")
        did_that_help()
    elif response == "3":
        print("Is it raining outside? If so, wait until it is not raining and then try again.")
        did_that_help()
    elif response == "4":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        television_support()


def internet_support():
    # Replace `pass` with your code
    print()
    response = input(
        'What is the nature of your problem?\n'
        '[1] I can\'t connect to the internet.\n'
        '[2] My connection is very slow.\n'
        '[3] I can\'t access certain sites.\n'
        '[4] Other issues.')
    if response == "1":
        print("Unplug your router, then plug it back in, then give it a good whack, like the Fonz.")
        did_that_help()
    elif response == "2":
        print(
            " Make sure that all cell phones and other peoples computers are not connected to the internet, so that\n"
            " you can have all the bandwidth")
        did_that_help()
    elif response == "3":
        print("Move to a different region or install a VPN. Some areas block certain sites.")
        did_that_help()
    elif response == "4":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        internet_support()


def did_that_help():
    print()
    response = input('Was your issue resolved?\n'
                     '[1]Yes\n'
                     '[2]No')
    if response == "1":
        "Thank you for using bot service"
    elif response == "2":
        response = input("Would you like to talk to a live representative or schedule a home visit?\n"
                         "[1] Live representative.\n"
                         "[2] home_visit")
        if response == "1":
            live_rep("support")
        elif response == "2":
            home_visit("support")
        else:
            print("Sorry, we didn't understand your selection.")
            did_that_help()


def sign_up():
    print()
    response = input(
        'Great choice, friend! We\'re excited to have you join the DNS family! Please select the package you are\n'
        'interested in signing up for.\n'
        '[1] Bundle Deal (Internet + Cable)\n'
        '[2] Internet\n'
        '[3] Cable')
    if response == "1":
        print(
            "You've selected the Bundle Package! Please schedule a home visit and our technician will come and set up\n"
            " your new service.")
        home_visit("new install")
    elif response == "2":
        print(
            "You've selected the Internet Only Package! Please schedule a home visit and our technician will come and\n"
            " set up your new service.")
        home_visit("new install")
    elif response == "3":
        print("You've selected the Cable Only Package! Please schedule a home visit and our technician will come and\n"
              " set up your new service.")
    else:
        print("Sorry, we didn't understand your selection.")
        sign_up()


def home_visit(purpose="none"):
    print()
    response = ''
    if purpose == "none":
        response = input('What is purpose of home visit?\n'
                         '[1] New service installation.\n'
                         '[2] Existing service repair.\n'
                         '[3] Location scouting for unserviced region.')
    if response == "1":
        home_visit("new install")
    elif response == "2":
        home_visit("support")
    elif response == "3":
        home_visit("scout")
    else:
        visit_date = input(
            "Please enter a date below when you are available for a technician to come to your home.")
        print(
            "Wonderful! A technical will come visit you on" + visit_date + " Please be available between the hours of\n"
                                                                           " 1:00 am and 11:00 pm.")
        return visit_date


def live_rep(purpose):
    print()
    # Replace `pass` with your code
    if purpose == "Sales":
        print(
            "Please hold while we connect you with a live sales representative. The wait time will be between two\n"
            " minutes and six hours. We thank you for your patience.")
    if purpose == "support":
        print(
            "Please hold while we connect you with a live support representative. The wait time will be between two\n"
            " minutes and six hours. We thank you for your patience.")


cs_service_bot()












