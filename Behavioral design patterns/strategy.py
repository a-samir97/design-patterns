'''
The strategy method is Behavioral Design pattern that allows you to define the complete family of algorithms, 
encapsulates each one and putting each of them into separate classes and also allows to interchange there objects
'''

class Item:

    def __init__(self, price, discount_strategy=None):
        '''
            constructor for taking price and discount strategy
        '''
        self.price = price
        self.discount_strategy = discount_strategy
    

    def price_after_discount(self):
        '''
            function to return price after discount
        '''
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0
        
        return self.price - discount
    
    def __repr__(self):
          
        statement = "Price: {}, price after discount: {}"
        return statement.format(self.price, self.price_after_discount()) 

def twenty_percent_discount(order): 
    '''
        discount to 20 %
    '''  
    return order.price * 0.20

def fifty_percent_discount(order): 
    '''
        discount to 50 %
    '''
    return order.price * 0.50



"""main function"""
if __name__ == "__main__": 
  
    print(Item(20000)) 
      
    """with discount strategy as 20 % discount"""
    print(Item(20000, discount_strategy = twenty_percent_discount)) 
  
    """with discount strategy as 50 % discount"""
    print(Item(20000, discount_strategy = fifty_percent_discount)) 