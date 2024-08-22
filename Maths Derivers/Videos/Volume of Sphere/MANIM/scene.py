
from manim import *
from math import *

class Sphere(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Surface(
            lambda u, v: np.array([
                np.cos(u) * np.sin(v),
                np.sin(u) * np.sin(v),
                np.cos(v)
            ]),
            u_range=[0, PI/2],
            v_range=[0, PI/2],
            checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.add(axes, sphere)
        self.play(Create(axes), Create(sphere))
