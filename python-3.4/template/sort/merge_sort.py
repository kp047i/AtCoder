# マージソート
# 以下のURLを参考
# https://qiita.com/drken/items/44c60118ab3703f7727f

# 左半分と右半分に分割し、さらにそれぞれを分割とマージを繰り返して
# 最後に左半分と右半分をソートしたものをマージする
# 平均計算量: O(nlogn)
# 最悪計算量: O(nlogn)
# メモリを多く使用してしまう

def merge_sort():
    

a = [12, 9, 15, 3, 8, 17, 6, 1]
n = len(a)
print("before")
print(a)
print("---------")
merge_sort(n, a)
print("after")
print(a)
