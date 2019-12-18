# you have data 
def selection_sort(l, compare_with):
    n = len(l)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if compare_with(l[j], l[min_idx]):
                min_idx = j
            # print(l[i], l[min_idx])
            l[i], l[min_idx] = l[min_idx] , l[i]


def less_than(a,b):
    return a > b

all_tuples = [(24,25), (11,13), (1,2), (3,5)]
def tuples_(a,b):
    return sum(a) < sum(b)


list = [4,5,6,7,32, 74, 9, 8]

print(list)
# selection_sort(list, less_than)
selection_sort(all_tuples, tuples_)
print(all_tuples)

print (list)
