from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.

# map_file = "maps/test_line.txt" ✅
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

# dict to store rooms and their doors
room_dict = dict()

# initialize stack

st = Stack()
st.push(player.current_room)

# mapping continues until dictionary popualtion is equal to number of rooms / dynamic
while st.size() > 0:
    # if room doesnt exist
    cur_room = st.pop()
    # print("stack", st.size(), "st.pop", cur_room)
    if player.current_room.id not in room_dict:
        # add to dictionary, values being cardinal directions
        room_dict[player.current_room.id] = player.current_room.get_exits()
        for cardinal in room_dict[player.current_room.id]:
            # st.push(player.current_room)
            print("c", cardinal)
            traversal_path.append(cardinal)
            st.push(player.travel(cardinal))
            print("here", player.current_room.id)


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



"""
Does current room have doors?
    YES
        How many Doors?   < ------
        Store doors in tmp / key? |
        go through one door       |
            remove door from tmp  |
            add cardinal to path  |
            update visited        |
            check again ----------
    No
        Go back to previous room
        add cardinal to path
        check another door (NOT THIS ONE AGAIN) - check dictionary
"""

