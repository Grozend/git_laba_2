class Car:
    color = None  # цвет автомобиля
    fuel = None  # количество топлива
    marka = None
    korobka = None

    def go(self):
        # Команда ехать:
        pass

    def turn(self):
        # Команда поворачивать:
        pass

    def stop(self):
        # Команда остановиться:
        pass

    def vivod_color(self):
        print(myCar.color)

    def vivod_last_info(self):
        print(myCar.fuel)
        print(myCar.marka)
        print(myCar.korobka)


myCar = Car()
myCar.color = 'red'  # красим в красный цвет
myCar.fuel = 50    # заливаем топливо
myCar.marka = 'BMW'
myCar.korobka = 'avtomat'


myCar.go()
myCar.turn()
myCar.stop()
myCar.vivod_color()
myCar.vivod_last_info()