score = []
x = int(input('student in class'))
for i in range(x):
    y = int(input("student score"))
    score.append(int(y))
print(score)
print("the average score is" , sum(score)/x)
print(int(max(score)) , "is the higest score")
print(int(min(score)), "is the lowest score")

