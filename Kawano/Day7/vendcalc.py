#初期設定
import sys
import vendcalc_import
##商品リスト作成
item_list = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}
min_price = min(list(item_list.values()))
print(min_price)
#販売商品の羅列
for item in item_list:
    print(f"{item}：{item_list[item]}円")
#金額投入
user_money = vendcalc_import.vertification_usermoney(min_price)
#購入商品入力
purchase_item = vendcalc_import.vertification_purchase_item(user_money,item_list)



    

