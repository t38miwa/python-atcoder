def remove_vowels(S):
    vowels = "aeiou"
    result = ''.join([char for char in S if char not in vowels])
    return result

# 入力を受け取り、関数を呼び出して結果を出力
S = input().strip()
print(remove_vowels(S))
