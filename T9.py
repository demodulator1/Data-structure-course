def search_optimal_moves(end_x, end_y, current_pos_x, current_pos_y, left_turns, right_turns):
    if current_pos_x == end_x and current_pos_y == end_y:
        return left_turns, right_turns

    optimal_moves = None

    if current_pos_x + current_pos_y <= end_x * 2 and current_pos_y <= end_y:
        left_moves = search_optimal_moves(end_x, end_y, current_pos_x + current_pos_y, current_pos_y, left_turns + 1, right_turns)
        if optimal_moves is None or (left_moves is not None and left_moves[0] + left_moves[1] < optimal_moves[0] + optimal_moves[1]):
            optimal_moves = left_moves

    if current_pos_x <= end_x and current_pos_x + current_pos_y <= end_y * 2:
        right_moves = search_optimal_moves(end_x, end_y, current_pos_x, current_pos_x + current_pos_y, left_turns, right_turns + 1)
        if optimal_moves is None or (right_moves is not None and right_moves[0] + right_moves[1] < optimal_moves[0] + optimal_moves[1]):
            optimal_moves = right_moves

    return optimal_moves


destination_x, destination_y = map(int, input().split())
path_result = search_optimal_moves(destination_x, destination_y, 1, 1, 0, 0)
if path_result:
    print(path_result[0], path_result[1])
else:
    print("No path found")