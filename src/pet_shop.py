# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, to_add_or_to_cost):
    pet_shop["admin"]["total_cash"] += to_add_or_to_cost

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, no_sold_pets):
    pet_shop["admin"]["pets_sold"] += no_sold_pets

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_dict_key_and_searched_val(pet_shop, key_name, searched_value):
    return_list = []
    pets = pet_shop["pets"]
    for pet in pets:
        if pet[key_name] == searched_value:
            return_list.append(searched_value)
    return return_list

def get_pets_by_breed(pet_shop, breed_name):
    return get_pets_by_dict_key_and_searched_val(pet_shop, "breed", breed_name)

# standard answer below - replaced by more generic/reuseable get_pets_by_dict_key_and_searched_val (above)
# though maybe totally unnessesary
# def get_pets_by_breed(pet_shop, breed_name):
#     return_list = []
#     pets = pet_shop["pets"]
#     for breed in pets:
#         if breed["breed"] == breed_name:
#             return_list.append(breed_name)
#     return return_list

def find_pet_by_name(pet_shop, pet_name): #needs to return single value not list
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, price):
    customer["cash"] -= price

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
    if get_customer_cash(customer) >= pet["price"]:
        return True
    return False

# created these to refactor sell_pet_to_customer
def check_pet_exists(pet_shop, pet_object):
    for pet in pet_shop["pets"]:
        if pet == pet_object:
            return True
    return False

def move_pet(pet_shop, pet, customer):
    add_pet_to_customer(customer, pet)
    remove_pet_by_name(pet_shop, pet["name"])

def process_pet_shop_transaction(pet_shop, customer, pet_price):
    add_or_remove_cash(pet_shop, pet_price)
    remove_customer_cash(customer, pet_price)

def sell_pet_to_customer(pet_shop, pet, customer):

    #if the pet doesn't exist; the selling stops
    if check_pet_exists(pet_shop, pet) == False: 
        print("That pet doesn't exist!")
        return 
    #If customer can't afford the pet; the selling stops
    if customer_can_afford_pet(customer, pet) == False: 
        print("Customer cannot afford to buy this pet!")
        return
    else: 
        move_pet(pet_shop, pet, customer)
        process_pet_shop_transaction(pet_shop, customer, pet["price"])
        increase_pets_sold(pet_shop, 1)











# # testing


# def add_or_remove_cash(pet_shop, value):

#     int(pet_shop["cash"] + value)

#     int(pet_shop["cash"] += value)

# def get_some_dict_values(dictionary):
#     return dictionary["key_1"]["key_2"]
#     #returns the value stored under the key

# def add_to_dict_value(dictionary, amount):
#     return (get_some_dict_values(dictionary) + amount)
#     #this will return a value + 'amount', but won't change the amount stored in the dict

# def add_to_dict_value(dictionary, amount):
#     get_some_dict_values(dictionary) += amount
#     #errors becasue you cannot assign a function to a value

# def add_to_dict_value(dictionary, amount):
#     dictionary["key_1"]["key_2"] += amount
#     #reassign the dict entry to itself plus amount (+=)

