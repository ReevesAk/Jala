class Static:
    num = 10
    def  __init__(self):
        print(self.num)

    def instance(self):
        print(self.num)

    def change_within_instance(self):
        Static.num = 5
        print(self.num)

    def change_within_class(self):
        s = Static()
        s.num = 15
        print(s.num)    

s = Static()
s.instance()
s.change_within_instance()
s.change_within_class()



          