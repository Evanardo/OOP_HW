class Cart:

    def __init__(self, item):
        self.item = item
        # self.question = question
        #self.list = shopping_list

    def show(self):
        print(f"Your current shopping list:\n{self.item}")

    def add(self):
        while True:
            add_question = input("What would you like to add? ")
            if add_question() == 'a':
                self.item.append(add_question)
    def remove(self):
        while True:
            remove_question = input("Which item would you like to remove? ")
            if remove_question.lower() == 'r':
                
                self.item.remove(remove_question)
            print(f"\n{self.remove}was removed from you shopping list.\nHere is your updated list:\n{self.item}")
    # def shopping_cart():
    #     while True:
           



# shoha_cart = Cart([])
# brandt_cart = Cart([])
# question =  input("\nWelcome to your shopping list\n" + "Do you want to show [s], Add [a], Delete [d], clear [c] or [q] to Quit: ")

    
    def runnit():

        shopping_list = Cart

        while True:

            user_question = input("\nWelcome to your shopping list\n\n" + "Do you want to Show [s], Add [a], Delete [d], clear [c] or [q] to Quit: ")

            if user_question.lower() == 's':
                shopping_list.show()

            if user_question.lower() == 'a':
                shopping_list.add()
            
            if user_question.lower() == 'd':
                shopping_list.delete
            if user_question.lower() == 'c':
                shopping_list.clear()
                print(f"\nYour shopping list has been cleared... no going back...\n") 

            if user_question.lower() == 'q':
                print(f"\nHere's your shopping list... did you forget anything?\n{shopping_list}")
                break

            # if user_question.lower != str:
            #     print("\nDoes not compute, try again.")

    runnit()
evan_cart = Cart()





















# shopping_cart()

# show = (f"\nYour current shopping list:\n{shopping_list}")
# add = input("What would you like to add? ")
# delete = input("Which item would you like to remove? ")


# # containing
#     def shopping_cart(self):
#         self.user_question = input ("\nWelcome to your shopping list\n\n" + "Do you want to Show [s], Add [a], Delete [d], clear [c] or [q] to Quit: ")
#     def show(self):
#         self.display = shopping_list[]
        

#     def add(self):
#         if user_question.lower() == 'a':
#             Cart.add = input("what would you like to add? ")
#             shopping_list.append(add)
#             print(f"\nYour current shopping list:\n{shopping_list}")