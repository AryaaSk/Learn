#For now, let's just focus on creating a single scene.
import json

f = open("3script.json", "r")
script = json.load(f)
f.close()

scene = script["scenes"][0]

#we're working with a 1920x1080 canvas
#reserve the header (1920x200) for the title
#this leaves 1920x880 for the subScenes

numberOfSubScenes = len(scene["subScenes"]) #5

#we need to split our area into 5 smaller areas, for now we'll just do this manually as [3, 2] being the number of areas in each row
#this means, the first subscene's top-left corner is at (0, 200) using top-left as (0, 0) and bottom-right as (1920, 1080);
#the subScene has area 640x440, so we need to generate an animation within that frame

subScene = scene["subScenes"][0]
subSceneDimensions = [640, 440] #width, height

#Now within this subScene, we have another title, so we need to reserve the top 100 pixels for that, giving us a remaining area of 640x340

#Title: Molecules in Constant Motion
#Narration: Gas molecules are in continuous, random motion. They travel in straight lines until they collide with other molecules or the walls of their container.

#We will take this narration and use ChatGPT to convert it into a 'storyboard'