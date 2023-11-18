# https://www.acmicpc.net/problem/2798

N, M = map(int, input().split())
card_list = list(map(int, input().split()))

value_difference = M
sum_of_blackjack = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_of_card = card_list[i] + card_list[j] + card_list[k]
            if sum_of_card > M:
                continue
            else:
                if M - sum_of_card < value_difference:
                    value_difference = M - sum_of_card
                    sum_of_blackjack = sum_of_card

print(sum_of_blackjack)

