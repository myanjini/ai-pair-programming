from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def insert_coin(self, vending_machine, amount):
        pass

    @abstractmethod
    def select_product(self, vending_machine, product):
        pass

    @abstractmethod
    def receive_product(self, vending_machine):
        pass

    @abstractmethod
    def receive_change(self, vending_machine):
        pass

    @abstractmethod
    def press_return_button(self, vending_machine):
        pass

    @abstractmethod
    def receive_returned_amount(self, vending_machine):
        pass

class InitialState(State):
    def insert_coin(self, vending_machine, amount):
        vending_machine.total_amount += amount
        vending_machine.set_state(vending_machine.receiving_amount_state)
        print(f"동전을 받았습니다. 현재 합계 금액: {vending_machine.total_amount}원")

    def select_product(self, vending_machine, product):
        print("동전을 먼저 넣어주세요.")

    def receive_product(self, vending_machine):
        print("동전을 먼저 넣어주세요.")

    def receive_change(self, vending_machine):
        print("동전을 먼저 넣어주세요.")

    def press_return_button(self, vending_machine):
        print("동전을 먼저 넣어주세요.")

    def receive_returned_amount(self, vending_machine):
        print("동전을 먼저 넣어주세요.")

class ReceivingAmountState(State):
    def insert_coin(self, vending_machine, amount):
        vending_machine.total_amount += amount
        print(f"동전을 받았습니다. 현재 합계 금액: {vending_machine.total_amount}원")

    def select_product(self, vending_machine, product):
        if product in vending_machine.inventory:
            product_price = vending_machine.inventory[product]['price']
            if vending_machine.total_amount >= product_price:
                if vending_machine.inventory[product]['stock'] > 0:
                    vending_machine.inventory[product]['stock'] -= 1
                    vending_machine.set_state(vending_machine.dispensing_product_state)
                    print(f"{product}을(를) 제공하고 있습니다.")
                else:
                    print("선택한 상품의 재고가 없습니다.")
            else:
                print("금액이 부족합니다.")
        else:
            print("존재하지 않는 상품입니다.")

    def receive_product(self, vending_machine):
        print("상품을 선택해 주세요.")

    def receive_change(self, vending_machine):
        print("상품을 선택해 주세요.")

    def press_return_button(self, vending_machine):
        vending_machine.set_state(vending_machine.processing_return_state)
        print("반환금을 계산하고 있습니다.")

    def receive_returned_amount(self, vending_machine):
        print("반환 버튼을 먼저 눌러주세요.")

class DispensingProductState(State):
    def insert_coin(self, vending_machine, amount):
        print("상품을 제공 중입니다. 잠시만 기다려주세요.")

    def select_product(self, vending_machine, product):
        print("상품을 제공 중입니다. 잠시만 기다려주세요.")

    def receive_product(self, vending_machine):
        vending_machine.set_state(vending_machine.returning_change_state)
        print("상품을 받았습니다. 거스름돈을 반환합니다.")

    def receive_change(self, vending_machine):
        print("상품을 먼저 받아주세요.")

    def press_return_button(self, vending_machine):
        print("상품을 먼저 받아주세요.")

    def receive_returned_amount(self, vending_machine):
        print("상품을 먼저 받아주세요.")

class ReturningChangeState(State):
    def insert_coin(self, vending_machine, amount):
        print("거스름돈을 반환 중입니다. 잠시만 기다려주세요.")

    def select_product(self, vending_machine, product):
        print("거스름돈을 반환 중입니다. 잠시만 기다려주세요.")

    def receive_product(self, vending_machine):
        print("거스름돈을 반환 중입니다. 잠시만 기다려주세요.")

    def receive_change(self, vending_machine):
        vending_machine.set_state(vending_machine.initial_state)
        vending_machine.total_amount = 0
        print("거스름돈을 받았습니다. 초기 상태로 돌아갑니다.")

    def press_return_button(self, vending_machine):
        print("거스름돈을 반환 중입니다. 잠시만 기다려주세요.")

    def receive_returned_amount(self, vending_machine):
        print("거스름돈을 반환 중입니다. 잠시만 기다려주세요.")

class ProcessingReturnState(State):
    def insert_coin(self, vending_machine, amount):
        print("반환금을 계산 중입니다. 잠시만 기다려주세요.")

    def select_product(self, vending_machine, product):
        print("반환금을 계산 중입니다. 잠시만 기다려주세요.")

    def receive_product(self, vending_machine):
        print("반환금을 계산 중입니다. 잠시만 기다려주세요.")

    def receive_change(self, vending_machine):
        print("반환금을 계산 중입니다. 잠시만 기다려주세요.")

    def press_return_button(self, vending_machine):
        print("반환금을 계산 중입니다. 잠시만 기다려주세요.")

    def receive_returned_amount(self, vending_machine):
        returned_amount = vending_machine.total_amount
        vending_machine.set_state(vending_machine.initial_state)
        vending_machine.total_amount = 0
        print(f"반환금 {returned_amount}원을 받았습니다. 초기 상태로 돌아갑니다.")

class VendingMachine:
    def __init__(self):
        self.initial_state = InitialState()
        self.receiving_amount_state = ReceivingAmountState()
        self.dispensing_product_state = DispensingProductState()
        self.returning_change_state = ReturningChangeState()
        self.processing_return_state = ProcessingReturnState()
        self.state = self.initial_state
        self.total_amount = 0
        self.inventory = {
            'item1': {'stock': 5, 'price': 100},
            'item2': {'stock': 5, 'price': 150}
        }

    def set_state(self, state):
        self.state = state

    def insert_coin(self, amount):
        self.state.insert_coin(self, amount)

    def select_product(self, product):
        self.state.select_product(self, product)

    def receive_product(self):
        self.state.receive_product(self)

    def receive_change(self):
        self.state.receive_change(self)

    def press_return_button(self):
        self.state.press_return_button(self)

    def receive_returned_amount(self):
        self.state.receive_returned_amount(self)

# 테스트 코드
def test_vending_machine():
    vm = VendingMachine()

    # 물품 금액 보다 적은 금액을 입력한 경우
    print("\n테스트 1: 물품 금액 보다 적은 금액을 입력한 경우")
    vm.insert_coin(50)
    vm.select_product('item1')

    # 물품 금액 보다 많은 금액을 입력한 경우
    print("\n테스트 2: 물품 금액 보다 많은 금액을 입력한 경우")
    vm.insert_coin(200)
    vm.select_product('item2')
    vm.receive_product()
    vm.receive_change()

    # 재고가 없는 물품을 선택한 경우
    print("\n테스트 3: 재고가 없는 물품을 선택한 경우")
    for _ in range(5):
        vm.insert_coin(100)
        vm.select_product('item1')
        vm.receive_product()
        vm.receive_change()
    vm.insert_coin(100)
    vm.select_product('item1')

    # 반환 버튼을 누른 경우
    print("\n테스트 4: 반환 버튼을 누른 경우")
    vm.insert_coin(100)
    vm.press_return_button()
    vm.receive_returned_amount()

test_vending_machine()