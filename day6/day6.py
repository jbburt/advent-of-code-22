f = 'day6/data.txt'

with open(f, 'r') as of:
    buffer = of.read().rstrip('\n')


# the start of a packet is indicated by a sequence of four characters
# that are all different

# the start of a message is indicated by a sequence of fourteen characters
# that are all different

# report the number of characters from the beginning of the buffer to the
# end of the first packet-start, and the first message
def subroutine(stream, n=4):
    i = 0
    j = n
    while True:
        if len(set(stream[i: j])) < n:
            i += 1
            j += 1
            continue
        break
    return j


print(f'part A: {subroutine(buffer)}')
print(f'part B: {subroutine(buffer, 14)}')
