#Increasing pace to only wait 0.7 seconds between animations, and now using FadeTransform for clearer animations

from manim import *

class QuadraticFormula(Scene):
    def construct(self):
        # Step 1: Write the general form of the quadratic equation
        eq1 = MathTex(r"ax^2 + bx + c = 0")
        self.play(Write(eq1))
        self.wait(0.7)

        # Step 2: Divide the whole equation by a
        eq2 = MathTex(r"x^2 + \frac{b}{a}x + \frac{c}{a} = 0")
        self.play(FadeTransform(eq1, eq2))
        self.wait(0.7)

        # Step 3: Move the constant term to the right side
        eq3 = MathTex(r"x^2 + \frac{b}{a}x = -\frac{c}{a}")
        self.play(FadeTransform(eq2, eq3))
        self.wait(0.7)

        # Step 4: Complete the square on the left side
        eq4 = MathTex(r"\left( x + \frac{b}{2a} \right)^2 - \frac{b^2}{4a^2} = -\frac{c}{a}")
        self.play(FadeTransform(eq3, eq4))
        self.wait(0.7)

        # Step 5: Add \(\frac{b^2}{4a^2}\) to both sides to balance the equation
        eq5 = MathTex(r"\left( x + \frac{b}{2a} \right)^2 = \frac{b^2}{4a^2} - \frac{c}{a}")
        self.play(FadeTransform(eq4, eq5))
        self.wait(0.7)

        # Step 6: Combine the fractions on the right side
        eq6 = MathTex(r"\left( x + \frac{b}{2a} \right)^2 = \frac{b^2 - 4ac}{4a^2}")
        self.play(FadeTransform(eq5, eq6))
        self.wait(0.7)

        # Step 7: Take the square root of both sides
        eq7 = MathTex(r"x + \frac{b}{2a} = \pm \frac{\sqrt{b^2 - 4ac}}{2a}")
        self.play(FadeTransform(eq6, eq7))
        self.wait(0.7)

        # Step 8: Solve for x by subtracting \(\frac{b}{2a}\) from both sides
        eq8 = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
        self.play(FadeTransform(eq7, eq8))
        self.wait(0.7)
