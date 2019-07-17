#!/usr/bin/env python3
import pkg_resources
from pyproj import Proj

PROJECTIONS = 'data/projections.txt'
REGIONS = 'data/regions.txt'


def reader(path):
    with pkg_resources.resource_stream('guessrs', path) as f:
        fields = f.readline().decode('ascii').strip().split('\t')
        for line in f:
            values = line.decode('ascii').strip().split('\t')
            yield dict(zip(fields, values))


def get_regions(bbox):
    '''Given a bounding box in geographic coordinates, find regions that overlap with it'''
    for row in reader(REGIONS):
        row_box = tuple(float(t) for t in (row['x0'], row['y0'], row['x1'], row['y1']))
        if intersect(bbox, row_box):
            yield row


def get_projections(*regions):
    '''Given a set of region names, find projections that match it'''
    for row in reader(PROJECTIONS):
        if row['region'] in regions:
            yield row


def inverse(srs_text, bbox):
    '''Given projectioned coordinates, inv-project to geographic coordinates.'''
    x, y = Proj(srs_text)(bbox[::2], bbox[1::2], inverse=True)
    return x[0], y[0], x[1], y[1]


def project(srs_text, bbox):
    '''Given a projection and a bbox, project geographic coordinates to it'''
    x, y = Proj(srs_text)(bbox[::2], bbox[1::2])
    return x[0], y[0], x[1], y[1]


def intersect(a, b):
    '''Given two bboxes, check if they overlap.'''
    return not (a[2] < b[0] or a[0] > b[2] or a[3] < b[1] or a[1] > b[3])
