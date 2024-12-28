def merge_two_sorted_lists(list1, list2):
    result = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result

def merge_sort_first_round(arr):
    subarrays = [[x] for x in arr]
    
    result = []
    for i in range(0, len(subarrays), 2):
        if i + 1 < len(subarrays):
            result.append(merge_two_sorted_lists(subarrays[i], subarrays[i+1]))
        else:
            result.append(subarrays[i])
    
    return [item for sublist in result for item in sublist]

def main():
    arr = list(map(int, input().split()))
    result = merge_sort_first_round(arr)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
