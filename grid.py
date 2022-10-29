# 그리디 문제 예제 거스름돈 문제
# 거슬러 줘야할 돈은 10의 배수이므로 못 거슬러줄 경우 없음
#  가장 큰 화폐단위 부터  500,100,50,10
# 예제 1260원 
from calendar import c


n=1260
count=0
# 큰 단위의 화폐부터 차례대로 확인하기 위한 리스트를 만들어 준다
array=[500,100,50,10]
for coin in array:
    count+=n//coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n%=coin #코인으로 나눈 나머지 값 
print(count)

# 어떠한 수 N이 1이 될 때까지
# 1<=N<100000 과 2<=K<=100000가 공백을 기준으로 하여 각각 자연수 
# 첫째 줄에 N이 1이 될 때까지 1번 혹은 2본의 과정을 수행해야 하는 횟수외 최솟값 
# 주어진 N에 대하여 최대한 많이 나누기 수행
n,k= map(int,input().split())
result=0
while True:
    target=(n//k)*k
    result+=(n-target)
    n=target
    if n<k:
        break
    result+=1
    n//=k

result+=(n-1)
print(result)
