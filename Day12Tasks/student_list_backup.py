# student list Backup.A teacher has a list of student marks: 
# marks = [50, 60, 70, 80] 
# She creates a backup using assignment,backup = marks .Modify the first element in marks,Observe the change in backup, Explain why both lists are affected.

marks = [50, 60, 70, 80]

backup = marks

marks[0] = 100

print("Original:", marks)
print("Backup:", backup)

