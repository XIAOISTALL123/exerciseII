class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        
        if isinstance(numerator, int) and isinstance(denominator, int):
            self.numerator = numerator
            self.denominator = denominator
        
        elif isinstance(numerator, str):
            self.numerator = numerator.strip()
            try:
                self.numerator, self.denominator = numerator.split('/')
            except:
                self.numerator = 0
                self.denominator = 1
        else:
            self.numerator = 0
            self.denominator = 1

        if denominator == 0:
            raise ZeroDivisionError

    def gcd(a, b):
        if b == 0:
            return abs(a)
        else:
            return gcd(b, a % b)

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass