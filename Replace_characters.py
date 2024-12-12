#Replacing the words from the user inputs
#write a simple program

#step 1: Start with source

#Assigning the source content as variable
list_source = ["The sun was setting over the horizon, casting a golden hue across the landscape. As the day turned into night, the stars began to twinkle in the sky. The gentle breeze rustled the leaves, creating a soothing melody. As the world quieted down, the creatures of the night emerged. The owl hooted softly, as the crickets chirped in harmony. The moon rose high, illuminating the path with its silvery glow. As the night deepened, the air grew cooler. The silence was profound, as the world seemed to hold its breath. The beauty of the night was mesmerizing, as the stars danced in the vast expanse. The tranquility was a balm to the soul, as the worries of the day faded away. The night was a canvas, painted with dreams and possibilities. As the hours passed, the world slept peacefully, wrapped in the embrace of the night."]
#iterating the for loop in each word
for text in list_source:
    #Using the replace module to execute the replacement characters in the source
    replace_words = text.replace("as", "an").replace("As", "An").split()
    #Print the source
    print(replace_words)
