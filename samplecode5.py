x = 10

if x > 5:
    print("xは5より大きいです")
else:
    print("xは5以下です")

# xは5より大きいです

# サンプルコード2: 複数の条件
y = 7

if y < 5:
    print("yは5より小さいです")
elif y == 5:
    print("yはちょうど5です")
else:
    print("yは5より大きいです")
# yは5より大きいです

# サンプルコード3: 複数の条件と論理演算子の組み合わせ
z = 12

if z > 10 and z % 2 == 0:
    print("zは10より大きく、偶数です")
elif z > 10 and z % 2 != 0:
    print("zは10より大きく、奇数です")
else:
    print("zは10以下です")
# zは10より大きく、偶数です