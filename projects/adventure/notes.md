## Requirements
- start from scratch
- sequence of steps that explores all rooms in map (<2000)
- omni potent (no teleport)
    - does this mean recursion?
- no islands

## Thoughts
- need conditional to check if neighbouring rooms exist
    - if room doesn't exists, key[cardinal] = None, "N", "S", "E", "W"
    ```
    UNEXPLORED
            {
       key  0: {'n': '?', 's': 5, 'w': '?', 'e': '?'}
            }
    EXPLORED
            {
       key  0: {'n': 0, 's': 5, 'w': None, 'e': '2'}
            }
    ```
- need DFS with backtracking func
    - updates visited object
    - stack class
    - reduce steps taken compared to BFS
- iterate over key value object
- all paths need to be pushed onto traversal path
    - do these have to be completed?
- Back tracking keys
    - choice
     - if ? N, S, E, W, None
    - constraints
    - goal


```
for cardinal in visited[room]:
    if cardinal == "?":
        execute dfs
```

## Useful
- maze solving algos
    - log all paths, not just winning

## README
 1. picks a random unexplored direction from the player's current room, 
 2. travels and logs that direction, 
 3. then loops. This should cause your player to walk a depth-first traversal. 
 4. When you reach a dead-end (i.e. a room with no unexplored paths), walk back to the nearest room that does contain an unexplored path.

You can find the path to the shortest unexplored room by using a breadth-first search for a room with a `'?'` for an exit. If you use the `bfs` code from the homework, you will need to make a few modifications.

1. Instead of searching for a target vertex, you are searching for an exit with a `'?'` as the value. If an exit has been explored, you can put it in your BFS queue like normal.

2. BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w directions before you can add it to your traversal path.

