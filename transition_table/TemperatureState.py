class State:
    def handle(self, context, temperature):
        raise NotImplementedError("Subclasses must implement this method")

class HighTemperatureState(State):
    def handle(self, context, temperature):
        if temperature < 50:
            context.set_state(NormalTemperatureState())
        print("고온 상태: 냉각 시스템 가동")

class NormalTemperatureState(State):
    def handle(self, context, temperature):
        if temperature >= 50:
            context.set_state(HighTemperatureState())
        elif temperature <= 30:
            context.set_state(LowTemperatureState())
        print("정상 상태: 시스템 정상 작동")

class LowTemperatureState(State):
    def handle(self, context, temperature):
        if temperature > 30:
            context.set_state(NormalTemperatureState())
        print("저온 상태: 난방 시스템 가동")

class Context:
    def __init__(self):
        self.state = NormalTemperatureState()

    def set_state(self, state):
        self.state = state

    def request(self, temperature):
        self.state.handle(self, temperature)

# 사용 예시
context = Context()
temperatures = [25, 35, 55, 45, 20]

for temp in temperatures:
    print(f"현재 온도: {temp}도")
    context.request(temp)
    print()