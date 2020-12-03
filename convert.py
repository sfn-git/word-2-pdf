from docx2pdf import convert
import easygui
import os

dir = easygui.diropenbox()

for filename in os.listdir(dir):
    if filename.endswith(".docx") or filename.endswith(".doc"):
        oldName = os.path.join(dir,filename)
        newName = filename.rsplit('.',1)[0] + ".pdf"
        convert(oldName)