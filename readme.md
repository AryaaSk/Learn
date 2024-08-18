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
- AnimationDescription(narration): Here is a narration script: {narration}

I want to create a small animation comprising of props which look like hand-drawn sketches to visualise this narration. Please provide a description of this animation.

For each part of the animation, also include the section of the narration to speak while that part is being played, and approximate the percentage of the scene at which an animation occurs (e.g. if an animation occurs 30% into a scene, startNarrationPercentage = 0.3). By logic, the startNarrationPercentage of a subsequent narration will always be greater than the startNarrationPercentage of the previous narration.

Return your answer in JSON format { animationDescription: string, narration: string, startNarrationPercentage: number }[]


*We have a clear description of each animation, so now we need to convert that into a format which we can easily create via algorithms*
- Animation(description, height, width}: Here's a description of an animation I would like to create {description}

I want you to parse this description into specific props (images) and their associated movements throughout the duration of the animation, using percentages as time stamps (e.g. if an animation started halfway through the video and ended at the end, startScenePercentage = 0 and endScenePercentage = 1).

Here's an example. Let's say a ball goes from (0, 0) to (30, 30) and then to (20, 20) in the second half of the scene; you'd define a prop as { id: "ball", desciption: "an image of a ball", startingPosition: { x: 0, y: 0 }, showAtScenePercentage: 0.5, removeAtScenePercentage: 1 }, and you'd define the animations as [{ propID: "ball", endPosition: { x: 30, y: 30 }, durationPercentage: 0.25 }, { propID: "ball", endPosition: { x: 20, y: 20 }, durationPercentage: 0.25 }]

Remember, duration percentage within an animation is still based on the overall scene length.

Now in the description given, the max-x and max-y point would be ({width}, {height}); stay within these coordinates but try to use as much of the room available as possible

Please do the same for the description given, returning your response in JSON format using the interfaces below: { props: Prop[], animations: Animation[] }


interface Point {
    x: number;
    y: number;
}

interface Prop {
    id: string;
    description: string;

    startingPosition: Point;
    showAtScenePercentage: number;
    removeAtScenePercentage: number;
}

interface Animation {
    propID: string;

    endPosition: Point;
    durationPercentage: number;
}



*For the virality effect, we'll also need to 'attach' an influential figure to each video, and we can do this by asking LLMs to modify the script in a way that conforms to this figure's speech.
- Transform(narration, figure): I will provide a generic narration, please transform it such that it appears to have been spoken by {figure} while maintaining the original information.

Narration: {narration}


**Viral Video Format**
Pick an influential character and topic.

Start video off with a joke about the topic from the character.

Introduction, sub-topics (explained with complementing visuals) and summary, final outro.

NEED TO GET PEOPLE TO COMMENT:
- JOKES
- MISTAKES (can intentionally tell people to 'spot the mistake'; this will lead to high viewership and commenting)
- Confusion/controversy.





**Another viral idea**
'Educational content' which is simply completely wrong just for humour.