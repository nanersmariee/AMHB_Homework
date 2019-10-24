
def get_delivery_report (file):
    
    the_file = open(file)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        #fix the indexes, all had 0 originally
        melon = words[0]
        count = words[1]
        amount = words[2]


        print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
    #the_file.close()

print("Day 1")
get_delivery_report("um-deliveries-20140519.txt")
print()

print("Day 2")
get_delivery_report("um-deliveries-20140520.txt")
print()

print("Day 3")
get_delivery_report("um-deliveries-20140521.txt")
print()

# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()
