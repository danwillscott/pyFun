print "This will prompt you for a grade then we will give you the letter grade back this happens 10 times."

def gradeScorePrompt():
	gradeMessage = "Score: {}; Your grade is a {}"
	print "Scores and Grades"
	for x in xrange(0,10):
		userInput = input("Enter a number grade score")
		if userInput >= 90:
			print gradeMessage.format(userInput, "A")
		elif userInput >= 80:
			print gradeMessage.format(userInput, "B")
		elif userInput >= 70:
			print gradeMessage.format(userInput, "C")
		elif userInput >= 60:
			print gradeMessage.format(userInput, "D")
		else:
			print "Your Score is to low!"
	print "End of Program. Bye!"

gradeScorePrompt()