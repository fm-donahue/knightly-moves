rows, cols = (8,8)
arr = []

row_move = [-2, -1, 1, 2, -2, -1, 1, 2]
col_move = [-1, -2, -2, -1, 1, 2, 2, 1]

r_queue = []
c_queue = []

visited = {}
tracker = {}
path = []

def solution(src, dest):
    global rows, cols, arr
    num_of_cell = 0
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(num_of_cell)
            if num_of_cell == src:
                src_row, src_col = i, j
            num_of_cell += 1
        arr.append(col)
        
    return solve(dest, src_row, src_col)

def explore_neighbors(row, col):
    global rows, cols, row_move, col_move, visited, arr
    steps = visited[arr[row][col]]
    for r, c in zip(row_move, col_move):
        r_move = row + r
        c_move = col + c
        if r_move < 0 or c_move < 0:
            continue
        if r_move >= rows or c_move >= cols:
            continue
        if arr[r_move][c_move] in visited:
            continue
        r_queue.append(r_move)
        c_queue.append(c_move)
        visited[arr[r_move][c_move]] = steps + 1
        tracker[arr[r_move][c_move]] = arr[row][col]

    return

def back_track(node):
    path.append(node)
    while True:
        path.append(tracker[node])
        node = tracker[node]
        if node not in tracker:
            break
    return

def solve(dest, src_row, src_col):
    global r_queue, c_queue, arr
    r_queue.append(src_row)
    c_queue.append(src_col)

    while r_queue != []:
        row = r_queue.pop(0)
        col = c_queue.pop(0)
        if dest in visited:
            if len(visited) == 1:
                return
            back_track(dest)
            return
        explore_neighbors(row, col)

source = 56
dest = 13
visited[source] = 0
solution(source,dest)
print(visited[dest])
print('->'.join(map(str, path[::-1])))
