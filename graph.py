class MapGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height


def draw_grid(graph, width=2):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % '.', end="")
        print()
        
def main():
    g = MapGrid(30, 15)
    draw_grid(g)


if __name__ == '__main__':
    main()