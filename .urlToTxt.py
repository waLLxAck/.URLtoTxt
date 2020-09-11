import glob

arrayFileNames = glob.glob("*.url")
strUrl = ""

for x in arrayFileNames:
    with open(x, "r") as infile:
        for line in infile:
            if (line.startswith('URL')):
                strUrl += "File Name: "+ x[:-4] + "\nURL: " + line[4:] +"\n"
                break

text_file = open("Name and URL.txt", "w")
n = text_file.write(strUrl)
text_file.close()
