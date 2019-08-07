class Phone(object):
    def __init__(self, phone_number):
        filtered = filter(lambda c: c.isnumeric(), phone_number)
        self.number = ''.join(filtered)
        numberLength = len(self.number)

        if numberLength < 10 or numberLength > 11:
            raise ValueError('Invalid phone number')
        elif numberLength == 11 and self.number[0] != '1':
            raise ValueError('Invalid phone number')
        elif numberLength == 11:
            self.number = self.number[1:]

        self.area_code = self.number[0:3]
        self.exchange_code = self.number[3:6]
        self.line_number = self.number[-4:]
        if int(self.area_code[0]) < 2 or int(self.exchange_code[0]) < 2:
            raise ValueError('Invalid phone number')

    def pretty(self):
        return f"({self.area_code}) {self.exchange_code}-{self.line_number}"
        