"""
https://www.acmicpc.net/problem/2231
소요시간: 1852ms

문제는 풀었지만 소요시간이 긴 이슈가 있음.
분해합을 계산하는 함수가 복잡한 것 같은데, 파이썬의 구조를 좀 더 공부할 필요가 있어보임.
"""



N = int(input())

selected_num = 0 # 선택된 숫자. 조건에 맞는 숫자가 없을 경우 0을 출력하므로 0으로 세팅.

for num in range(1, N):
    digits_of_num = []
    temp = num

    while num != 0:
        digits_of_num.append(num % 10)
        num = int(num / 10)

    sum_of_num = temp + sum(digits_of_num)

    if sum_of_num == N:
        selected_num = temp
        break

print(selected_num)