# Authors: see git history
#
# Copyright (c) 2010 Authors
# Licensed under the GNU GPL version 3.0 or later.  See the file LICENSE for details.

import inkex
from shapely import geometry as shgeo

from .stitch_plan import Stitch
from .svg.tags import EMBROIDERABLE_TAGS
from .utils import Point


def is_pattern(node):
    if node.tag not in EMBROIDERABLE_TAGS:
        return False
    style = node.get('style') or ''
    return "marker-start:url(#inkstitch-pattern-marker)" in style


def apply_patterns(patches, node):
    patterns = get_patterns(node, "#inkstitch-pattern-marker")
    _apply_stroke_patterns(patterns['stroke_patterns'], patches)
    _apply_fill_patterns(patterns['fill_patterns'], patches)


def _apply_stroke_patterns(patterns, patches):
    for pattern in patterns:
        for patch in patches:
            patch_points = []
            for i, stitch in enumerate(patch.stitches):
                patch_points.append(stitch)
                if i == len(patch.stitches) - 1:
                    continue
                intersection_points = _get_pattern_points(stitch, patch.stitches[i+1], pattern)
                for point in intersection_points:
                    patch_points.append(Stitch(point, tags=('pattern_point',)))
            patch.stitches = patch_points


def _apply_fill_patterns(patterns, patches):
    for pattern in patterns:
        for patch in patches:
            patch_points = []
            for i, stitch in enumerate(patch.stitches):
                if not shgeo.Point(stitch).within(pattern):
                    # keep points outside the fill pattern
                    patch_points.append(stitch)
                elif i - 1 < 0 or i >= len(patch.stitches) - 1:
                    # keep start and end points
                    patch_points.append(stitch)
                elif stitch.has_tag('fill_row_start') or stitch.has_tag('fill_row_end'):
                    # keep points if they are the start or end of a fill stitch row
                    patch_points.append(stitch)
                elif stitch.has_tag('auto_fill') and not stitch.has_tag('auto_fill_top'):
                    # keep auto-fill underlay
                    patch_points.append(stitch)
                elif stitch.has_tag('auto_fill_travel'):
                    # keep travel stitches (underpath or travel around the border)
                    patch_points.append(stitch)
                elif stitch.has_tag('satin_column') and not stitch.has_tag('satin_split_stitch'):
                    # keep satin column stitches unless they are split stitches
                    patch_points.append(stitch)
            patch.stitches = patch_points


def get_patterns(node, marker_id, get_fills=True, get_strokes=True):
    from .elements import EmbroideryElement
    from .elements.stroke import Stroke

    fills = []
    strokes = []
    xpath = "./parent::svg:g/*[contains(@style, 'marker-start:url("+marker_id+")')]"
    patterns = node.xpath(xpath, namespaces=inkex.NSS)
    for pattern in patterns:
        if pattern.tag not in EMBROIDERABLE_TAGS:
            continue

        element = EmbroideryElement(pattern)
        fill = element.get_style('fill')
        stroke = element.get_style('stroke')

        if get_fills and fill is not None:
            fill_pattern = auto_fill(pattern).shape
            fills.append(fill_pattern)
            #fill_pattern = Stroke(pattern).paths
            #linear_rings = [shgeo.LinearRing(path) for path in fill_pattern]
            #for ring in linear_rings:
            #    fills.append(shgeo.Polygon(ring))

        if get_strokes and stroke is not None:
            stroke_pattern = Stroke(pattern).paths
            line_strings = [shgeo.LineString(path) for path in stroke_pattern]
            strokes.append(shgeo.MultiLineString(line_strings))

    return {'fill_patterns': fills, 'stroke_patterns': strokes}


def _get_pattern_points(first, second, pattern):
    points = []
    intersection = shgeo.LineString([first, second]).intersection(pattern)
    if isinstance(intersection, shgeo.Point):
        points.append(Point(intersection.x, intersection.y))
    if isinstance(intersection, shgeo.MultiPoint):
        for point in intersection:
            points.append(Point(point.x, point.y))
    # sort points after their distance to first
    points.sort(key=lambda point: point.distance(first))
    return points
