class Date:
    def __init__(self,y,m,d,t):
        #properties
        self.year=y
        self.month=m
        self.day=d
        self.type=t #Solar date, lunar date, Gregorian date

        #methods
        def convert_to_solar(self):
            ...

        def convert_to_lunar(self):
            ...

        def convert_to_gregorian(self):
            ...

        def difference(self):
            ...

        def is_today(self):
            ...
