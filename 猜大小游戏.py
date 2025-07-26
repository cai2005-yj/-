import random

def roll_dice(numbers=3,points=None):
    print("roll dice")
    if points is None:
        points=[]
    while numbers>0:
        point=random.randrange(1,7)
        points.append(point)
        numbers=numbers-1
    return points
def roll_result(total):
    isBig=11<=total<=18
    isSmall=3<=total<=10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'
def start_game():
    amount=1000
    while amount>0:
     print("你押多少：")
     yajin = int(input())
     print("游戏开始")
     choices = ['Big', 'Small']
     your_choices = input("Big or Small:")
     if your_choices in choices:
        points=roll_dice()
        total=sum(points)
        youwin=your_choices==roll_result(total)
        if youwin:
            print('The points are',points,'you win')
            amount=amount+yajin
        else:
            print("The points are",points,'you lose')
            amount=amount-yajin
        print('现在的金额：'+str(amount))
    while amount<=0:
        print("游戏结束")
        break
start_game()