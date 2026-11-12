n = int(input("숫자 n을 입력하세요:"))
total = 0
for i in range(1, n+1):
    total += i
print(f"1부터 {n}까지의 합: {total}")
