import math

class Fraction:
    def __init__(self,nn,dd):
        self.numerator = nn
        self.denominator = dd

    def sum(self,other):
        result_n = self.numerator * other.denominator + self.denominator * other.numerator
        result_d = self.denominator * other.denominator
        result = Fraction(result_n, result_d)
        return result

    def mul(self, other):
        result_n = self.numerator * other.numerator
        result_d = self.denominator * other.denominator
        result = Fraction(result_n, result_d)
        return result

    def sub(self,other):
        result_n = self.numerator * other.denominator - self.denominator * other.numerator
        result_d = self.denominator * other.denominator
        result = Fraction(result_n, result_d)
        return result

    def div(self,other):
        result_n = self.numerator * other.denominator
        reselt_d = self.denominator * other.numerator
        result = Fraction(result_n, reselt_d)
        return result

    def fraction_to_number(self):
        if self.denominator!=0:
            num = self.numerator / self.denominator
            return num
        else:
            return "Cannot divide be zero."
    
    def simplify(self):
        gcd = math.gcd(self.numerator,self.denominator)
        result_n = int(self.numerator/gcd)
        result_d = int(self.denominator/gcd)
        result = Fraction(result_n,result_d)
        return result

    def show(self):
        print(self.numerator,"/",self.denominator)



n1=3
d1=5

n2=15
d2=6

f1=Fraction(n1,d1)
f2=Fraction(n2,d2)

f1.show()
f2.show()

sum_result=f1.sum(f2)
sum_result.show()
print(sum_result.fraction_to_number())
simpled=sum_result.simplify()
simpled.show()


n3=10
d3=0

f3=Fraction(n3,d3)
print(f3.fraction_to_number())






