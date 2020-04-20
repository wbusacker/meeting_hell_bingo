#!/usr/bin/python3

import random

name_list = [
"\"Sorry I was double muted\"",
"\"Let's circle back\"",
"Someone is asked a question followed by silence",
"\"*Name* is dialing in\"",
"\"Let's take this offline\"",
"Dog barking",
"Kids screaming",
"\"I'll take that action\"",
"Static",
"Someone pressing buttons",
"\"Having Webex issues\"",
"\"Can you see my screen\"",
"\"How do I share my screen?\"",
"\"Can you hear me now\"",
"4+ people talking over each other",
"\"Looks like/I think you're muted\"",
"Someone offers someone else for a task",
"Heavy Breathing",
"\"That's coming up in a couple of charts\"",
"Charts get skipped to answer a question",
"\"Can you repeat that?\" *clearly wasn't listening\"",
"\"Sorry, I was multitasking\"",
"\"Sorry, go ahead *Name*\"",
"\"I'll reach out to/I'll follow up with *Name*\"",
"3 Call in User that are people in the Webex",
"Someone starts talking about the virus/quarantine",
"\"Any questions on the bridge?\"",
"Sirens in the background",
"Eating/plate clinking/bag of chips/assorted dining noises",
"Someone else in our bingo group gets called on to answer question",
"Someone is criticizing presentation/formatting (Not the information)",
"Spend half hour on one chart",
"You were asked a question while briefly away from meeting",
"\"Pass the ball\"",
]

# Build up the list of squares

squares = []

for i in range(0, 25):
    if(i == 12):
        squares.append("Free!")
    else:
        while(1):
            potential = name_list[random.randint(0,len(name_list)-1)]
            if potential not in squares:
                squares.append(potential)
                break

with open("bingo.tex","w") as fh:

    fh.write("""\\documentclass[12pt]{article}
\\usepackage[margin=0.5in]{geometry}
\\usepackage{array}
\\begin{document}

\\begin{tabular}{|m{3cm}|m{3cm}|m{3cm}|m{3cm}|m{3cm}|}""")

    for i in range(0, 25):
        if((i % 5) == 0):
            fh.write("\\\\ \n\\hline\n")
        if((i % 5) != 0):
            fh.write(" & ")
        fh.write(squares[i])

    fh.write("\\\\ \n\\hline\n")

    fh.write("""
    
\\end{tabular}

\\end{document}
    """)


# \\begin{table}[]
# \\begin{tabular}{ |p{3cm}|p{3cm}|p{3cm}|p{3cm}|p{3cm}|   }