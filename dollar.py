class MoneyFmt:
    def __init__(self,akcha):
        self.akcha = akcha

    def update(self,akcha):
        self.akcha = akcha

    def __repr__(self):
        return f'{self.akcha}'


    def dollarize(self):
        if self.akcha >= 0:
            return '${:,.2f}'.format(self.akcha)
        else:
            return '-${:,.2f}'.format(self.akcha)

    def __str__(self):
        return f'Кароче меняем число на баксы {self.akcha}, ${self.akcha}'
        

cash = MoneyFmt(12345678.021)
print(cash.dollarize())
cash.update(100000.4567)
print(cash.dollarize())
cash.update(-0.3)
print(cash.dollarize())
print(repr(cash))
print(cash)