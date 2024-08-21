from manim import *

def ToLatex(lines):
    latexLines = []
    for line in lines:
        latexLines.append(MathTex(line))
    return latexLines

def Animation(scene, lines):
    scene.play(Write(lines[0])) #assumes len(lines) > 0
    scene.wait(1)

    i = 1
    while i < len(lines):
        scene.play(ReplacementTransform(lines[i - 1], lines[i]))
        scene.wait(1)
        i += 1






class Main(Scene):
    def construct(self):
        # Expression 1
        expr1 = MathTex(r"\frac{d}{dx} \sin(x)", "=", r"\cos(x)")
        self.play(Write(expr1))
        self.wait(1)

        # Fade out first expression
        self.play(FadeOut(expr1))
        self.wait(1)
        
        # Expression 2
        expr2 = MathTex(r"\frac{d}{dx} \sin(x)")
        self.play(Write(expr2))
        self.wait(1)

        # Transform to Expression 3
        expr3 = MathTex(r"= \lim_{h \to 0}", r"\frac{\sin(x + h) - \sin(x)}{h}")
        self.play(Transform(expr2, expr3))
        self.wait(1)

        # Transform to Expression 4
        expr4 = MathTex(r"= \lim_{h \to 0}", r"\frac{\sin(x)\cos(h) + \cos(x)\sin(h) - \sin(x)}{h}")
        self.play(Transform(expr2, expr4))
        self.wait(1)

        # Transform to Expression 5
        expr5 = MathTex(r"= \lim_{h \to 0}", r"\frac{\sin(x)\cos(h) - \sin(x) + \cos(x)\sin(h)}{h}")
        self.play(Transform(expr2, expr5))
        self.wait(1)

        # Transform to Expression 6
        expr6 = MathTex(r"= \lim_{h \to 0}", r"\sin(x) \cdot \frac{\cos(h) - 1}{h} + \cos(x) \cdot \frac{\sin(h)}{h}")
        self.play(Transform(expr2, expr6))
        self.wait(1)

        # Transform to Expression 7
        expr7 = MathTex(r"= \lim_{h \to 0}", r"\sin(x) \cdot \frac{1 - \frac{h^2}{2!} + \frac{h^4}{4!} \dots - 1}{h} + \cos(x) \cdot \frac{h - \frac{h^3}{3!} + \frac{h^5}{5!} \dots}{h}")
        self.play(Transform(expr2, expr7))
        self.wait(1)

        # Transform to Expression 8
        expr8 = MathTex(r"= \lim_{h \to 0}", r"\sin(x) \cdot \frac{- \frac{h^2}{2!} + \frac{h^4}{4!} \dots}{h} + \cos(x) \cdot \frac{h - \frac{h^3}{3!} + \frac{h^5}{5!} \dots}{h}")
        self.play(Transform(expr2, expr8))
        self.wait(1)

        # Transform to Expression 9
        expr9 = MathTex(r"= \lim_{h \to 0}", r"\sin(x) \cdot \left(-\frac{h}{2!} + \frac{h^3}{4!} \dots \right) + \cos(x) \cdot \left(1 - \frac{h^2}{3!} + \frac{h^4}{5!} \dots \right)")
        self.play(Transform(expr2, expr9))
        self.wait(1)

        # Transform to Expression 10
        expr10 = MathTex(r"= \sin(x) \cdot (0 + 0 \dots) + \cos(x) \cdot (1 - 0 + 0 \dots)")
        self.play(Transform(expr2, expr10))
        self.wait(1)

        # Transform to Expression 11
        expr11 = MathTex(r"= \sin(x) \cdot 0 + \cos(x) \cdot 1")
        self.play(Transform(expr2, expr11))
        self.wait(1)

        # Transform to Expression 12
        expr12 = MathTex(r"= \cos(x)")
        self.play(Transform(expr2, expr12))
        self.wait(1)

        # Fade out final expression and display result
        self.play(FadeOut(expr2))
        expr13 = MathTex(r"\frac{d}{dx} \sin(x)", "=", r"\cos(x)")
        self.play(Write(expr13))
        self.wait(2)