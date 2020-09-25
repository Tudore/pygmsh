from helpers import compute_volume

import pygmsh


def test():
    with pygmsh.opencascade.Geometry() as geom:
        geom.add_wedge([0.0, 0.0, 0.0], [1.0, 1.0, 1.0], top_extent=0.4, mesh_size=0.1)
        mesh = pygmsh.generate_mesh(geom)

    ref = 0.7
    assert abs(compute_volume(mesh) - ref) < 1.0e-2 * ref
    return mesh


if __name__ == "__main__":
    test().write("opencascade_wedge.vtu")