# List
friends = ["Kevin", "Karen", "Jim", "Jim","Oscar","Tony"]
friends[1] = "Mike"
print(friends[-3])
print(friends[1:])
print(friends[1:5])

# List functions
lucky_number = [4,6,23,34,25,73]
friends.extend(["thomas"])
friends.append("thomas 2")
friends.insert(1, "Kelly")
friends.remove("thomas")
friends.pop()
print(friends)
print(friends.index("Kevin"))
print(friends.count("Jim"))
lucky_number.sort()
print(lucky_number)
friends.reverse()
print(friends)
friends2 = friends.copy()
print(friends2)
# friends.clear()

