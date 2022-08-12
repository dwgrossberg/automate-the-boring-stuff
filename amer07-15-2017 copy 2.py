import os

for folderName, subfolders, filenames in os.walk("/Users/dan/nips"):
	print("the folder is " + folderName)
	print("the subfolders in " + folderName + " are: " + str(subfolders))
	print("the filenames in " + folderName + " are: " + str(filenames))
	print()

	for subfolder in subfolders:
            print(subfolder)

        for file in filenames:
            if file.endswith(".txt"):
                shutil.copy(os.join(folderName, file), os.join(folderName, file + ".backup"))
