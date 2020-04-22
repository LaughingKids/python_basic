# read - r
# appending - a
# write - w
test_csv = open("test1.csv","w")

# for record in test_csv.readlines():
#     print(record.split(","))

test_csv.write("Sandy Allen,2019,Oliver House,108,3.48")

test_csv.close()