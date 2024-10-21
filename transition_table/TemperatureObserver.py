class Observer:
    def update(self, temperature):
        raise NotImplementedError("Subclasses must implement this method")

class HighTemperatureObserver(Observer):
    def update(self, temperature):
        if temperature >= 50:
            print("고온 상태: 냉각 시스템 가동")

class NormalTemperatureObserver(Observer):
    def update(self, temperature):
        if 30 < temperature < 50:
            print("정상 상태: 시스템 정상 작동")

class LowTemperatureObserver(Observer):
    def update(self, temperature):
        if temperature <= 30:
            print("저온 상태: 난방 시스템 가동")

class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, temperature):
        for observer in self._observers:
            observer.update(temperature)

class TemperatureSensor(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = None

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify_observers(temperature)

# 사용 예시
sensor = TemperatureSensor()
sensor.add_observer(HighTemperatureObserver())
sensor.add_observer(NormalTemperatureObserver())
sensor.add_observer(LowTemperatureObserver())

temperatures = [25, 35, 55, 45, 20]

for temp in temperatures:
    print(f"현재 온도: {temp}도")
    sensor.set_temperature(temp)
    print()