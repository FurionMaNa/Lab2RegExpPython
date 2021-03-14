from ParseClass import ParseClass


class FileWorkClass:

    def ReadFile(file):
        f = open(file, "r", encoding="utf8")
        str = ""
        dict= {}
        for i in f.read():
            if (ParseClass.parsing(i)):
                str += i
            elif (ParseClass.parsing(str)):
                if (dict.get(str) == None):
                    dict[str] = 1
                else:
                    dict[str]+=1
                str = ""
        if (len(str) >0 and ParseClass.parsing(str)):
            if (dict.get(str) == None):
                dict[str] = 1
            else:
                dict[str] += 1
        return dict

    def WriteFile(file, dict):
        f = open(file, "w", encoding='utf-8')
        for i in dict:
            f.write(i[0] + " = " + str(i[1]) + "\n")
        f.close()