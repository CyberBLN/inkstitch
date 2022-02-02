import math

# Used in the simplify routine of shapely
simplification_threshold = 0.01

# If a line segment is shorter than this threshold it is handled as a single point
line_lengh_seen_as_one_point = 0.05

# E.g. to check whether a point is already present in a point list,
# the point is allowed to be this value in distance apart
point_spacing_to_be_considered_equal = 0.05

# Adjacent geometry should have points closer than
# offset*offset_factor_for_adjacent_geometry to be considered adjacent
offset_factor_for_adjacent_geometry = 1.5

# Transfer point distance is used for projecting points from already
# rastered geometry to adjacent geometry
# (max spacing transfer_point_distance_factor*offset)
# to get a more regular pattern
transfer_point_distance_factor = 1.5

# Used to handle numerical inaccuracies during comparisons
eps = 1e-3

# When entering and leaving a child from a parent we introduce an offset of
# abs_offset*factor_offset_starting_points
# so that entering and leaving points are not lying above each other.
factor_offset_starting_points = 0.5

# if points are closer than abs_offset*factor_offset_remove_points one of it is removed
factor_offset_remove_points = 0.5

# decides whether the point belongs to a hard edge (must use this point during sampling)
# or soft edge (do not necessarily need to use this point)
limiting_angle = math.pi * 15 / 180.0

# angles straighter (smaller) than this are considered as more or less straight
# (no concrete edges required for path segments having only angles <= this value)
limiting_angle_straight = math.pi * 0.5 / 180.0

# if a point distance to the connected line of its two neighbors is smaller than
# abs_offset times this factor, this point will be removed if the stitching distance will not be exceeded
factor_offset_remove_dense_points = 0.2

# if a soft edge is closer to a forbidden point than abs_offset*this factor it will be marked as forbidden.
factor_offset_forbidden_point = 1.0

# usually overnext projected points are preferred.
# If an overnext projected point would create a much smaller segment than a direct
# projected point we might prefer the direct projected point
factor_segment_length_direct_preferred_over_overnext = 0.5
