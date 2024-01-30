def maximize_product_of_trees(n, F):
    max_value = max(F[0], F[1])
    min_value = min(F[0], F[1])
    max_negative = min_value if min_value < 0 else None
    min_positive = max_value if max_value > 0 else None

    for i in range(2, n):
        if F[i] >= max_value:
            min_value = max_value
            max_value = F[i]
        elif F[i] < min_value:
            min_value = F[i]

        if F[i] < 0 and (max_negative is None or F[i] < max_negative):
            max_negative = F[i]
        elif F[i] > 0 and (min_positive is None or F[i] > min_positive):
            min_positive = F[i]

    if max_negative is not None and min_positive is not None:
        return max_value * max_negative if max_value * max_negative > max_value * min_value else max_value * min_positive
    else:
        return max_value * min_value

# 예시 입력
n = 3
F = [5, -1, 4]

result = maximize_product_of_trees(n, F)
print("나무를 심을 위치의 최대 Fa*Fb 값:", result)