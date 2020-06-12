from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.

# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# unique values to store visited history
visited = set()

# dict to store rooms and their doors
room_dict = dict()

# initialize stack
q = Queue()
q.enqueue([player.current_room])

while q.size() > 0:
    path = q.dequeue()
    cur_room = path[-1]
    # print("ROOM:", cur_room.id)

    if cur_room.id not in visited:
        visited.add(cur_room.id)
        room_dict[cur_room.id] = { "n": "?", "s": "?", "e": "?", "w": "?", }
        

        
print("VISITED:", visited)
print("ROUTE:", traversal_path)
print("ROOM_DICT:", room_dict)
# for room in visited:
#     print(room)
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# ######
# UNCOMMENT TO WALK AROUND
# ######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")





# UPER
# create graph
# create visited dictionary
# create q for traversal
# start 