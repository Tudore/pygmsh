class Polygon:
    dimension = 2

    def __init__(self, host, points, mesh_size=None, holes=None, make_surface=True):
        if holes is None:
            holes = []
        else:
            assert make_surface

        if isinstance(mesh_size, list):
            assert len(points) == len(mesh_size)
        else:
            mesh_size = len(points) * [mesh_size]

        # Create points.
        self.points = [
            host.add_point(x, mesh_size=l) for x, l in zip(points, mesh_size)
        ]
        # Create lines
        self.lines = [
            host.add_line(self.points[k], self.points[k + 1])
            for k in range(len(self.points) - 1)
        ] + [host.add_line(self.points[-1], self.points[0])]
        self.curve_loop = host.add_curve_loop(self.lines)
        # self.surface = host.add_plane_surface(ll, holes) if make_surface else None
        if make_surface:
            self.surface = host.add_plane_surface(self.curve_loop, holes)
            self.dim_tags = self.surface.dim_tags
            self._ID = self.surface._ID

    def __repr__(self):
        return "<pygmsh Polygon object>"
