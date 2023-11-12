import re


class Text:
    def __init__(self, text):
        self.text = text

    def count_sim(self):
        count_sim = 0
        for i in self.text:
            count_sim += 1
        return count_sim

    def count_bukv(self):
        count_bukv = 0
        for i in self.text:
            if i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                count_bukv += 1
        return count_bukv

    def count_space(self):
        count_space = 0
        for i in self.text:
            if i == ' ':
                count_space += 1
        return count_space

    def count_sim_not_space(self):
        count_sim_not_space = 0
        for i in self.text:
            if i != ' ':
                count_sim_not_space += 1
        return count_sim_not_space

    def mass_words(self):
        mass = self.text.split()
        return mass

    def mass_predl(self):
        return re.split('!.?', self.text)


text = Text('Я видел сон!! и знаешь ты.')

print(text.count_sim())
print(text.count_bukv())
print(text.count_space())
print(text.count_sim_not_space())
print(text.mass_words())
print(text.mass_predl())