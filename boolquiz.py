# A quiz written in python to test truth tables and propositions
# Written By Gordon Potter gordon@gordonpotter.com
# Inspired by http://learnpythonthehardway.org/book/ex28.html
# 
# MIT License
# Copyright (c) 2011 Gordon Potter
# 
# Permission is hereby granted, free of charge, to any person obtaining 
# a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the Software 
# is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
# THE SOFTWARE.

import collections
from random import choice

TruthTable = collections.namedtuple('TruthTable', 'proposition, value', verbose=False)

numberOfQuestionsToAsk = 100

v0  = True and True
v1  = False and True
v2  = 1 == 1 and 2 == 1
v3  = "test" == "test"
v4  = 1 == 1 or 2 != 1
v5  = True and 1 == 1
v6  = False and 0 != 0
v7  = True or 1 == 1
v8  = "test" == "testing"
v9  = 1 != 0 and 2 == 1
v10 = "test" != "testing"
v11 = "test" == 1
v12 = not (True and False)
v13 = not (1 == 1 and 0 != 1)
v14 = not (10 == 1 or 1000 == 1000)
v15 = not (1 != 10 or 3 == 4)
v16 = not ("testing" == "testing" and "Zed" == "Cool Guy")
v17 = 1 == 1 and not ("testing" == 1 or 1 == 0)
v18 = "chunky" == "bacon" and not (3 == 4 or 3 == 3)
v19 = 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")

s0  = "True and True"
s1  = "False and True"
s2  = "1 == 1 and 2 == 1"
s3  = "\"test\" == \"test\""
s4  = "1 == 1 or 2 != 1"
s5  = "True and 1 == 1"
s6  = "False and 0 != 0"
s7  = "True or 1 == 1"
s8  = "\"test\" == \"testing\""
s9  = "1 != 0 and 2 == 1"
s10 = "\"test\" != \"testing\""
s11 = "\"test\" == 1"
s12 = "not (True and False)"
s13 = "not (1 == 1 and 0 != 1)"
s14 = "not (10 == 1 or 1000 == 1000)"
s15 = "not (1 != 10 or 3 == 4)"
s16 = "not (\"testing\" == \"testing\" and \"Zed\" == \"Cool Guy\")"
s17 = "1 == 1 and not (\"testing\" == 1 or 1 == 0)"
s18 = "\"chunky\" == \"bacon\" and not (3 == 4 or 3 == 3)"
s19 = "3 == 3 and not (\"testing\" == \"testing\" or \"Python\" == \"Fun\")"


t0  = TruthTable(s0 , v0 )
t1  = TruthTable(s1 , v1 )
t2  = TruthTable(s2 , v2 )
t3  = TruthTable(s3 , v3 )
t4  = TruthTable(s4 , v4 )
t5  = TruthTable(s5 , v5 )
t6  = TruthTable(s6 , v6 )
t7  = TruthTable(s7 , v7 )
t8  = TruthTable(s8 , v8 )
t9  = TruthTable(s9 , v9 )
t10 = TruthTable(s10, v10)
t11 = TruthTable(s11, v11)
t12 = TruthTable(s12, v12)
t13 = TruthTable(s13, v13)
t14 = TruthTable(s14, v14)
t15 = TruthTable(s15, v15)
t16 = TruthTable(s16, v16)
t17 = TruthTable(s17, v17)
t18 = TruthTable(s18, v18)
t19 = TruthTable(s19, v19)

questionList = [t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19]

# Keep tallies of the correct and incorrect answers
correctAnswers = []
incorrectAnswers = []

def userAnswerToBoolean(input):
    # Converts the input to a boolean value
    # This lets the user use: 
    # Truth, tRuTh, TRUTH, t, T 
    # or 
    # False, fAlSe, FALSE, f, F

    # The default value, random non standard input interpreted as False
    inputValue = False

    # Convert to uppercase to make consistent string
    inputString = input.upper()
    
    if inputString == "T":
        inputValue = True
    elif inputString == "TRUTH":
        inputValue = True
    elif inputString == "F":
        inputValue = False
    elif inputString == "FALSE":
        inputValue = False  
          
    return inputValue

start = raw_input("\nReady for the boolean truth table quiz? \nQuestions to ask: " + str(numberOfQuestionsToAsk) + "\nType truth, or t for Truth, false or f for False\nHit RETURN to continue, CTRL-C to exit quiz. \n")

# Loop through the number of questions to ask
# each time asking a random question
for x in range(1,numberOfQuestionsToAsk):
    questionTuple = choice(questionList)
    answer = raw_input("Question " + str(x) + ": \n" + questionTuple[0] + "\n")

    
    theAnswer = userAnswerToBoolean(answer)
    
    if (questionTuple[1] == theAnswer):
        correctAnswers.append(questionTuple)
        print "Correct! " + questionTuple[0] + " = " + str(questionTuple[1])
        print "\n"
    else:
        incorrectAnswers.append(questionTuple)        
        print "Bzzt! Wrong answer: " + questionTuple[0] + " = " + str(questionTuple[1])
        print "\n"

print "\n"
print "Boolean Quiz completed \n"

print "\n"
print "###############################################"
print "Questions answered correctly \n"
print "###############################################"
print "\n"

for item in correctAnswers:
    print item
    # print "\n"

print "\n"
print "###############################################"
print "Questions answered incorrectly \n"
print "###############################################"
print "\n"

for item in incorrectAnswers:
    print item
    # print "\n"
