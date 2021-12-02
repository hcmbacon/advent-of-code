
def get_depth_changes(filename):
    with open(filename, 'r') as f:
        counter = 0
        prev_depth = None
        times_increased = 0
        for line in f:
            depth = int(line)
            if counter ==0:
                pass
            else:
                if prev_depth < depth:
                    times_increased +=1
            prev_depth = depth
            counter +=1
        return times_increased

if __name__ =="__main__":
    get_depth_changes('depths_input.txt')