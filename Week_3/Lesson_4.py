import matplotlib.pyplot as plt

hours_studied = [1, 1.5, 2, 2.5, 3, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5]
breaks_taken = [0, 2, 1, 3, 0, 1, 2, 0, 3, 0, 2, 1, 3, 0, 2] 
exam_scores = [52, 54, 57, 59, 63, 67, 72, 76, 78, 82, 85, 88, 90, 93, 95]

plt.scatter(hours_studied, exam_scores, label='Hours Studied', color='c', marker='*')
plt.scatter(breaks_taken, exam_scores, label='Breaks Taken', color='m', marker='o')
plt.title('Exam Scores Given Hours Studied and Breaks Taken')
plt.xlabel('Number of Hours Studied or Breaks Taken')
plt.ylabel('Exam Scores')
plt.grid(True)
plt.legend()


plt.show()