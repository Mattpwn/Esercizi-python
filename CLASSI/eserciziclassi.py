
#ESERCIZIO 9.1

class Restaurant:

    def __init__ (self, restaurant_name:str, cusine_type:str):

        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

ristorante: Restaurant = Restaurant("Schiano", "Pesce")
    
def describe_restaurant():

    print(ristorante)


        
   