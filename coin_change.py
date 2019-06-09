import numpy as np

def read_data(path):

    with open(path) as input_data:
        temp = [line.strip() for line in input_data]
    integer = int(temp[0])
    integer_list = temp[1]
    integer_list = integer_list.split(',')
    integer_list = [int(c) for c in integer_list]
    return integer, integer_list


def compute_min_coins(money, coins):

    t = np.zeros((len(coins), money+1))
    for index0 in range(t.shape[1]):
        t[0][index0] = index0
    for index1 in range(1, t.shape[0]):
        for index2 in range(t.shape[1]):
            if index2 >= coins[index1]:
                t[index1][index2] = min(t[index1-1][index2], t[index1][index2 - coins[index1]]+1)
            else:
                t[index1][index2] = t[index1 - 1][index2]
    return t

input_money = int(input("Please enter value of money :"))
input_coins = input("Please enter array of positiver integer coins :")
input_coins = input_coins.split(',')
input_coins = [int(c) for c in input_coins]

t_test3 = compute_min_coins(input_money, input_coins)
print('The minimum number of coins ' + str(input_coins) + ' to make the change ' +
      str(input_money) + ' is: ' + str(int(t_test3[-1][-1])))

