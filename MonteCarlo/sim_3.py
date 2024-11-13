import matplotlib.pyplot as plt
import random as rand

global broke_people
global profited_people
global profit_amount
global step_list
global norm_list
broke_people = 0
profited_people = 0
profit_amount = []
step_list = []
norm_list = []

def game(roll_over):
    roll = rand.randint(1,100)
    if roll < roll_over:
        return False
    if roll >= roll_over:
        return True
    
def strat(pot,initial_bet, numof_bets,roll_over,step):
    global broke_people
    global profited_people
    global profit_amount
    money = []
    bet_num = []
    multiplier = 99/(100-roll_over)
    initial_pot = pot
    bet = initial_bet
    for i in range(1,(numof_bets+1)):
        profit = (bet*multiplier) - bet
        if game(roll_over):
            pot+=profit
            if pot > 0:
                bet = initial_bet
            else:
                pot = 0
                money.append(pot)
                bet_num.append(i)
                broke_people += 1
                break
        else:
            pot-=bet
            if pot > 0: 
                bet*=step
            else:
                pot = 0
                money.append(pot)
                bet_num.append(i)
                broke_people += 1
                break
        money.append(pot)
        bet_num.append(i)
    if pot > initial_pot:
        profited_people += 1
        profit_amount.append((pot-initial_pot))
    #plt.plot(bet_num,money)

def strat_statistics(num_people,step,pot):
    global broke_people
    global profited_people
    global profit_amount
    global step_list
    global norm_list
    total_profit = 0
    broke_percentage = (broke_people/num_people)*100
    profit_percentage = (profited_people/num_people)*100
    for profit in profit_amount:
        total_profit+=profit
    if profit_percentage != 0:
        mean_profit = total_profit/profited_people
    else:
        mean_profit = 0
    norm = ((profit_percentage/100)*mean_profit)-((broke_percentage/100)*pot)
    norm_list.append(norm)
    step_list.append(step)
    plt.plot(step_list,norm_list)
    print("{} percentage of people went broke".format(broke_percentage))
    print("{} percentage of people made a profit with a mean profit of {}".format(profit_percentage,mean_profit))
    broke_people = 0
    profited_people = 0
    profit_amount.clear()
def main():
    num_people = 1000
    pot = 10000
    intial_bet = 10
    numof_bets = 5
    roll_over = 50
    for step in range(1,11):
        for i in range(num_people):
            #def strat(pot,initial_bet, numof_bets,roll_over,step):
            strat(pot,intial_bet,numof_bets,roll_over,step)
        strat_statistics(num_people,step,pot)
    plt.xlabel('step')
    plt.ylabel('betting norm')
    plt.show()

if __name__ == "__main__":
    main()