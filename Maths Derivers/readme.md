# A tool to enable rapid generation of maths derivation-like videos/shorts

I am currently using this tool for a few YouTube videos. Check out the videos here: https://www.youtube.com/@aryaaskmaths and here: https://www.tiktok.com/@aryaaskmaths

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

This step can also be completd via ChatGPT.

## Create narrations
This can be done with 11Labs using a script such as this one.

```
let's solve this simple linear equation.

subtract 4.

divide by 1, and we're done!.
```
*Remember to add full-stops after each narration to provide a pause*

This step can also be done simply with ChatGPT, by just importing the script with the prompt

Here's a script

{script}

I want you to remove all the maths expression and just focus on the narrations after the semicolon.

Put the narrations in a list separated by full stops and line breaks. e.g.
narration 1.

narration 2.

narration 3.
...

## Import into a video editor and sync narrations with animations

## Add background music