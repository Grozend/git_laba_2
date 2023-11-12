class Validator:

    def is_email(self, stri):
        for i in stri:
            if '@' in stri and '.' in stri:
                return 'Ваш Email: ' + stri
            else:
                return 'incorrect email'

    def is_domain(self, stri):
        if stri.isalpha():
            return 'correct domain'
        else:
            return 'incorrect domain'

    def is_number(self, stri):
        if stri.isdigit():
            return 'full number'
        else:
            return 'not full number'


valid = Validator()

print(valid.is_email('mybody@gmail.com'))
print(valid.is_domain('com'))
print(valid.is_number('12345'))