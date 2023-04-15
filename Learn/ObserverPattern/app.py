#!/usr/bin/python3.5

from observable import Observable

from Learn.ObserverPattern.observer import Observer


class AmericanStockMarket(Observer):
    def update(self, *args, **kwargs):
        print('American Stock Market received: ', args, kwargs)


class EuropeanStockMarket(Observer):
    def update(self, *args, **kwargs):
        print('European Stock Market received : ', args, kwargs)


if __name__ == '__main__':
    observable = Observable()

    american_observer = AmericanStockMarket()
    observable.register(american_observer)

    european_observer = EuropeanStockMarket()
    observable.register(european_observer)

    observable.update_observers('Market Rally', something='Hello World')