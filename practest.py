def sum(emerald,weight):
    sum_weight = 0
    max_weight = []
    for i in weight:
        if i%2 == 0:
            sum_weight += i
            max_weight.append(sum_weight)
        else:
            sum_weight = 0
    print(f"{max(max_weight)}")
sum(13, [2, 3, 4, 4, 5, 6, 1, 2, 2, 2, 1, 8, 2])