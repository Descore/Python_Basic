
def tpl_sort(nums_in):

    nums_list = list(nums_in)
    for i in nums_list:
        if int(i) != float(i):
            return nums_in
    nums_list.sort()
    nums_tuple = tuple(nums_list)
    return nums_tuple


print(tpl_sort((6, 3, -1, 8, 4, 10, 5)))
