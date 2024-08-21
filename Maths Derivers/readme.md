# A tool to enable rapid generation of maths derivation-like videos/shorts

As a subset of the main program, this branch is specifically designed to create derivation-like shorts which take the user from a starting equation/expression to a final desired expression.

For example, this tool could be used to quickly generate a short of solving the following equation

3x + 4 = 7
3x = 3
x = 1

The user will enter the steps and extra information, and the tool should output a script/video complete music and visualisations.

The visualisations will be created via Manim.

## Basic workflow

### Write line and assciated narration
line; narration
3x + 4 = 7; let's solve this simple linear equation
3x = 3; subtract 4
x = 1; divide by 1, and we're done!

### Convert each line to latex
Can be done using tools like [Text2Latex](https://www.text2latex.com/), or just leaving the line will be alright sometimes.

Compile a list of latex objects in python
```python
lines = [
    "3x + 4 = 7",
    "3x = 3",
    "x = 1"
]

def ToLatex(lines):
    latexLines = []
    for line in lines:
        latexLines.append(MathTex(line))
    return latexLines

lines = ToLatex(lines)
```

### Create the MANIM animation

```python
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
        Animation(self, lines)
```

Low quality render to check (can render in high quality once satisfied with result)
```
manim -pql script.py Main
```

*Create narrations with 11Labs, import media into video editor and add background music*