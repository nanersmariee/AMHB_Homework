
def get_delivery_report (day_number,file):
    
    print("Day", day_number)
    print()

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
    print()
    #the_file.close()

get_delivery_report(1, "um-deliveries-20140519.txt")
get_delivery_report(2, "um-deliveries-20140520.txt")
get_delivery_report(3, "um-deliveries-20140521.txt")
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
