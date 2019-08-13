areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Creates the variable areas_copy, such that areas_copy is an explicit copy of areas
areas_copy = areas[:]

# Update the area of the bathroom area to be 10.50 square meters instead of 9.50.
areas[-1] = 10.50

# Make the areas list more trendy! Change "living room" to "chill zone"
areas[4] = "chill zone"

# Print areas_copy
print(areas_copy)

# Add poolhouse data ["poolhouse", 24.5] to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data ["garage", 15.45] to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

# Remove poolhouse and its area
del(areas_2[-4:-2])
