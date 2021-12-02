
def get_depth_changes(filename):
    with open(filename, 'r') as f:
        counter = 0
        prev_depths = []
        times_increased = 0
        for line in f:
            depth = int(line)
            if counter <4:
                prev_depths.append(depth)
            else:
                if sum(prev_depths[:3]) < sum(prev_depths[1:]):
                    times_increased +=1
                prev_depths = prev_depths[1:]
                prev_depths.append(depth)
            counter +=1
        if sum(prev_depths[:3]) < sum(prev_depths[1:]):
            times_increased +=1

        return times_increased

if __name__ =="__main__":
    print(get_depth_changes('depths_input.txt'))