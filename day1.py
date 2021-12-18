import sys
def measurements_larger_than_previous_measurements(depths):
    c = 0
    for i, depth in enumerate(depths):
        if i>0 and depths[i]>=depths[i-1]:
            c+=1

    return c
def sliding_window_increasing_measurements(depths):
    sums = [x1+x2+x3 for x1,x2,x3 in zip(depths,depths[1:],depths[2:])]
    inc = [x2-x1 for x1,x2 in zip(sums, sums[1:]) if x2-x1>0]
    return len(inc)

depths = []
filename = sys.argv[1]
with open(filename) as file:
    depths = file.readlines()
    depths = [int(depth.rstrip()) for depth in depths]

print(measurements_larger_than_previous_measurements(depths))   
print(sliding_window_increasing_measurements(depths))    
