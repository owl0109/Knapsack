
# 変数の宣言
result_size = []
result_price = []
total_size = 0
total_price = 0
combi = []

#物の重さ、価値
size = [10, 12, 7, 9, 21, 16]
price = [120, 130, 80, 100, 250, 185]

# 要領
capacity = 65

# 重さ当たりの値段を算出
price_per_size = [j/i for(i,j)in zip(size,price)]

# 重さ当たりの値段,重さ,値段を2次元リストにする
table = [price_per_size,size,price]

# リストの列,行を入れ替え
table_t = [list(x) for x in zip(*table)]

# 重さ当たりの値段を使って降順にソートする
table_t.sort(reverse= True)

# リストの列,行を元に戻す
table_s = [list(x) for x in zip(*table_t)]

# 重さあたりの値段の大きい順にループする
for i,j,k in zip(table_s[0],table_s[1],table_s[2]):
    if total_size + j <= capacity:
        total_size += j
        total_price += k
        result_size.append(j)
        result_price.append(k)
        combi.append(j)

# 結果の表示

print("=====貪欲法=====")
print("合計が最大になる組み合わせ")
print(combi)
print("合計価格: ", total_price)
print("合計サイズ: ", total_size)
print()

