import sys
import argparse
from pyproj import Proj
from . import get_regions, get_projections, intersect

out_format = "{}\t{}\t{x[0]:.5f}\t{y[0]:.5f}\t{x[1]:.5f}\t{y[1]:.5f}"

def main():
    parser = argparse.ArgumentParser(prog='guessrs')
    parser.add_argument('source', nargs=4, type=float, help='bounding box in unknown projected coordinates')
    parser.add_argument('target', nargs=4, type=float, help='bounding box in geographic coordinates')

    args = parser.parse_args()

    target = args.target
    regions = list(get_regions(target))
    projections = get_projections(*[r['region'] for r in regions])

    for projection in projections:
        p = Proj(projection['wkt'])
        x, y = p(args.source[::2], args.source[1::2], inverse=True)
        if intersect((x[0], y[0], x[1], y[1]), target):
            xd, yd = (target[0] - x[0], target[2] - x[1]), (target[1] - y[0], target[3] - y[1])
            print(out_format.format(projection['epsg'], p.crs.name, x=xd, y=yd), file=sys.stdout)


if __name__ == '__main__':
    main()
