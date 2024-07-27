import os
import shutil


def file_organizer(p_origin,p_destination):

    path_content = os.listdir(path)
    for document in path_content:
        if ".zip" in document:
            if not os.path.isdir(path_destination + "Zip files"):
                os.mkdir(path_destination + "Zip files")
            shutil.move(path+document, path_destination+"Zip files/" + document)
        if ".pdf" in document:
            if not os.path.isdir(path_destination + "Pdf files"):
                os.mkdir(path_destination + "Pdf files")
            shutil.move(path+document, path_destination+"Pdf files/" + document)
        if ".png" in document:
            if not os.path.isdir(path_destination + "Png files"):
                os.mkdir(path_destination + "Png files")
            shutil.move(path+document, path_destination+"Png files/" + document)
        if ".pptx" in document:
            if not os.path.isdir(path_destination + "Pptx files"):
                os.mkdir(path_destination + "Pptx files")
            shutil.move(path + document, path_destination + "Pptx files/" + document)


print("Note that new directories will be opened")
ans = input("Would you like to organize your files ? Y/N : ").lower()
if ans == "y":
    name = os.environ["HOME"]
    path = name + "/Downloads/"
    path_destination = name + "/Documents/"
    file_organizer(path,path_destination)
    print("Your download files are now organized")
elif ans == "n":
    print("Okay")
else:
    print("Enter a valid answer")
        