class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        
        if isinstance(numerator, str):
            numerator = numerator.strip()
            numerator, denominator = numerator.split('/')

    def gcd(a, b):
        #TODO
        pass

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass