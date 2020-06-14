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

# ##### PLAYER AND ROOM METHOD DESCRIPTIONS #####
# print("get_exits:", player.current_room.get_exits())
# # returns arrays of strings
# print("get_exits_string:", player.current_room.get_exits_string())
# # returns exits array as string value for game display
# print("get_room_in_direction:", player.current_room.get_room_in_direction("n"))
# # returns room object, shows name, descrip and exits
# print("get_coords:", player.current_room.get_coords())
# # return list of coords
# print(player.travel("n"), player.current_room)
# # updates player.current room

# print("ROUTE:", traversal_path)
# print("ROOM_DICT:", room_dict)

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
Has the room been explored? <-------------
    No:                                   |
        Does current room have doors?     | 
            YES                           |
                How many Doors?           |
                Store doors in tmp / key? |
                go through one door       | <---------------------------------
                    remove door from tmp  |                                   |
                    add cardinal to path  |                                   |
                    update explored       |                                   |
                    check again ----------                                    |
            No                                                                |
                Go back to previous room                                      |
                add cardinal to path                                          |
                check another door (NOT THIS ONE AGAIN) - check dictionary    |
    Yes:                                                                      |
        Any doors left that need exploring?                                   |
            Yes ---------------------------------------------------------------
            No:
                go back to previous room
                add cardinal to path
                check another door (NOT THIS ONE AGAIN) - check dictionary

    EVERY TRAVEL MUST BE ADDED TO THE TRAVERSAL_PATH!!!!!
    https://www.youtube.com/watch?v=gBC_Fd8EE8A&t=306s
    https://www.youtube.com/watch?v=Zq4upTEaQyM&t=610s
"""
