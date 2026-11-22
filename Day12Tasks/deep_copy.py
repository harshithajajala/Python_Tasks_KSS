# Nested Data Independence.A school stores classroom data: classes = [["Math", [30, 35]], ["Science", [25, 28]]] 
# Create a deep copy of this structure. Modify student count in original. 
# Prove that copied data remains unchanged. 
# Explain why deep copy is required here.

import copy

classes = [["Math", [30, 35]], ["Science", [25, 28]]]

backup = copy.deepcopy(classes)

classes[0][1][0] = 50

print("Original:", classes)
print("Backup:", backup)
