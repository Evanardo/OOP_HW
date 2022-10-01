# def shopping_cart():
#     dict = {}
#     entering_data = True
#     while entering_data:
#         items = input("what do you want to buy?")
#         quantity = input ("how many you want?")
#         # dict[items] = quantity
#         change = input("Do you want to : Show/Add/Delete or Quit?")
#         if change.lower() == 'show':
#             for items,quanity in dict.items():
#                 print(f'i want {quantity} of {items}')
#         if change.lower() == 'add':
#             print(dict)
#             # for item in dict:
#             #     if item[0] not in dict:
#             #         dict[item[0]] = item[1]
#             #     else:
#             #         dict[item[0]].append(item[1])
#         if change.lower() == 'delete':
#             x = input(f"which item would you like to delete? {dict} ")
#             del dict[x]
            
#         if change.lower() == 'quit':
#             for items, quantity in dict.items():
#                 print(f'i want {quantity} of {items}')
#             break
#         dict[items]=quantity
# shopping_cart()
# from classes import Cart

# def shopping_cart():

#     shopping_list = []

#     while True:

#         user_question = input("\nWelcome to your shopping list\n\n" + "Do you want to Show [s], Add [a], Delete [d], clear [c] or [q] to Quit: ")

#         if user_question.lower() == 's':
#             return Cart.show 

#         if user_question.lower() == 'a':
#             Cart.add = input("what would you like to add? ")
#             shopping_list.append(add)
#             print(f"\nYour current shopping list:\n{shopping_list}")
        
#         if user_question.lower() == 'd':
#             Cart.delete = input("which item would you like to remove? ")
#             shopping_list.remove(remove)
#             print(f"\n{remove} was removed from your shopping list.\n\n Here is your updated list:\n\n{shopping_list}\n")
#             # if len(shopping_list) == 0:
#             #     print("Nothing to remove")
#         if user_question.lower() == 'c':
#             Cart.clear shopping_list.clear()
#             print(f"\nYour shopping list has been cleared... no going back...\n") 

#         if user_question.lower() == 'q':
#             print(f"\nHere's your shopping list... did you forget anything?\n{shopping_list}")
#             break
#         if user_question.lower() != ('s', 'a', 'd','c','q'):
#             print("Not a valid entry. Please try again.")

# shopping_cart()

def shopping_cart():

    shopping_list = []

    while True:

        user_question = input("\nWelcome to your shopping list\n\n" + "Do you want to Show [s], Add [a], Delete [d], clear [c] or [q] to Quit: ")

        if user_question.lower() == 's':
            print(f"\nYour current shopping list:\n{shopping_list}")

        if user_question.lower() == 'a':
            add = input("what would you like to add? ")
            shopping_list.append(add)
            print(f"\nYour current shopping list:\n{shopping_list}")
        
        if user_question.lower() == 'd':
            remove = input("which item would you like to remove? ")
            shopping_list.remove(remove)
            print(f"\n{remove} was removed from your shopping list.\n\n Here is your updated list:\n\n{shopping_list}\n")
            # if len(shopping_list) == 0:
            #      print("Nothing to remove")
        if user_question.lower() == 'c':
            shopping_list.clear()
            print(f"\nYour shopping list has been cleared... no going back...\n") 

        if user_question.lower() == 'q':
            print(f"\nHere's your shopping list... did you forget anything?\n{shopping_list}")
            break

        if user_question.lower != str:
            print("\nDoes not compute, try again.")

shopping_cart()