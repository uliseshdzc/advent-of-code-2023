from shapely import geometry
import sys

# sys.argv[1]: input file to use
# sys.argv[2]: part of the daily challenge to run

def main():

    # Load data
    file = open(sys.argv[1])
    data = [line.split() for line in file.read().splitlines()]
    file.close()

    # It is assumed that the perimeter is exactly in the midle of every tile, 
    # therefore the first position is (0.5, 0.5)
    points = []
    current_position = (0.5, 0.5)
    conv_dict = { '0': 'R', '1': 'D', '2': 'L', '3': 'U' }

    # Get all vertices of polygon
    for direction, n_tiles, rgb in data:
        direction = conv_dict[rgb[-2:-1]] if sys.argv[2] == '2' else direction
        n_tiles = int(rgb[2:-2], 16) if sys.argv[2] == '2' else int(n_tiles)
        i, j = current_position

        if direction == 'R':
            j += n_tiles
        if direction == 'L':
            j -= n_tiles
        if direction == 'U':
            i -= n_tiles
        if direction == 'D':
            i += n_tiles

        current_position = i, j
        points.append(current_position)

    # Return the area of the polygon increasing 0.5 the perimeter
    return int(geometry.Polygon(points).buffer(0.5, join_style="mitre").area)
    
if __name__ == "__main__":
    print(main())