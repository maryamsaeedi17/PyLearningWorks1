class Time:
    def __init__(self,hh,mm,ss):
        self.hour = hh
        self.min = mm
        self.sec = ss
        self.fix()

    def show(self):
        print(self.hour,":",self.min,":",self.sec)

    def sum(self, other):
        sec = self.sec + other.sec
        min = self.min + other.min
        hour = self.hour + other.hour
        result = Time(hour, min, sec)
        return result

    def sub(self,other):
        sec = self.sec - other.sec
        min = self.min - other.min
        hour = self.hour - other.hour
        result = Time(hour, min, sec)
        return result
    
    def time_to_sec(self):
        result = (self.hour * 60 + self.min) * 60 + self.sec
        return result
    
    def sec_to_time(self):
        hour = self.sec//3600
        min = (self.sec - hour * 3600) // 60
        sec = (self.sec - hour * 3600) - min * 60
        result = Time(hour, min, sec)
        return result
        
    def GMT_to_IRAN(self):
        IRAN_time = Time(3, 30, 0)
        result = Time.sum(self, IRAN_time)
        return result

    def fix(self):
        if self.sec >= 60:
            while True:
                if self.sec >= 60:
                    self.sec -= 60
                    self.min += 1
                else:
                    break
        if self.min>=60:
            while True:
                if self.min >= 60:
                    self.min -= 60
                    self.hour += 1
                else:
                    break
        if self.sec < 0:
            while True:
                if self.sec < 0:
                    self.sec += 60
                    self.min -= 1
                else:
                    break
        if self.min < 0:
            while True:
                if self.min < 0:
                    self.min += 60
                    self.hour -= 1
                else:
                    break



h1=3
m1=15
s1=45

h2=2
m2=20
s2=25

t1=Time(h1,m1,s1)
t2=Time(h2,m2,s2)

t1.show()
t2.show()

s1=t1.sum(t2)
s1.show()

s2=t1.sub(t2)
s2.show()

sec=t1.time_to_sec
print(sec)

s=3665
t=Time(0,0,s)
t.show()

G=Time(0,0,0)
I=G.GMT_to_IRAN()
I.show()