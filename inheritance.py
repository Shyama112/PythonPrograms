class Landline:
    def __init__ (self,name,brand,price,isfixed):
        self.name=name
        self.brand=brand
        self.price=price
        self.isfixed=isfixed
    def incoming(self):
        print("Attend the call")
    def outgoing(self):
        print("Make a call")
class ButtonPhone(Landline):
    def __init__(self,name,brand,price,isfixed,battery,storage):
        super().__init__(name,brand,price,isfixed)
##        self.name=name
##        self.brand=brand
##        self.price=price
##        self.isfixed=isfixed
        self.battery=battery
        self.storage=storage

b=ButtonPhone("v20","vivo",20000,False,5000,128)
b.outgoing()

class OnlineStore:
    def __init__ (self,name,service,priceLevel):
        self.name=name
        self.service=service
        self.priceLevel=priceLevel
    def ordering(self):
        print("buying the product")
    def returning(self):
        print("returning the product that has bought")
    def exchanging(self):
        print("exchange the product for a different one")
class Amazon(OnlineStore):
    def __init__ (self,name,service,priceLevel,coupons,discount):
        super().__init__(name,service,priceLevel)
        self.coupons=coupons
        self.discount=discount
    def primeMembership(self):
        
        print(self.name,"PrimeMembership is free for subscribers")
        

store=Amazon("Amazon","shopping","100-80000",">1000",">5000")
store.returning()
store.primeMembership()

    
        
        
    
