import random

destinations_list = ["San Juan", "Aruba", "Venice", "Italy" , "Greece" , "Belize"]


def random_item_picker(list):
    random_item = random.choice(list)
    return random_item

def user_destination_confirmation():
    random_destination = random_item_picker(destinations_list)
    user_input = input(f'Would you like to travel to {random_destination}? y/n ')
    if user_input == "y":
        print(f'Great, lets get {random_destination} booked for you! Next we will pick your mode of transportation')
        return random_destination
    elif user_input == "n":
        return user_destination_confirmation()


transportation_list = ["Rental car", "Train", "Bike", "Walking" , "Scooter"]

def random_item_picker(list):
    random_item = random.choice(list)
    return random_item

def user_transportation_confirmation():
    random_transportation = random_item_picker(transportation_list)
    user_input = input(f'Would you like to get around by {random_transportation}? y/n ')
    if user_input == "y":
        print(f'Good choice, {random_transportation} sounds like a great idea. Now lets see where you are going to eat. ')
        return random_transportation
    elif user_input == "n":
        return user_transportation_confirmation()



restaurant_list = ["Bak Steakhouse", "Pizzeria", "Steak 48", "Cuba Libre"]

def random_item_picker(list):
    random_item = random.choice(list)
    return random_item

def user_restaurant_confirmation():
    random_restaurant = random_item_picker(restaurant_list)
    user_input = input(f'Would you like dine at {random_restaurant}? y/n ')
    if user_input == "y":
        print(f'{random_restaurant} sounds delicious! Now lets find you some entertainment. ')
        return random_restaurant
    elif user_input == "n":
        return user_restaurant_confirmation()


entertainment_list = ["A concert", "The recording studio", "A museum", "Taking a nap"]
def random_item_picker(list):
    random_item = random.choice(list)
    return random_item

def user_entertainment_confirmation():
    random_entertainment = random_item_picker(entertainment_list)
    user_input = input(f'Does {random_entertainment} sound like fun? y/n ')
    if user_input == "y":
        print(f' {random_entertainment} thats a great vibe! ')
        return random_entertainment
    elif user_input == "n":
        return user_entertainment_confirmation()
        

def random_item_picker(list):
    random_item = random.choice(list)
    return random_item

    
def run_program():
    confirmed_destination = user_destination_confirmation ()
    confirmed_transportation = user_transportation_confirmation ()
    confirmed_restaurant = user_restaurant_confirmation()
    confirmed_entertainment = user_entertainment_confirmation()  

    user_input = input(f'Would you like to confirm this Day Trip? y/n')
    if user_input == "y":
        print(f'You have chosen to travel to {confirmed_destination} to get around by {confirmed_transportation} to dine at {confirmed_restaurant} and to enjoy spending time at {confirmed_entertainment}. ')
        return user_daytrip_confirmation
    elif user_input == "n":
        print("Let's start over! ")
        run_program()

run_program()

# def user_daytrip_confirmation():



# print (confirmed_daytrip)


# result_one = random_item_picker(destinations_list)
# print(result_one)

# result_two = random_item_picker(restaurant_list)
# print(result_two)

# result_three = random_item_picker(transportation_list)
# print(result_three)

# result_four = random_item_picker(entertainment_list)
# print(result_four)
# def user_daytrip_confirmation(user_destination_confirmation, confirmed_destination, confirmed_transportation, confirmed_restaurant, confirmed_entertainment, confirmed_daytrip, user_input):
 # confirmed_destination, confirmed_transportation, confirmed_restaurant, confirmed_entertainment = user_daytrip_confirmation
