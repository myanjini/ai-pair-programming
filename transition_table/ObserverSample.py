from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class NewsPublisher:
    def __init__(self):
        self._subscribers = []
        self._latest_news = None

    def subscribe(self, subscriber: Observer):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)
            print(f"{subscriber.name}이(가) 구독을 시작했습니다.")

    def unsubscribe(self, subscriber: Observer):
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)
            print(f"{subscriber.name}이(가) 구독을 취소했습니다.")

    def notify_subscribers(self):
        print("새로운 뉴스가 게시되었습니다. 구독자들에게 알림을 전송합니다.")
        for subscriber in self._subscribers:
            subscriber.update(self._latest_news)

    def add_news(self, news: str):
        self._latest_news = news
        self.notify_subscribers()

class Subscriber(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str):
        print(f"{self.name}이(가) 새로운 뉴스를 받았습니다: {message}")


if __name__ == "__main__":
    # 주제 생성
    news_publisher = NewsPublisher()

    # 옵저버 생성
    subscriber1 = Subscriber("Alice")
    subscriber2 = Subscriber("Bob")
    subscriber3 = Subscriber("Charlie")

    # 옵저버 구독
    news_publisher.subscribe(subscriber1)
    news_publisher.subscribe(subscriber2)

    # 뉴스 추가 및 알림
    news_publisher.add_news("오늘의 날씨는 맑음입니다.")

    print("\nBob이 구독을 취소합니다.\n")
    # 옵저버 구독 취소
    news_publisher.unsubscribe(subscriber2)

    # 또 다른 뉴스 추가 및 알림
    news_publisher.add_news("주식시장이 상승세를 보이고 있습니다.")

    print("\nCharlie가 구독을 시작합니다.\n")
    # 새로운 옵저버 구독
    news_publisher.subscribe(subscriber3)

    # 추가 뉴스
    news_publisher.add_news("새로운 스마트폰이 출시되었습니다.")
