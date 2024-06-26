# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

scores = [1, 3, 3, 3, 4]


def change_scores(scores, index=0, max_scores=max(scores), min_scores=min(scores)):
    if index < len(scores):
        if scores[index] == max_scores:
            scores[index] = min_scores
        change_scores(scores, index + 1)
        return scores


print(*change_scores(scores))


# change_scores(scores)
# print(*scores)
