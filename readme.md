A tool which allows you to rapidly create high quality educational videos with a simple topic prompt.

The tool will generate animations with props that look hand-drawn with a stop-motion style.

Pipeline:
- User produces prompt, e.g. Kinetic Theory of Gases

- Content(prompt): What is {prompt}; output the response in markdown.

- Script(content): Split the following script into individual scenes with narration. Under each title and subtitle (marked with ## and ### respectively) please include scenes as a list: {content}. Return answer in JSON format provided by the Video interface given below.

interface Introduction {
    title: string;
    narration: string;
}

interface Scene {
    title: string;
    subScenes: { subtitle: string, narration: string }[];
}

interface Summary {
    narration: string;
}

interface Video {
    introduction: Introduction;
    scenes: Scene[];
    summary: Summary
}

Content: {content}


*Now we have the script, we need to generate the hand-drawn sketches and animations*
- Animation(narration): Here is a narration script: {narration}

I want to create a small animation comprising of props which look like hand-drawn sketches to visualise this narration. Please provide a description of this animation.

For each part of the animation, also include the section of the narration to speak while that part is being played. Return your answer in JSON format { animationDescription: string, narration: string }[]