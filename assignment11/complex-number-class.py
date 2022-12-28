class Complex:
    def __init__(self,rr,ii):
        self.real = rr
        self.image = ii

    def sum(self,other):
        result_r = self.real + other.real
        result_i = self.image + other.image
        result = Complex(result_r, result_i)
        return result

    def mul(self, other):
        result_r = self.real * other.real - self.image * other.image
        result_i= self.real * other.image + self.image *other.real
        result = Complex(result_r, result_i)
        return result

    def sub(self,other):
        result_r = self.real - other.real
        result_i = self.image - other.image
        result = Complex(result_r, result_i)
        return result

    def show(self):
        if self.image>0:
            print(self.real,"+i",self.image)
        elif self.image<0:
            print(self.real,"-i",abs(self.image))
        else:
            print(self.real)
            print("--> A real number is a complex number with an imaginary part equal to zero.")




r1=4
i1=-3

r2=-2
i2=3

c1=Complex(r1,i1)
c2=Complex(r2,i2)

c1.show()
c2.show()

s1=c1.sum(c2)
s1.show()

m=c1.mul(c2)
m.show()

s2=c1.sub(c2)
s2.show()



