# 挿入ソート
# 以下のURLを参考
# https://qiita.com/drken/items/44c60118ab3703f7727f

# 前から順番に、i番目の要素を適切な場所へ挿入することを繰り返す単純なソート
# 平均計算量: O(n**2)
# 最悪計算量: O(n**2)

def insertion_sort(n, a):
    for i in range(1, n):
        # 目的の値を挿入する適切な場所を探す
        for j in reversed(range(i)):
            if a[j] > a[j+1]:
                # 目的の値の値のほうが大きかった場合交換する
                a[j], a[j+1] = a[j+1], a[j]
            else:
                break

# n = int(input())
# a = [int(input()) for _ in range(n)]
a = [12, 9, 15, 3, 8, 17, 6, 1]
n = len(a)
print("before")
print(a)
print("---------")
insertion_sort(n, a)
print("after")
print(a)

