class Category:
    def __init__(self,name):
        self.name=name
        self.balance=0
        self.ledger=[]
    def __str__(self):
        calc=(30-len(self.name))//2
        toprint='*'*calc+self.name+'*'*calc+'\n'
        for ext in self.ledger:
            desc=ext['description']
            amount=ext['amount']
            if len(desc)>23:
                desc=desc[:23]
            calc=30-len(desc)-len(f'{amount:.2f}')
            toprint+=f'{desc}'+calc*' '+f'{amount:.2f}\n'
        toprint+=f'Total: {self.balance}'
        return toprint
    def check_funds(self,amount):
        if amount>self.balance:
            return False
        else: return True
    def deposit(self,amount,desc=''):
        self.ledger.append({'amount': amount, 'description': desc})
        self.balance+=amount
    def withdraw(self,amount,desc=''):
        self.ledger.append({'amount': -amount, 'description': desc})
        if self.check_funds(amount):
            self.balance-=amount
            return True
        else: return False
    def get_balance(self):
        return self.balance
    def transfer(self,amount,target):
        flag=0
        if self.withdraw(amount,f'Transfer to {target.name}'):
            target.deposit(amount, f'Transfer from {self.name}')
            flag=1
        if flag:
            return True
        else :return False
    def get_spent(self):
        return self.ledger[0]['amount']-self.balance

def create_spend_chart(categories):
    chart=[]
    total=0
    for obj in categories:
        total+=obj.get_spent()
    maxlen=0
    for obj in categories:
        maxlen=max(maxlen,len(obj.name))
        chart.append((obj.name,int(obj.get_spent()/total*10)))
    toprint='Percentage spent by category\n'
    for i in range(10,-1,-1):
        temp=(str(i) if i==10 else ' '+str(i))+'0| '
        if i==0:
            temp='  0| '
        for j in chart:
            if j[1] >= i:
                temp+='o  '
            else: temp+='   '
        toprint+=temp+'\n'
    bar='    -'+len(categories)*'---'
    toprint+=bar+'\n'
    for i in range(maxlen):
        temp=' '*5
        for j in chart:
            try:
                temp+=j[0][i]+'  '
            except IndexError:
                temp+='   '
        toprint+=temp+'\n'
    return toprint.strip('\n')
    





if __name__=='__main__':
    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    clothing.withdraw(10)
    print(food) 
    print(clothing)
    print(create_spend_chart([food,clothing]))
