import sys

# create the users and their relations
with open(sys.argv[1], "r") as my_file1:
    social_net = {}
    for row in my_file1.read().splitlines():
        row = row.split(":")
        social_net[row[0]] = row[1].split()


def ANU(new_user):
    """
    In Add New User function, adds new user into the social network
    :param new_user: new node
    """
    if new_user in social_net.keys():
        my_file3.write("ERROR: Wrong input type! for 'ANU’! -- This user already exists!!\n")
    else:
        social_net[new_user] = list()
        my_file3.write(f"User '{new_user}' has been added to the social network successfully\n")


def DEU(username):
    """
    In Delete Existing User function, the user taken as parameter and all of relations that she/he has will be deleted
    :param username: existing node to be deleted
    """
    if username not in social_net.keys():
        my_file3.write(f"ERROR: Wrong input type! for 'DEU'!--There is no user named '{username}'!!\n")
    else:
        social_net.pop(username)
        for valuelist in social_net.values():
            for value in valuelist:
                if value == username:
                    valuelist.remove(value)
        my_file3.write(f"User '{username}' and his/her all relations have been deleted successfully\n")


def ANF(source_user, target_user):
    """
    In Add New Friend function, a new relation between two nodes will be created
    :param source_user: existing node 
    :param target_user: existing node 
    """
    if (source_user not in social_net) and (target_user in social_net):
        my_file3.write(f"ERROR: Wrong input type! for 'ANF'! -- No user named '{source_user}' found!!\n")
    elif (source_user in social_net) and (target_user not in social_net):
        my_file3.write(f"ERROR: Wrong input type! for 'ANF'! -- No user named '{target_user}' found!!\n")
    elif (source_user not in social_net) and (target_user not in social_net):
        my_file3.write(f"ERROR: Wrong input type! for 'ANF'! -- No user named '{source_user}' and '{target_user}' found!!\n")
    elif target_user in social_net[source_user]:
        my_file3.write(f"ERROR: A relation between '{source_user}' and '{target_user}' already exists!!\n")
    else:
        social_net[source_user].append(target_user)
        social_net[target_user].append(source_user)
        my_file3.write(f"Relation between '{source_user}' and '{target_user}' has been added successfully\n")


def DEF(source_user, target_user):
    """
    In Delete Existing Friend function, the relation between two nodes will be deleted
    :param source_user: existing node 
    :param target_user: existing node 
    """
    if (source_user not in social_net) and (target_user in social_net):
        my_file3.write(f"ERROR: Wrong input type! for 'DEF'! -- No user named '{source_user}' found!!\n")
    elif (source_user in social_net) and (target_user not in social_net):
        my_file3.write(f"ERROR: Wrong input type! for 'DEF'! -- No user named '{target_user}' found!!\n")
    elif (source_user not in social_net) and (target_user not in social_net):
        my_file3.write(f"ERROR: Wrong input type! for 'DEF'! -- No user named '{source_user}' and '{target_user}' found!!\n")
    elif target_user not in social_net[source_user]:
        my_file3.write(f"ERROR: No relation between '{source_user}' and '{target_user}' found!!\n")
    else:
        social_net[source_user].remove(target_user)
        social_net[target_user].remove(source_user)
        my_file3.write(f"Relation between '{source_user}' and '{target_user}' has been deleted successfully\n")


def CF(username):
    """
    In Count Friend function, number of friends of the given user will be given
    :param username: existing user
    """
    if username not in social_net.keys():
        my_file3.write(f"ERROR: Wrong input type! for 'CF'! -- No user named '{username}' found!\n")
    else:
        my_file3.write(f"User '{username}' has {len(social_net[username])} friends\n")


def FPF(username, maximum_distance):
    """
    Find Possible Friends function finds possible friends for each user.
    :param username: existing node 
    :param maximum_distance: distance from the given user
    """
    max_dis1 = maximum_distance
    possible_friend = set()
    if username not in social_net.keys():
        my_file3.write(f"ERROR: Wrong input type! for 'FPF'! -- No user named '{username}' found!\n")
    elif (maximum_distance < 1) or (maximum_distance > 3):
        my_file3.write(f"ERROR: Maximum distance is out of range!\n")
    else:
        x = 0
        looper = 0
        while x == 0:
            maximum_distance -= 1
            looper += 1
            for f1 in social_net[username]:
                possible_friend.add(f1)
                if maximum_distance == 0:
                    x = 1
                else:
                    for f2 in social_net[f1]:
                        possible_friend.add(f2)
                        if looper == 2:
                            for f3 in social_net[f2]:
                                possible_friend.add(f3)
                    continue

        possible_friend.discard(username)
        my_file3.write(f"User '{username}' has {len(possible_friend)} possible friends when maximum distance is {max_dis1}\n")
        my_file3.write("These possible friends: {}".format(sorted(possible_friend)).replace("[", "{").replace("]", "}\n"))


def SF(username, MD):
    """
    Suggest Friend function finds possible friends for each user.
    :param username: existing node 
    :param MD: mutuality degree 
    """
    if username not in social_net.keys():
        my_file3.write(f"Error: Wrong input type! for 'SF'! -- No user named '{username}' found!!\n")
    elif (MD < 2) or (MD > 3):
        my_file3.write("Error: Mutually Degree cannot be less than 2 or greater than 3\n")
    elif MD > len(social_net[username]):
        my_file3.write("Error: MD cannot be greater than username's friends!!\n")
    else:
        my_file3.write(f"Suggestion List for '{username}' (when MD is {MD}):\n")
        fof_set = set()
        fof_list = []
        suggestion_list = []

        for person in social_net[username]:
            for f2 in social_net[person]:
                if (f2 != username) and (f2 not in social_net[username]):
                    fof_set.add(f2)
                    fof_list.append(f2)
        count_dic = {f2: fof_list.count(f2) for f2 in sorted(fof_set)}

        for person, count in sorted(count_dic.items(), key=lambda item: item[1]):
            if (count >= MD) and (count <= 3):
                my_file3.write(f"'{username}' has {count} mutual friends with '{person}'\n")
                suggestion_list.append(f"'{person}'")
        my_file3.write("The suggested friends for '{}':{}\n".format(username, ",".join(suggestion_list)))


with open("output.txt", "w") as my_file3:
    with open(sys.argv[2], "r") as my_file2:
        for command in my_file2.read().splitlines():
            command = list(command.split(" "))
            if command[0] == "ANU":
                ANU(command[1])
            elif command[0] == "DEU":
                DEU(command[1])
            elif command[0] == "ANF":
                try:
                    ANF(command[1], command[2])
                except IndexError:
                    my_file3.write("ERROR: This command must contain 3 elements!!\n")
            elif command[0] == "DEF":
                try:
                    DEF(command[1], command[2])
                except IndexError:
                    my_file3.write("ERROR: This command must contain 3 elements!!\n")
            elif command[0] == "CF":
                CF(command[1])
            elif command[0] == "FPF":
                try:
                    FPF(command[1], int(command[2]))
                except IndexError:
                    my_file3.write("ERROR: This command must contain 3 elements!!\n")
            elif command[0] == "SF":
                try:
                    SF(command[1], int(command[2]))
                except IndexError:
                    my_file3.write("ERROR: This command must contain 3 elements!!\n")
            elif command[0] == "":
                pass
            else:
                my_file3.write("ERROR: Invalid command!!\n")