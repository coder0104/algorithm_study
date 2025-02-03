#거스름돈 문제(1260원을 500, 100, 50, 10원으로 거스를 수 있는 동전의 최소 개수)
n = 1260
count = 0

coin_array = [500, 100, 50, 10]

for coin in coin_array:
  count += n // coin
  n %= coin

print(count)
#시간복잡도 O(k)

#이코테 그리디 문제 2번 곱하기 혹은 더하기
s = int(input())
print(s)