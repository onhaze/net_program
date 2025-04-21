class MyComplex:
    def __init__(self, real_1, imaginary_1, real_2, imaginary_2):
        self.real_1 = real_1
        self.imaginary_1 = imaginary_1
        self.real_2 = real_2
        self.imaginary_2 = imaginary_2
    
    def multiply(self):
        # (a + bi) x (c + di) = (ac - bd) + (ad + bc)i
        real_result = (self.real_1 * self.real_2) - (self.imaginary_1 * self.imaginary_2)
        imaginary_result = (self.real_1 * self.imaginary_2) + (self.imaginary_1 * self.real_2)
        print(f"{real_result}+{imaginary_result}i")

# 복소수 a = 3-4i, b = -5+2i
complex_nums = MyComplex(3, -4, -5, 2)
complex_nums.multiply()