
faq_file_in = "Python_scrips\\faq-text-file.txt"

def main():
    flist = []
    qalist=[]
    with open( faq_file_in, "r") as f:
        file_data = f.read()
        flist = file_data.split("\n")
        
        for line in flist:
            qalist.append(line.split("A."))
        count = 1
        for line in qalist:
            if len(line) > 1:
                line[0] = "<p class=\"faq-body-sub\">Question "+str(count)+":<br>"+line[0][3:]
                line[1] = "Answer "+str(count)+":<br>"+line[1]+"</p>"
                count += 1


        print(qalist)

        f.close()
    with open("Python_scrips\\faq-out.txt", "w") as f:
        f.write("<div class=\"faq-body\">")
        for line in qalist:
            for qa in line:
                f.write(f"{qa}<br>\n")
        f.write("</diva>")

main()