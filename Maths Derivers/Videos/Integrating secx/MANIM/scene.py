#changes: Indian music and voice; reducing pacing at 0.5 seconds between animations and 1.2 seconds between scenes
#switch from white text on black background to black text on white background

from manim import *

def LineByLine(scene, objects, delay):
    #incrementally add objects below objects[0]
    #does not write objects[0] to screen: assumed it is already written
    i = 1
    while i < len(objects):
        prevObject = objects[i - 1]
        object = objects[i]
        object.next_to(prevObject, DOWN, aligned_edge=LEFT)

        scene.play(Create(object))
        scene.wait(delay)
        i += 1



class Main(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        #transforming for substitution
        eq1 = MathTex(r"\int \sec{x} \, dx", color=BLACK)
        eq2 = MathTex(r"=\int \frac{1}{\cos{x}} \, dx", color=BLACK)
        eq3 = MathTex(r"=\int \frac{\cos{x}}{\cos^2{x}} \, dx", color=BLACK)
        eq4 = MathTex(r"=\int \frac{\cos{x}}{1 - \sin^2{x}} \, dx", color=BLACK)

        #u = sinx
        sub5 = MathTex(r"\textit{let } u = \sin{x}", color=BLACK)
        sub6 = MathTex(r"du = \cos{x} \, dx", color=BLACK)

        #partial fractions
        eq7 = MathTex(r"=\int \frac{1}{1 - u^2} \, du", color=BLACK)
        eq8 = MathTex(r"=\int \frac{1}{(1 + u)(1 - u)} \, du", color=BLACK)
        eq9 = MathTex(r"=\int \frac{A}{1 + u} + \frac{B}{1 - u} \, du", color=BLACK)
        eq10 = MathTex(r"=\int \frac{\frac{1}{2}}{1+u}+\frac{\frac{1}{2}}{1-u} \, du", color=BLACK)

        #integral done, manipulating to final result
        eq11 = MathTex(r"=\left[ \frac{1}{2} \ln(1 + u) - \frac{1}{2} \ln(1 - u) \right]", color=BLACK)
        eq12 = MathTex(r"=\frac{1}{2} \left[ \ln(1 + u) - \ln(1 - u) \right]", color=BLACK)
        eq13 = MathTex(r"=\frac{1}{2} \ln \left( \frac{1 + u}{1 - u} \right)", color=BLACK)
        eq14 = MathTex(r"=\frac{1}{2} \ln \left( \frac{1 + \sin{x}}{1 - \sin{x}} \right)", color=BLACK)
        eq15 = MathTex(r"=\frac{1}{2} \ln \left( \frac{(1 + \sin{x})(1 + \sin{x})}{(1 - \sin{x})(1 + \sin{x})} \right)", color=BLACK)
        eq16 = MathTex(r"=\frac{1}{2} \ln \left( \frac{(1 + \sin{x})^2}{1 - \sin^2{x}} \right)", color=BLACK)
        eq17 = MathTex(r"=\frac{1}{2} \ln \left( \frac{(1 + \sin{x})^2}{\cos^2{x}} \right)", color=BLACK)
        eq18 = MathTex(r"=\ln \left( \sqrt{\frac{(1 + \sin{x})^2}{\cos^2{x}}} \right)", color=BLACK)
        eq19 = MathTex(r"=\ln\left( \frac{1 + \sin{x}}{\cos{x}} \right)", color=BLACK)
        eq20 = MathTex(r"=\ln\left( \frac{1}{\cos{x}} + \frac{\sin{x}}{\cos{x}} \right)", color=BLACK)
        eq21 = MathTex(r"=\ln(\sec{x} + \tan{x})", color=BLACK)
        eq22 = MathTex(r"\ln(\sec{x} + \tan{x}) + C", color=BLACK)


        #draw graph of 1/secx in background
        # Create the axes without labels and arrows
        axes = Axes(
            x_range=[-3.5, 3.5, 1],  # x-axis range
            y_range=[-3, 3, 1],  # y-axis range
            axis_config={"color": "#bbbbbb", "include_tip": False},
            tips=False,  # Remove arrows at the ends of axes
        )

        # Create the graph of y = sec(x), avoiding asymptotes
        PURPLE = "#a22ef0"
        sec_graph_left = axes.plot(
            lambda x: 1 / np.cos(x), 
            x_range=[-3.5, -np.pi/2 - 0.1],  # Before first asymptote
            color=PURPLE,
        )
        sec_graph_middle = axes.plot(
            lambda x: 1 / np.cos(x), 
            x_range=[-np.pi/2 + 0.1, np.pi/2 - 0.1],
            color=PURPLE,
        )
        sec_graph_right = axes.plot(
            lambda x: 1 / np.cos(x), 
            x_range=[np.pi/2 + 0.1, 3.5],  # After second asymptote
            color=PURPLE,
        )

        # Create the shaded area between x = -1 and x = 1
        shaded_area = axes.get_area(
            sec_graph_middle, 
            x_range=[-1, 1],
            color="#8800ff", 
            opacity=0.63
        )

        eq1.move_to(np.array((0, -0.7, 0)))

        # Display the graphs and shaded area
        self.play(Create(axes), Create(sec_graph_left), Create(sec_graph_middle), Create(sec_graph_right))
        self.play(DrawBorderThenFill(shaded_area, run_time=0.5))
        self.play(Write(eq1))
        self.wait(2)

        self.play(
            FadeOut(axes),
            FadeOut(sec_graph_left),
            FadeOut(sec_graph_middle),
            FadeOut(sec_graph_right),
            FadeOut(shaded_area),
            eq1.animate.move_to(np.array((-0.5, 2.0, 0.0)))
        )
        self.wait(0.5)
        LineByLine(self, [eq1, eq2, eq3, eq4], 0.5)
        self.wait(0.7)
        self.play(
            FadeOut(eq1),
            FadeOut(eq2),
            FadeOut(eq3),
            eq4.animate.move_to(UP*3)
        )

        sub5.next_to(eq4, DOWN*3)
        sub6.next_to(sub5, DOWN)
        equations_group = VGroup(sub5, sub6)
        box = SurroundingRectangle(equations_group, color=BLACK, buff=0.5)

        self.play(Create(box))
        self.wait(0.5)
        self.play(Create(sub5))
        self.wait(0.5)
        self.play(Create(sub6))
        self.wait(0.5)

        eq7.next_to(eq4, DOWN*10, aligned_edge=LEFT)
        self.play(Create(eq7))
        LineByLine(self, [eq7, eq8, eq9], 0.5)
        self.wait(0.7)
        self.play(
            FadeOut(eq4),
            FadeOut(box),
            FadeOut(sub5),
            FadeOut(sub6),
            FadeOut(eq7),
            FadeOut(eq8),
            eq9.animate.move_to(UP*3)
        )

        LineByLine(self, [eq9, eq10, eq11, eq12, eq13], 0.5)
        self.wait(0.7)
        self.play(
            FadeOut(eq9),
            FadeOut(eq10),
            FadeOut(eq11),
            FadeOut(eq12),
            eq13.animate.move_to(np.array((-0.63, 3.0, 0.0)))
        )

        LineByLine(self, [eq13, eq14, eq15, eq16, eq17], 0.5)
        self.wait(0.7)
        self.play(
            FadeOut(eq13),
            FadeOut(eq14),
            FadeOut(eq15),
            FadeOut(eq16),
            eq17.animate.move_to(UP*3)
        )

        LineByLine(self, [eq17, eq18, eq19, eq20, eq21], 0.5)
        self.wait(0.7)
        self.play(
            FadeOut(eq17),
            FadeOut(eq18),
            FadeOut(eq19),
            FadeOut(eq20),
            Transform(eq21, eq22)
        )
        self.play(eq21.animate.move_to(ORIGIN))

class Subtitles(Scene):
    def construct(self):
        script = """
Multiply numerator and denominator by cosx.

Use trigonometric identity.

Setup substitution to simplify.

Decompose into partial fractions.

Determine constants and integrate to natural logs.

Factor out constant half and combine logarithms.

Re-substitute sinx.

Rationalise numerator and denominator.

Simplify and use sin cos identity again.

Move half into logarithm to square root.

Split fractions to clean up.

Don't forget the plus 'c', and WE'RE DONE!
""".split(".")
        script.insert(0, "Not many people can solve this integral, can you?")
        
        self.camera.background_color = WHITE

        for line in script:
            print(line)
            latex = Text(line, color=BLACK)
            self.play(FadeIn(latex))
            self.wait(2)
            self.play(FadeOut(latex))
            self.wait(1)
