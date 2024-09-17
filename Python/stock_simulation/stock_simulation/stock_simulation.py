from util import company_lists, plot_line_graph
from random import random
import os 
from collections import defaultdict

class Stock:
    HISTORY_DIR = 'stock_history'
    def __init__(self, name):
        self.name = name 
        self.initial_price = 10000
        self.price_history = [10000]
        self.momentum = 0
        self.momentum_upper_bound = max(abs(random()-0.5), 0.5)
        self.momentum_lower_bound = -max(abs(random()-0.5), 0.5)
        self.price = self.initial_price

    def __hash__(self):
        return hash(self.name)
    
    def step(self, market):
        if random() < 0.05:
            self.price = self.price * 1.10
        elif random() > 0.95:
            self.price = self.price * 0.80
        else:
            self.momentum += (random() - 0.5) * 0.1 #+ self.momentum
            if self.momentum_upper_bound < self.momentum:
                self.momentum = self.momentum_lower_bound
            elif self.momentum_lower_bound > self.momentum:
                self.momentum = self.momentum_lower_bound
            delta = random() - 0.5 + self.momentum + market.momentum 
            self.price += self.momentum * self.price 
        self.price_history.append(self.price)

    def plot_history(self):
        if not os.path.exists(Stock.HISTORY_DIR):
            os.makedirs(Stock.HISTORY_DIR)
        
        plot_line_graph(self.price_history, save_to = f'stock_history/{self.name}.png', title = f'Price graph of {self.name}', x_label = 'time', y_label = '{self.name} price')
         

class StockMarket:
    def __init__(self, listed_stocks):
        self.listed_stocks = listed_stocks
        self.momentum = 0.01

    def step(self):
        for stock in self.listed_stocks:
            stock.step(self)

class Investor:
    def __init__(self, name = 'MJ', initial_asset = 10000000, strategy = lambda investor, market:None):
        self.name = name 
        self.asset = initial_asset
        self.cash = initial_asset 
        self.asset_history = [initial_asset]
        self.portfolio = defaultdict(float)
        self.strategy = strategy

    def buy(self, stock, amount):
        if self.cash - stock.price * amount >= 0:
            self.portfolio[stock] += amount
            self.cash -= stock.price * amount
        else:
            print('Out of money')

    def sell(self, stock, amount):
        if stock in self.portfolio and self.portfolio[stock] >= amount:
            self.portfolio[stock] -= amount 
            self.cash += stock.price * amount 
        else:
            print('Not enough stocks')

    def buy_or_sell(self, market):
        self.strategy(self, market)
        stock_asset = 0
        for stock, amount in self.portfolio.items():
            stock_asset += stock.price * amount
        self.asset = stock_asset + self.cash 
        self.asset_history.append(self.asset)

    def plot_history(self):
        plot_line_graph(self.asset_history, save_to = f'{self.name}.png', title = f'Asset History of {self.name}', x_label = 'time', y_label = '{self.name} Asset')

def simulate(strategy = lambda investor, market:None, n_steps = 100, n_company = 10):
    investor = Investor(strategy=strategy)
    stocks = []
    
    company_list = []

    if not os.path.exists(Stock.HISTORY_DIR):
        company_list = company_lists(n_company)
    else:
        company_list = [e.strip('.png') for e in os.listdir(Stock.HISTORY_DIR)]
        
        if len(company_list) > n_company:
            company_list = company_list[:n_company]
        else:
            company_list = company_list + company_lists(n_company - len(company_list))

    for name in company_list:
        stocks.append(Stock(name))

    market = StockMarket(stocks)

    for step in range(n_steps):
        market.step()
        investor.buy_or_sell(market)

    for stock in stocks:
        stock.plot_history()
    investor.plot_history()

def my_strategy(investor, market):

    # 자산의 1%만을 주식에 투자
    total_investment = investor.asset * 0.01
    
    for stock in market.listed_stocks:
        # 보유하고 있는 주식 수
        current_amount = investor.portfolio[stock]
        
        # 주식 가격이 상승할 때
        if stock.price > stock.initial_price * 1.2:
            # 가격이 상승했지만 너무 과도한 상승이 아닐 때만 매도
            if current_amount > 0:
                amount_to_sell = current_amount * 0.7  # 보유 주식의 50%를 매도
                investor.sell(stock, amount_to_sell)
        
        # 주식 가격이 하락할 때
        elif stock.price < stock.initial_price * 0.9:
            # 가격이 하락했지만 너무 과도한 하락이 아닐 때만 매수
            amount_to_buy = total_investment // stock.price
            if amount_to_buy > 0:
                investor.buy(stock, amount_to_buy)

    # # 모든 주식에 대해 반복
    # for stock in market.listed_stocks:
    #     # 주식 가격이 초기 가격보다 많이 상승했으면 매도
    #     if stock.price > stock.initial_price * 1.20:
    #         amount_to_sell = investor.portfolio[stock] * 0.5  
    #         # 현재 보유 주식의 50%를 매도
    #         investor.sell(stock, amount_to_sell)
        
    #     # 주식 가격이 초기 가격보다 많이 하락했으면 매수
    #     elif stock.price < stock.initial_price * 0.80:
    #         amount_to_buy = investor.cash // stock.price * 0.1  # 현금의 10%를 사용하여 매수
    #         investor.buy(stock, amount_to_buy)
    print(f'{investor.name} on market')

if __name__ == '__main__':
    simulate(strategy = my_strategy)
    

'''
주식 평가: 투자자가 보유한 주식의 현재 가치를 평가하고, 이를 바탕으로 구매 또는 판매 결정을 내리는 전략을 추가할 수 있습니다. 예를 들어, 가격이 일정 비율 이상 상승하면 판매하고, 일정 비율 이하로 하락하면 구매하는 식입니다.

포트폴리오 조정: 포트폴리오의 비율을 조정하는 전략을 구현할 수 있습니다. 예를 들어, 특정 주식이 너무 많거나 너무 적으면 조정할 수 있습니다.

시장 동향 분석: 시장 전체의 동향을 분석하여 투자 결정을 내릴 수 있습니다. 예를 들어, 시장의 모멘텀을 고려하여 특정 주식을 사거나 팔 수 있습니다.

리스크 관리: 손실을 최소화하기 위해 리스크 관리 전략을 추가할 수 있습니다. 예를 들어, 손절매를 설정하거나 포트폴리오의 다양화를 고려할 수 있습니다.
'''