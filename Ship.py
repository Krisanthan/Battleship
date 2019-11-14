class Ship:

    # MAX_ROW_SIZE = 11
    # MAX_COL_SIZE = 9

    def __init__(self, holes, name, board):
        self.name = name
        self.position = []

        for _ in range(holes):
            x_position = input("Enter a letter position for your " + name + " **FORMAT: {A-K}**\n")
            y_position = int(input("Enter a number position for your " + name + " **FORMAT: {1-9}**\n"))
            position = [x_position, y_position]
            position[0] = ord(position[0].lower()) - 96
            position[1] = position[1] - 1
            if not board.check_valid_position(position):
                raise Exception("Invalid Position, please start over")
            self.position.append(position)

        print(self.position)

        # [[1,0], [1,1], [1,2]
        # [[1,0], [2,0], [3,0]


    def check_hit(self, x, y):
        if [x, y] in self.position:
            self.position.remove([x, y])
        print(self.position)

