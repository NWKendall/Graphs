import random

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
	        self.add_user(f"User {i}")

        # Create friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        # Shuffle the possible friendships
        random.shuffle(possible_friendships)
        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # create queue for BFS
        q = Queue()
        # initialize queue with default user_id
        q.enqueue([user_id])
        # initiate traversal
        while q.size() > 0:
            # path is an array
            path = q.dequeue()
            # user is last item in array
            user = path[-1]
            # if user not visited
            if user not in visited:
                # do the thing (adding the path to value of user in visited)
                visited[user] = path
                # for each friends friend
                for friend in self.friendships[user]:
                    # copy path and enqueue
                    new_path = path.copy()
                    new_path.append(friend)
                    q.enqueue(new_path)
        
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    # sg.populate_graph(1000, 5)
    sg.add_user(1)
    sg.add_user(2)
    sg.add_user(3)
    sg.add_user(4)
    sg.add_user(5)
    sg.add_user(6)
    sg.add_user(7)
    sg.add_user(8)
    sg.add_user(9)
    sg.add_user(10)
    sg.add_friendship(1, 8)
    sg.add_friendship(1, 10)
    sg.add_friendship(1, 5)
    sg.add_friendship(2, 10)
    sg.add_friendship(2, 5)
    sg.add_friendship(2, 7)
    sg.add_friendship(3, 4)
    sg.add_friendship(4, 9)
    sg.add_friendship(5, 8)
    sg.add_friendship(5, 1)
    sg.add_friendship(5, 2)
    sg.add_friendship(6, 10)
    sg.add_friendship(7, 2)
    sg.add_friendship(8, 1)
    sg.add_friendship(8, 6)
    sg.add_friendship(9, 4)
    sg.add_friendship(10, 1)
    sg.add_friendship(10, 2)
    sg.add_friendship(10, 6)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

    # {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}

##############
#### UPER ####
##############

#### U ####
# graph of Users
# users connected by friendships
# get all social paths given user_id
# returns dict of user_id's friends with array of connections
    # e.g. {1: [1], 8: [1, 8], 10: [1, 10], 2: [1, 10, 2]...
    #       U   U   F   U  F    F   U   F   FF   U   F  FF

#### P ####
# populate visited dict to default [False]
# traverse own friends
# use BFS for shortest path, need Queue
    # results appended to dict value
# add to dictionary, mark as true?
# for every friend, traverse their friend

# traverse friends

    # traverse friends of friends
        # check to see not already in visited
        # if not add to visited


# # README
# {   1: [1],   
#     2: [1, 10, 2],
#     5: [1, 5],
#     6: [1, 10, 6],
#     7: [1, 10, 2, 7]
#     8: [1, 8],
#     10: [1, 10], 
# }
# # MINE
# {
#     1: [1], ✅
#     2: [1, 10, 2], ✅
#     5: [1, 5], ✅
#     6: [1, 8, 6], 
#     7: [1, 10, 2, 7],✅
#     8: [1, 8], ✅
#     10: [1, 10], ✅
# }
# # MILO
# {
#     1: [1], ✅
#     2: [1, 5, 2], 
#     5: [1, 5], ✅ 
#     6: [1, 10, 6], ✅
#     7: [1, 5, 2, 7], 
#     8: [1, 8], ✅
#     10: [1, 10], ✅
# }