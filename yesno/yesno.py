#!/usr/bin/python

"""
Python prog that helps you choose.
"""

import random

YES = ["Perhaps...",
"It looks like it's a good time to do it.",
"Errrr... yyyy... nnnn...yyeeee.....nnnn... \
errr... yes, I think... or maybe... no, \
definently a no, I mean yes. Yes.",
"The stars read YES.",
"Yup!",
"By all means, go for it.",
"YES!",
"Yes.",
"I would try that, if I where you.",
"Yeehaw!"]
NO = ["Perhaps not...",
"It looks suspicious.",
"Too many unknown variables.",
"The stars read NO.",
"Do, you should not!",
"No way man!",
"NO!",
"No.",
"I wouldn't do that, if I where you.",
"Nah."]
REFUSE = ["Error: Leave me alone...",
"Error: I refuse to say anything right now.",
"Error: I don't feel like working right now.",
"Error: The application you are trying to use \
is currently unavailable for output. \
Error code: 23411009F: I'm on vacation!"]

YESNO = int(random.randrange(3))
if YESNO == 2:
    YESNO = int(random.randrange(3))
    if YESNO == 2:
        INDEX = int(random.randrange(len(REFUSE)))
        print REFUSE[INDEX] + '\n'
        exit(1)
if YESNO == 1:
    INDEX = int(random.randrange(len(YES)))
else:
    INDEX = int(random.randrange(len(NO)))
if YESNO == 1:
    print YES[INDEX] + '\n'
else:
    print NO[INDEX] + '\n'
