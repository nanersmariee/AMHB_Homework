log_file = open("um-server-01.txt")
#setting a variable to logging a file, it's opening it up

def sales_reports(log_file):
    #a function to retrieve the sales report

    for line in log_file:
        #i think this is iterating over a list?

        line = line.rstrip()
        #redefining function

        day = line[0:3]
        if day == "Tues":
            print(line)


sales_reports(log_file)
