
attendees = ["Kim", "Elena","Treasure"]
attendees.append ("Ashley")
attendees.extend(["James","Gill"])
optional = ["Ben", "Dave"]
potential = attendees + optional
print("There are", len(potential),"attendees currently")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional)

print("To: " + to_line)
print("Cc: " + cc_line)



