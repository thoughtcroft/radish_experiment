class Calculator(object):

    def __init__(self, caching):
        self.caching = caching

    def add(self, number_one, number_two):
        return number_one + number_two

    def multiply(self, number_one, number_two):
        return number_one * number_two
