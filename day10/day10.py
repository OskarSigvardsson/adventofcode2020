adaptors = []

with open("input.txt", "r") as f:
    adaptors = [int(line) for line in f]


def part1(adaptors):
    # add the wall outlet
    ns = [0] + sorted(adaptors)

    c1 = sum(1 for a,b in zip(ns, ns[1:]) if b == a+1)
    c3 = sum(1 for a,b in zip(ns, ns[1:]) if b == a+3)

    # the final one to the device
    c3 += 1
    
    return c1 * c3


def part2(adaptors):
    adaptors = set(adaptors)

    adaptors.add(0)

    memo = {}
    
    # This function returns the count of the number of ways you can get adaptors
    # from start to end. The only adaptors you can plug into an adaptor of
    # joltage "start" are ones that are 1, 2 or 3 values higher. That means
    # that, in general, the formula for this count is this:
    #
    #   count(start, end) = count(start + 1, end)
    #                     + count(start + 2, end)
    #                     + count(start + 3, end)
    #
    # There are some special cases though: if start is more than end, there is
    # no ways to plug them in. Same if there isn't an adaptor of of size start,
    # then there is also no way to plug it in. If we're within a range of 3,
    # there is one extra way to plug it in, because you can plug in the device
    # directly.
    #
    # That part is straightforwardly recursive, but there's another issue with
    # this function: it's far too slow to just do directly. At every level of
    # recursion, the number of function calls multiply by 3. Then the next level
    # they multiply by 3 again, then 3 again, then 3 again... Just running it
    # would take a humungous amount of time, because the number of function
    # calls grows exponentially. The function will be called literally trillions
    # of times. 
    #
    # The trick here is to realise that for any given value of count(start,
    # end), you only need to calculate it ONCE. It's always going to give you
    # the same values for the same inputs, so there's no need to calculate it
    # over and over, which is what the recursive version does. You can think of
    # it like this: if the max value is (say) 100, there's only 100 different
    # possible inputs to count (i.e. count(0, 100), count (1, 100), count(2,
    # 100), ..., count(100, 100)). Yet the function is being called trillions of
    # times: clearly we're recalculating values we've already calculated. 
    #
    # The answer therefore is to cache the input values and output values of the
    # function in a dictionary. This is what the "memo" dict does. This
    # technique is called "memoization", and it's part of a more general field
    # of problems called "dynamic programming problems". Dynamic programming
    # problems all have this same structure, where you have a recursive solution
    # which recalculates the same values over and over again. The simplest way
    # to solve dynamic programming problems are using memoization, though there
    # are also faster ways to do it, but it's not necessary in this case. 
    def count(start, end):
        # Check if we've overshot
        if start >= end:
            return 0

        # Check if an adaptor of size start actually exists
        if start not in adaptors:
            return 0

        # Check if we've already calculated the value
        if start in memo:
            return memo[start]
        
        ways = 0

        # Do the recursive check
        for i in range(1,4):
            ways += count(start + i, end)

        # If we can plug it in directly, there's one extra way to solve it
        if end - start <= 3:
            ways += 1

        # Cache the value for future calculations
        memo[start] = ways
        
        return ways

    return count(0, max(adaptors) + 3)

print(part1(adaptors))
print(part2(adaptors))
