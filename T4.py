from collections import deque

def validate_structure(num, entry_order, exit_order): 
    stack_list = []
    is_stack_valid = True
    entry_pointer = 0
    for elem in exit_order:
        while entry_pointer < num and (not stack_list or stack_list[-1] != elem):
            stack_list.append(entry_order[entry_pointer])
            entry_pointer += 1
        if stack_list and stack_list[-1] == elem:
            stack_list.pop()
        else:
            is_stack_valid = False
            break
    
    queue_container = deque()
    is_queue_valid = True
    entry_pointer = 0
    for elem in exit_order:
        while entry_pointer < num and len(queue_container) < num:
            queue_container.append(entry_order[entry_pointer])
            entry_pointer += 1
        if queue_container and queue_container[0] == elem:
            queue_container.popleft()
        else:
            is_queue_valid = False
            break

    if is_stack_valid and is_queue_valid:
        return "both"
    elif is_stack_valid:
        return "stack"
    elif is_queue_valid:
        return "queue"
    else:
        return "neither"

num_elements = int(input())
elements_entering = list(map(int, input().split()))
elements_leaving = list(map(int, input().split()))

validation_result = validate_structure(num_elements, elements_entering, elements_leaving)
print(validation_result)