#Arthur Poon
#MPCS 50101 2,1 Intro to Programming Monday Section
#Module 3 Assignment
#Problem 6

#open file

#initiate empty dictionary
points_coordinates = {}

#open file
try:
    file_handle = open("points.txt", 'r')
except:
    print("error reading file")
else:
    #iterate over file lines
    for line in file_handle:
        #clean lines of whitespaces
        clean_line = line.strip()
        split_line = clean_line.split(',')
        #create dictionary item
        points_coordinates[split_line[0]] = (eval(split_line[1]),eval(split_line[2]), eval(split_line[3]))

print(points_coordinates)

points_coordinates["Origin"] = (0,0,0)

file_handle.close()

def distance_bw_2points(point_a, point_b):
    #initiate squared differences var
    squared_differences = 0

    print(points_coordinates[point_a],points_coordinates[point_b])

    for axes in range(0,len(points_coordinates[point_a])):
        squared_differences += (points_coordinates[point_a][axes] - points_coordinates[point_b][axes]) ** 2

    distance_bw = squared_differences ** 0.5
    return distance_bw

#to get distances from origns
origin_distances = {}
#iterate against origin
for point in points_coordinates:
    origin_distances[point]=distance_bw_2points(point,'Origin')

#calculate the greatest distance
print(f"The point farthest from the origin is {max(origin_distances,key=origin_distances.get)}")

#to get distances between points
distance_bw_points = {}
for point_a in points_coordinates:
    for point_b in points_coordinates:
        if point_b != point_a:
            distance_bw_points[point_a,point_b] = distance_bw_2points(point_a,point_b)
        else:
            pass

print(distance_bw_points)
print(f"The shortest distance is between {min(distance_bw_points,key=distance_bw_points.get)}")

