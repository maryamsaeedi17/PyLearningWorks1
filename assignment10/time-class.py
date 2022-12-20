class Time:
    def __init__(self,h,m,s,t):
        #properties
        self.hour=h
        self.minute=m
        self.seconds=s
        self.type=t    #24hours or 12hours

        #methods
        def is_AM(self):
            ...

        def is_PM(self):
            ...

        def convert_to_secends(self):
            ...

        def difference(self):
            ...

        def convert_type(self):
            ...