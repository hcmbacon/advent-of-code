
def get_submarine_position(filename):
    x = 0
    y = 0
    with open(filename, 'r') as f:
        for line in f:
            inputs = line.split(' ')
            direction = inputs[0]
            length = int(inputs[1])

            if direction == "forward":
                x += length
            elif direction == "down":
                y += length
            elif direction == "up":
                y -= length

    return x, y


if __name__ =="__main__":
    x, y =get_submarine_position('dive_input.txt')
    print(x, y)
    print(x*y)