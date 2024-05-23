import sys
def calccharge(user_money):
    '''お釣りを出力する'''
    chargelist = [[5000,0], [1000,0], [500,0], [100,0], [50,0], [10,0]]
    #お釣りの枚数計算
    for i in range(len(chargelist)):
       while user_money >= chargelist[i][0]:
           user_money -= chargelist[i][0]
           chargelist[i][1] += 1
    #お釣りの出力
    print("おつり")
    for i in range(len(chargelist)):
        if i <= 1:
            print(f"{chargelist[i][0]}円札：{chargelist[i][1]}枚")
        else:
            print(f"{chargelist[i][0]}円玉：{chargelist[i][1]}枚")
    

def vertification_usermoney(min_price):
    '''金額の投入と投入金額のチェック'''
    user_money = int(input("投入金額を入力してください\n")) #金額の入力
    ##①10000を超えるとき②購入金額以下のとき③1の位が0でないとき
    error1 = (user_money > 10000)
    error2 = (user_money < min_price)
    error3 = (str(user_money)[-1] != "0")
    ##投入金額を受け付けない時の処理
    while error1 or error2 or error3:
        if error1:
            user_money = input("10000円を超える金額は投入できません。再度投入金額を入力してください\n")
        elif error2:
            user_money = input(f"{user_money}円では購入できる商品がありません。再度投入金額を入力してください\n")
        elif error3:
            user_money = input("1円玉、5円玉は使用できません。再度投入金額を入力してください\n")
    return user_money

def vertification_purchase_item(user_money,item_list):
    '''購入商品の入力と入力のチェック'''
    print("以下の商品が購入できます")
    ableitem_list = {}
    for i in item_list.keys():
        if user_money > item_list[i]:
            ableitem_list.append({i:item_list[i]})
            print(f"{i}：{item_list[i]}円")
    purchase_item = input("何を購入しますか？\n")
    count_True = 0
    for i in range(len(item_list)):
        if purchase_item == list(item_list.keys())[i]:
            count_True += 1 
    while count_True == 0:
        purchase_item = input("陳列されている商品名を入力してください。何を購入しますか？\n")
        for i in range(len(item_list)):
            if purchase_item == list(item_list.keys())[i]:
                count_True += 1
    return purchase_item 

def vertification_continue(user_money,min_price,item_list,purchase_item):
    '''残金に対する処理'''
    #残金の計算
    user_money -= item_list[purchase_item]
    if user_money < min_price: ##残金が商品より少ないとき
        calccharge(user_money)
        sys.exit()
    elif user_money == 0: ##残金0円のとき
        sys.exit()
    print(f"残金：{user_money}円")
    choice_continue = input("続けて購入しますか（Y/N）\n")
    while not(choice_continue == "Y" or choice_continue == "N"):
        choice_continue = input("YまたはNを入力してください\n") 
        if choice_continue == "Y":
            vertification_purchase_item(user_money,item_list)
        elif choice_continue == "N":
            calccharge(user_money)
