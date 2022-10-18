
def slicer(text_in, num_in):
    num_list = []
    for i, v in enumerate(text_in):
        if v == num_in:
            num_list.append(text_in[i])
            for y in range(i+1, len(text_in)):
                num_list.append(text_in[y])
                if num_in == text_in[y]:
                    break
            break
    num_tuple = tuple(num_list)
    return num_tuple
