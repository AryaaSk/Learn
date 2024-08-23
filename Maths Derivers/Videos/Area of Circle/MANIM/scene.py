#showing all steps one after each other, and faster pacing to 0.3 seconds between animations

from manim import *
from math import *

class Main(Scene):
    def construct(self):
        r = 1.5
        axes = Axes(
            x_range=[-1, 1], 
            y_range=[-1, 1],
            x_length=4,   # Adjust the length of the x-axis
            y_length=4,   # Adjust the length of the y-axis to match x-axis length
            axis_config={"color": WHITE, "include_tip": False}
        )

        # Ensure equal aspect ratio to maintain proportional spacing
        axes.set_aspect_ratio(1)

        # Create a circle with a radius that matches the units on the axis
        circle = Circle(radius=axes.x_length / (2 * r), color=BLUE)
        circle.move_to(axes.c2p(0, 0))  # Center the circle at the origin


        xDot = Dot((axes.x_length / (2 * r), 0, 0), color=RED) #not sure why x axis has wrong scale
        yDot = Dot((0, axes.y_length / (2 * r), 0), color=RED)
        intersection_points = VGroup(
            VGroup(xDot, Tex("r").next_to(xDot, DOWN)),
            VGroup(yDot, Tex("r").next_to(yDot, LEFT)),
        )

        #equation1 = MathTex("x^2 + y^2 = r^2").to_edge(UP)
        #equation2 = MathTex("y^2 = r^2 - x^2").next_to(equation1, DOWN)
        #equation3 = MathTex("y = \\sqrt{r^2 - x^2}").next_to(equation2, DOWN)
        area = MathTex(r"A = \pi r^2")
        area.next_to(axes, DOWN)  # This positions the formula below the axes
        area.shift(DOWN * 0.5)    # Adjust further down if needed

        xLine = Line((0, 0, 0), (axes.x_length / (2 * r), 0, 0), color=YELLOW)
        first_quadrant_arc = Arc(radius=axes.x_length / (2 * r), start_angle=0, angle=PI/2, color=YELLOW)
        yLine = Line((0, axes.y_length / (2 * r), 0), (0, 0, 0), color=YELLOW)
        outline = VGroup(xLine, first_quadrant_arc, yLine)

        outlineWithPoints = VGroup(intersection_points, outline)
        
        self.play(Create(axes))
        self.play(Create(circle))
        self.play(Write(area))
        self.wait(5)


        self.play(Create(outlineWithPoints))
        self.wait(10)

        # Fade out everything except the quarter circle outline
        self.play(
            FadeOut(axes),
            FadeOut(circle),
            FadeOut(area)
        )
        
        # Optionally, you can adjust the quarter circle position
        # e.g., move it to the center of the scene
        self.play(outlineWithPoints.animate.move_to(UP*2.5))
        
        self.wait(2)

        circleEquation1 = MathTex(r"x^{2}+y^{2}=r^{2}")
        circleEquation1.next_to(outlineWithPoints, DOWN)

        circleEquation2 = MathTex(r"y^{2}=r^{2}-x^{2}")
        circleEquation2.next_to(circleEquation1, DOWN)

        circleEquation3 = MathTex(r"y=\sqrt{r^{2}-x^{2}}")
        circleEquation3.next_to(circleEquation2, DOWN)

        areaEquation1 = MathTex(r"A=4\int_{0}^{r}ydx")
        areaEquation1.next_to(circleEquation3, DOWN)

        self.play(Write(circleEquation1))
        self.wait(0.3)
        self.play(Write(circleEquation2))
        self.wait(0.3)
        self.play(Write(circleEquation3))
        self.wait(1)
        self.play(Write(areaEquation1))
        self.wait(0.3)

        areaEquation2 = MathTex(r"A=4\int_{0}^{r}\sqrt{r^{2}-x^{2}}dx")
        areaEquation2.next_to(areaEquation1, DOWN)
        self.play(Write(areaEquation2))

        self.wait(5)

        self.play(
            FadeOut(outlineWithPoints),
            FadeOut(circleEquation1),
            FadeOut(circleEquation2),
            FadeOut(circleEquation3),
            FadeOut(areaEquation1),
            areaEquation2.animate.move_to(UP*3)
        )


        #Substitution box
        subEq1 = MathTex(r"let\ x=r\sin\theta")
        subEq1.next_to(areaEquation2, DOWN*3)
        subEq2 = MathTex(r"x=0,\ r")
        subEq2.next_to(subEq1, DOWN)
        subEq3 = MathTex(r"\theta=0,\ \frac{\pi}{2}")
        subEq3.next_to(subEq2, DOWN)
        subEq4 = MathTex(r"dx=r\cos\theta\ d\theta")
        subEq4.next_to(subEq3, DOWN)

        equations_group = VGroup(subEq1, subEq2, subEq3, subEq4)
        box = SurroundingRectangle(equations_group, color=WHITE, buff=0.3)
        self.play(Create(box))

        self.play(Write(subEq1))
        self.wait(0.3)
        self.play(Write(subEq2))
        self.wait(0.3)
        self.play(Write(subEq3))
        self.wait(0.3)
        self.play(Write(subEq4))
        self.wait(0.3)

        #make substitution
        area1 = MathTex(r"A=4\int_{0}^{\frac{\pi}{2}}\sqrt{r^{2}-r^{2}\sin^{2}\theta}\cdot r\cos\theta\ d\theta")
        area1.next_to(subEq4, DOWN*4)
        self.play(Write(area1))

        self.wait(2)
        self.play(
            FadeOut(areaEquation2),
            FadeOut(box),
            FadeOut(subEq1),
            FadeOut(subEq2),
            FadeOut(subEq3),
            FadeOut(subEq4),
            area1.animate.to_edge(UP)
        )

        area1b = MathTex(r"=4\int_{0}^{\frac{\pi}{2}}r\sqrt{1-\sin^{2}\theta}\cdot r\cos\theta\ d\theta")
        area1b.next_to(area1, DOWN)

        area2 = MathTex(r"=4\int_{0}^{\frac{\pi}{2}}r\sqrt{\cos^{2}\theta}\cdot r\cos\theta\ d\theta")
        area2.next_to(area1b, DOWN, aligned_edge=LEFT)

        area3 = MathTex(r"=4\int_{0}^{\frac{\pi}{2}}r\cos\theta\cdot r\cos\theta\ d\theta")
        area3.next_to(area2, DOWN, aligned_edge=LEFT)

        area4 = MathTex(r"=4r^{2}\int_{0}^{\frac{\pi}{2}}\cos^{2}\theta\ d\theta")
        area4.next_to(area3, DOWN, aligned_edge=LEFT)

        # Displaying the areas one after another
        self.play(Write(area1b))
        self.wait(0.3)
        self.play(Write(area2))
        self.wait(0.3)
        self.play(Write(area3))
        self.wait(0.3)
        self.play(Write(area4))
        self.wait(2)

        self.play(
            FadeOut(area1),
            FadeOut(area1b),
            FadeOut(area2),
            FadeOut(area3),
            area4.animate.move_to(UP*3.3)
        )

        area5 = MathTex(r"=4r^{2}\int_{0}^{\frac{\pi}{2}}\frac{1}{2}\left(1+\cos2\theta\right)\ d\theta")
        area5.next_to(area4, DOWN, aligned_edge=LEFT)

        limits = MathTex(
            r"=2r^{2}\left[\theta + \frac{1}{2}\sin2\theta\right]_0^\frac{\pi}{2}"
        )
        limits.next_to(area5, DOWN, aligned_edge=LEFT)

        evaluated = MathTex(r"=2r^{2}\left[\frac{\pi}{2}+\frac{1}{2}\sin\pi\right]")
        evaluated.next_to(limits, DOWN, aligned_edge=LEFT)

        simplified = MathTex(r"=2r^{2}\left[\frac{\pi}{2}\right]")
        simplified.next_to(evaluated, DOWN, aligned_edge=LEFT)

        final = MathTex(r"=\pi r^{2}")
        final.next_to(simplified, DOWN, aligned_edge=LEFT)

        self.play(Write(area5))
        self.wait(0.3)
        self.play(Write(limits))
        self.wait(0.3)
        self.play(Write(evaluated))
        self.wait(0.3)
        self.play(Write(simplified))
        self.wait(0.3)
        self.play(Write(final))
        self.wait(2)

        final2 = MathTex(r"A=\pi r^{2}")

        self.play(
            FadeOut(area4),
            FadeOut(area5),
            FadeOut(limits),
            FadeOut(evaluated),
            FadeOut(simplified),
            Transform(final, final2),
        )
        self.play(final.animate.move_to(ORIGIN))