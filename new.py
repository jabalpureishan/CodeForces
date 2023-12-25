# from itertools import chain, combinations

# def subsets(arr):
#     return chain(*[combinations(arr,i + 1) for i,a in enumerate(arr)])

# def k_subset(arr, k):
#     s_arr = sorted(arr)
#     return set([frozenset(i) for i in combinations(subsets(arr),k) 
#                if sorted(chain(*i)) == s_arr])

# ans = k_subset(arr,k)
# Min = 10000000
# for i in ans:
#     i = list(i)
#     temp = []
#     for j in i:
#         temp.extend(j)
#     #print(i)
#     if temp==arr:
#         total = 0
#         print(i)
#         for j in i:
#             total += j[0] + j[-1]
#         Min = min(Min,total)

# print(Min)
arr = [8,9,8,2,9,9,2]
k = 3
def k_subset(s, k):
    if k == len(s):
        return (tuple([(x,) for x in s]),)
    k_subs = []
    for i in range(len(s)):
        partials = k_subset(s[:i] + s[i + 1:], k)
        for partial in partials:
            for p in range(len(partial)):
                k_subs.append(partial[:p] + (partial[p] + (s[i],),) + partial[p + 1:])
    return k_subs

print(k_subset(arr,k))



