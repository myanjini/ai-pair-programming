from abc import ABC, abstractmethod

# 상태 인터페이스
class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

# 구체적인 상태 A
class ConcreteStateA(State):
    def handle(self, context):
        print("상태 A의 동작 수행")
        context.state = ConcreteStateB()  # 상태 B로 전환

# 구체적인 상태 B
class ConcreteStateB(State):
    def handle(self, context):
        print("상태 B의 동작 수행")
        context.state = ConcreteStateA()  # 상태 A로 전환

# Context 클래스
class Context:
    def __init__(self, state: State):
        self.state = state
    
    def request(self):
        self.state.handle(self)

# 상태 패턴 동작 예시
context = Context(ConcreteStateA())  # 처음에 상태 A로 시작
context.request()  # 상태 A에서 B로 전환
context.request()  # 상태 B에서 A로 전환
