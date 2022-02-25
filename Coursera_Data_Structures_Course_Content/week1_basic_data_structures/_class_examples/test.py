class Hello:
    hi1 = '1'
    hi2 = '2'
    hi_small = 'small hi'

    def __init__(self, veg = 'tuna'):
        self.veg = veg

    def hello_method(self):
        return self.hi_small

class BigHello(Hello):
    hi3 = '3'

    def __init__(self, big_veg = 'shark'):
        self.big_veg = big_veg
    
    def big_hello_method(self):
        a = self.hello_method()

        return self.hi_small, 'big ' + a
 


hey = BigHello()

print(hey.hi1, hey.hi2, hey.big_hello_method())
