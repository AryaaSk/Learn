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
        lines = [
            "3x + 4 = 7",
            "3x = 3",
            "x = 1"
        ]
        lines = ToLatex(lines)

        Animation(self, lines)