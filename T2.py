list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

i, j = 0, 0
merged_list = []

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        if not merged_list or merged_list[-1] != list1[i]:
            merged_list.append(list1[i])
        i += 1
    elif list1[i] > list2[j]:
        if not merged_list or merged_list[-1] != list2[j]:
            merged_list.append(list2[j])
        j += 1
    else:
        if not merged_list or merged_list[-1] != list1[i]:
            merged_list.append(list1[i])
        i += 1
        j += 1
        
while i < len(list1):
    if not merged_list or merged_list[-1] != list1[i]:
        merged_list.append(list1[i])
    i += 1

while j < len(list2):
    if not merged_list or merged_list[-1] != list2[j]:
        merged_list.append(list2[j])
    j += 1

print(" ".join(map(str, merged_list)))
