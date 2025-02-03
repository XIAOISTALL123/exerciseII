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

    @staticmethod
    def euclidean(a, b):
        if int(b) == 0:
            return abs(int(a))
        else:
            return Fraction.euclidean(int(b), int(a) % int(b))
    @staticmethod    
    def gcd(a, b):
        if int(b) == 0 or int(a) == 0:
            return 0
        else:
            return Fraction.euclidean(int(a), int(b))

    def get_numerator(self):
        if Fraction.gcd(self.numerator, self.denominator) != 0:
            return str(int(self.numerator)//Fraction.gcd(self.numerator, self.denominator))
        else:
            return '0'

    def get_denominator(self):
        if Fraction.gcd(self.numerator, self.denominator) != 0:
            return str(int(self.denominator)//Fraction.gcd(self.numerator, self.denominator))
        else:
            return '0'

    def get_fraction(self):
        try:
            if int(self.denominator) == 0 or int(self.numerator) == 0:
                return '0'

            if int(self.denominator) < 0:
                if int(self.numerator) < 0:
                    return self.get_numerator()[1:] + '/' + self.get_denominator()[1:]
                else:
                    return '-' + self.get_numerator() + '/' + self.get_denominator()[1:]

            elif int(self.denominator) == 0 or int(self.numerator) == 0:
                return '0'
            else:
                return self.get_numerator() + '/' + self.get_denominator()
        except:
            return '0'
