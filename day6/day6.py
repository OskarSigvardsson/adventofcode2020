from functools import reduce

# Part 1
with open("input.txt", "r") as f:
    # converting a sequence to a set removes all duplicates, so if you just take
    # each chunk and join all the lines and make that a set, the answer is the
    # length of the set
    print(sum(len(set(chunk.replace("\n", ""))) for chunk in f.read().split("\n\n")))

# Part 2
with open("input.txt", "r") as f:
    # reduce(func, list) takes a list "inserts" the function between each pair
    # of items in the list. so if "+" was a function, then reduce(+, [1,2,3,4])
    # is 1+2+3+4. You can't use operators like that directly in python though,
    # so you have to instead wrap it in a lambda that takes two arguments:
    # reduce(lambda x,y: x + y, [1,2,3,4])
    #
    # In this case, we want set intersection, which is & in Python. If you did
    # set union instead (i.e. lambda x,y: x.union(y)), you get the answer to part 1. 
    count = 0

    for chunk in f.read().split("\n\n"):
        answers = [set(x) for x in chunk.strip().split("\n")]
        count += len(reduce(lambda x,y: x & y, answers))

    print(count)
