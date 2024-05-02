from colorama import Style

class BudgetCategory:
    def __init__ (self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__expense = 0  #---Set this to 0 since the user dictates this 

    def get_category_name(self):    #---simply returns the category name
        return self.__category_name
    
    def set_category_name(self, new_name):  #---SET category allows us to control the input, validating basically. Not much is needed for name
        self.__category_name = new_name

    def get_allocated_budget(self):
        self.__allocated_budget
    
    def set_allocated_budget(self, new_budget): #---validates that the 
        if new_budget >= 0:
            self.__allocated_budget = new_budget
        else:
            print('Please enter a non-negative amount')

    def add_expense(self, expense):
        if expense >= 0:
            self.__expense += expense
        else:
            print('Please enter a non-negative amount')

    def display_category_summary(self):
        budget_summary = self.__allocated_budget - self.__expense
        print(f'For {self.__category_name} you have spent ${self.__expense} out of your bugeted ${self.__allocated_budget} leaving you with ${budget_summary}\n')


# Example usage
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()

fun = BudgetCategory('Baseball Games', 70)
fun.add_expense(35)
fun.display_category_summary()

car_payment = BudgetCategory('Car Lease', 450)
car_payment.add_expense(450)
car_payment.display_category_summary()
print(car_payment.get_category_name())
print()
print(Style.BRIGHT + 'Lets give this a more pretentious name...\n' + Style.RESET_ALL)
car_payment.set_category_name('BMW Lease')
print(car_payment.get_category_name())
print()
print(Style.BRIGHT + 'there we go :)\n' + Style.RESET_ALL)
print(Style.BRIGHT + 'maybe we should increase our car budget...zoom zoom...\n' + Style.RESET_ALL)
car_payment.set_allocated_budget(900)
car_payment.display_category_summary()
print(Style.BRIGHT + 'much better...\n' + Style.RESET_ALL)