"""
Create a class called FoodOrder with attributes: restaurant_name, items (list), and total_price. Write an __init__() constructor to initialize these, then create an object representing your last Zomato or Swiggy order and print its details

"""
class FoodOrder:
        # def __init__(self, restaurant_name, items, total_price):
        #     self.restaurant_name = restaurant_name
        #     self.items = items
        #     self.total_price = total_price

        rest_name =input("enter the restaurant name : ")
        items = []
        total_price = 0
        for i in range(5):
            item = input("enter the item : ")
            items.append(item)
            total_price += int(input("enter the price : "))
        def show(self):
            print("restaurant name is :",self.rest_name)
            print("items are :",self.items)
            print("total price is :",self.total_price)

f=FoodOrder()
f.show()


