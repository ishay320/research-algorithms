from typing import List


def bounded_subset(lst:List, cap:int) -> List:
    '''
    for every loop generate the next number and yield the number if 
    the sum is less or equals to the cap
    '''
    max_size_bit = 2**len(lst)
 
    for out_loop in range(max_size_bit):
        results = []
        lst_sum = 0
        for in_loop in range(len(lst)):
            if((out_loop & (1 << in_loop)) > 0):
                results.append(lst[in_loop])
                lst_sum += lst[in_loop]

        if sum(results) > cap:
            continue

        yield results

if __name__ == "__main__":
    for i in bounded_subset([4, 1, 2, 3], 5):
        print(i)

