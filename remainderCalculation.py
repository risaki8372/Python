print("num1 -> 左の数 num2 -> 右の数")
print("num1 % num2 = 余りがあれば ng, 余らなければ ok")
print("数を入力してください。例：8 2")
def r(num1, num2): # num1 -> 左の数 num2 -> 右の数
    return "ng" if num1 % num2 else "ok" # num1 ÷ num2 = 余りがあれば "ng",     余らなければ "ok"  
  
num1, num2 = map(int, input().split()) # num1とnum2に整数を入れる、入ってい>    る数を読み込む。
  
result = r(num1, num2) # rの関数の結果をresultに入れる。
print(result) # resultの結果を出力。
