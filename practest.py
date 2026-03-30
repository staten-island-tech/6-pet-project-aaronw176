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

def tree(heights):
    greater = 1
    less = 1
    greaterf = 0
    lessf = 0
    for i in range(1, len(heights)):
        if heights[i] > heights [i-1]:
            less = 1
            greater += 1
            if greater > greaterf:
                greaterf = greater
        
        if heights[i] < heights[i-1]:
            greater = 1
            less += 1
            if less > lessf:
                lessf = less
    print(greaterf)
    print(lessf)

tree([1,3,4,2,1,4,6,8,2,3,4,2,1,0])