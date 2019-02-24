import os,sys
import datetime
from prettytable import PrettyTable
from us01_ny import us01_date_b4_now
from us_rs import us_rs
from us42_ny import us42_legit_date, us42_tsk01_is_legit_date
<<<<<<< HEAD
from us02_sp import us02_birth_before_marriage
from us35_sp import us35_ppl_born_last_30days
# import US04
# import US07
=======
import us04_an
import us07_an
>>>>>>> b7a43d4f463d0c2ddb5ea80bc95fd9dcf0a4fae5
# !To developers: please call all your user story methods in either print_all() or 
# validate_all() as the name implies
FILENAME="GEDCOM_Ashish.ged"

class Gedcom():
    def __init__(self, filename):
        ged=open(filename,'r')
        a=ged.read()
        b=a.split("\n")
        #print(b)
        self.ind={}
        self.family={}
        matrix = self._preprocess_file(b)
        self._matrix_to_dict(matrix) 

    def _preprocess_file(self, b):
        c=[]
        lineNumber = 0
        error = []
        finalize=[]
        check={'0':["HEAD","NOTE","TRLR","INDI","FAM"],
        '1':["NAME","SEX","BIRT","DEAT","FAMC","FAMS","MARR","HUSB","WIFE","CHIL","DIV",],
        '2':["DATE"]}
        for i in range(0,len(b)):
            #print(str(i) +" "+b[i])
            if b[i]=="":
                c.append(["","","",i+1])
            else:
                space=b[i][2:].find(" ")
                #print(space)
                if space==-1:
                    #print(b[i])
                    #print("no space")
                    c.append([b[i][0],b[i][2:],"",i+1])
                else:
                    if b[i][space+3:].isspace():
                        #print(b[i])
                        #print("spaces removed")
                        c.append([b[i][0],b[i][2:2+space],"",i+1])
                    else:
                        c.append([b[i][0],b[i][2:2+space],b[i][space+3:],i+1])

        print(c)

        for i in range(0,len(c)):
            lineNumber += 1
            if(c[i][0]=="" and c[i][1]=="" and c[i][2]==""):
                temporary="temporary"#used as a place holder
            else:
                print("-->"+b[i])
                if c[i][0]=='0':
                    if (c[i][1] in check[c[i][0]]) and (c[i][1]=="HEAD" or c[i][1]=="TRLR" or c[i][1]=="NOTE"):
                        if (c[i][1]=="HEAD" or c[i][1]=="TRLR") and (c[i][2]==""):
                            #print("valid\n")
                            print("<--"+c[i][0]+"|"+c[i][1]+"|Y"+c[i][2]+"\n")
                            finalize.append(c[i])
                        elif c[i][1]=="NOTE" and c[i][2]!="":
                            #print("valid\n")
                            print("<--"+c[i][0]+"|"+c[i][1]+"|Y|"+c[i][2]+"\n")
                            finalize.append(c[i])
                        else:
                            #print("invalid")
                            if c[i][2]=="":
                                print("<--"+c[i][0]+"|"+c[i][1]+"|N"+c[i][2]+"\n")
                                error.append(lineNumber)
                                
                            else:
                                print("<--"+c[i][0]+"|"+c[i][1]+"|N|"+c[i][2]+"\n")
                                error.append(lineNumber)
                    elif (c[i][2] in check[c[i][0]]) and (c[i][2]=="INDI" or c[i][2]=="FAM"):
                        #print("valid\n")
                        print("<--"+c[i][0]+"|"+c[i][2]+"|Y|"+c[i][1]+"\n")
                        temp=[c[i][0],c[i][2],c[i][1],i+1]
                        finalize.append(temp)
                    else:
                        #print("invalid\n")
                        if c[i][2]=="":
                            print("<--"+c[i][0]+"|"+c[i][1]+"|N"+c[i][2]+"\n")
                            error.append(lineNumber)
                        else:
                            print("<--"+c[i][0]+"|"+c[i][1]+"|N|"+c[i][2]+"\n")
                            error.append(lineNumber)
                elif (c[i][0]=='1') and (c[i][1] in check[c[i][0]]):
                    if (c[i][1]=="BIRT" or c[i][1]=="DEAT" or c[i][1]=="MARR" or c[i][1]=="DIV" ) and (c[i][2]==""):
                        #print("valid\n")
                        print("<--"+c[i][0]+"|"+c[i][1]+"|Y"+c[i][2]+"\n")
                        finalize.append(c[i])
                    elif (c[i][1]!="BIRT" or c[i][1]!="DEAT" or c[i][1]!="MARR" or c[i][1]!="DIV" ):
                        if (c[i][1]=="SEX"):
                            if (c[i][2]=='M' or c[i][2]=='F'):
                                #print("valid\n")
                                print("<--"+c[i][0]+"|"+c[i][1]+"|Y|"+c[i][2]+"\n")
                                finalize.append(c[i])
                            else:
                                #print("invalid\n")
                                if c[i][2]=="":
                                    print("<--"+c[i][0]+"|"+c[i][1]+"|N"+c[i][2]+"\n")
                                    error.append(lineNumber)
                                else:
                                    print("<--"+c[i][0]+"|"+c[i][1]+"|N|"+c[i][2]+"\n")
                                    error.append(lineNumber)
                        else:
                            #print("valid\n")
                            print("<--"+c[i][0]+"|"+c[i][1]+"|Y|"+c[i][2]+"\n")
                            finalize.append(c[i])
                elif (c[i][0]=='2') and (c[i][1] in check[c[i][0]]):
                    #print("valid\n")
                    print("<--"+c[i][0]+"|"+c[i][1]+"|Y|"+c[i][2]+"\n")
                    finalize.append(c[i])
                else:
                    #print("invalid\n")
                    if c[i][2]=="":
                        print("<--"+c[i][0]+"|"+c[i][1]+"|N"+c[i][2]+"\n")
                        error.append(lineNumber)
                    else:
                        print("<--"+c[i][0]+"|"+c[i][1]+"|N|"+c[i][2]+"\n")
                        error.append(lineNumber)

        #print(finalize)
        return finalize
    
    def _matrix_to_dict(self, finalize):
        check={'0':["HEAD","NOTE","TRLR","INDI","FAM"],
        '1':["NAME","SEX","BIRT","DEAT","FAMC","FAMS","MARR","HUSB","WIFE","CHIL","DIV",],
        '2':["DATE"]}
        i=0
        while i<len(finalize):
            if finalize[i][0]=="0" and finalize[i][1]=="INDI":
                self.ind[finalize[i][2]]={}
                j=i+1
                while not(finalize[j][0]=="0" and (finalize[j][1]=="INDI" or finalize[j][1]=="FAM")) :
                    if finalize[j][0]=='1' and (finalize[j][1] in check[finalize[j][0]]):
                        if (finalize[j][1]=="BIRT" or finalize[j][1]=="DEAT"):
                            self.ind[finalize[i][2]][finalize[j][1]+"_"+finalize[j+1][1]]=[finalize[j+1][2],finalize[j+1][3]]#changed
                            #print(ind)
                            j=j+2
                        elif (finalize[j][1]=="FAMC" or finalize[j][1]=="FAMS"):
                            if finalize[j][1] in self.ind[finalize[i][2]]:
                                self.ind[finalize[i][2]][finalize[j][1]].append([finalize[j][2],finalize[j][3]])#ch
                            else:
                                self.ind[finalize[i][2]][finalize[j][1]]=[]
                                self.ind[finalize[i][2]][finalize[j][1]].append([finalize[j][2],finalize[j][3]])#ch
                            j=j+1
                        else:
                            self.ind[finalize[i][2]][finalize[j][1]]=[finalize[j][2],finalize[j][3]]#ch
                            #print(ind)
                            j=j+1
                    else:
                        j=j+1
                        if(j>=len(finalize)):
                            break
                if not("DEAT_DATE" in self.ind[finalize[i][2]]):
                    self.ind[finalize[i][2]]["DEAT_DATE"]="NA"
                    self.ind[finalize[i][2]]["ALIVE"]="True"
                    dea_date=datetime.datetime.now()
                else:
                    isLegitDate = us42_tsk01_is_legit_date(self.ind[finalize[i][2]]["DEAT_DATE"][0])
                    if(isLegitDate == True):
                        dea_date=datetime.datetime.strptime(self.ind[finalize[i][2]]["DEAT_DATE"][0],'%d %b %Y')
                        self.ind[finalize[i][2]]["DEAT_DATE"]=[dea_date.strftime('%Y-%m-%d'),finalize[i][3]]
                    else:
                        dea_date = "Invalid"
                        self.ind[finalize[i][2]]["DEAT_DATE"]= "Invalid"
                    self.ind[finalize[i][2]]["ALIVE"]="False"

                if not("BIRT_DATE" in self.ind[finalize[i][2]]):
                    self.ind[finalize[i][2]]["BIRT_DATE"]="NA"
                    self.ind[finalize[i][2]]["AGE"]="NA"
                else:
                    isLegitDate = us42_tsk01_is_legit_date(self.ind[finalize[i][2]]["BIRT_DATE"][0])
                    if(isLegitDate == True):
                        con_date=datetime.datetime.strptime(self.ind[finalize[i][2]]["BIRT_DATE"][0],'%d %b %Y')
                        self.ind[finalize[i][2]]["BIRT_DATE"]=[con_date.strftime('%Y-%m-%d'),finalize[i][3]]
                        if (dea_date != "Invalid"):
                            self.ind[finalize[i][2]]["AGE"]=int(((dea_date)-(con_date)).days/365)
                        else:
                            self.ind[finalize[i][2]]["AGE"]="Invalid"
                    else:
                        self.ind[finalize[i][2]]["BIRT_DATE"]="Invalid"
                        self.ind[finalize[i][2]]["AGE"]="Invalid"
                
                if not("FAMC" in self.ind[finalize[i][2]]):
                    self.ind[finalize[i][2]]["FAMC"]="None"

                if not("FAMS" in self.ind[finalize[i][2]]):
                    self.ind[finalize[i][2]]["FAMS"]="NA"

                i=j
            elif finalize[i][0]=="0" and finalize[i][1]=="FAM":
                self.family[finalize[i][2]]={}
                j=i+1
                while not(finalize[j][0]=="0" and (finalize[j][1]=="INDI" or finalize[j][1]=="FAM")):
                    if finalize[j][0]=='1' and (finalize[j][1] in check[finalize[j][0]]):
                        if (finalize[j][1]=="MARR" or finalize[j][1]=="DIV"):
                            self.family[finalize[i][2]][finalize[j][1]+"_"+finalize[j+1][1]]=[finalize[j+1][2],finalize[j+1][3]]#ch
                            #print(family)
                            j=j+2
                        elif (finalize[j][1]=="CHIL"):
                            if finalize[j][1] in self.family[finalize[i][2]]:
                                self.family[finalize[i][2]][finalize[j][1]].append([finalize[j][2],finalize[j][3]])#ch
                            else:
                                self.family[finalize[i][2]][finalize[j][1]]=[]
                                self.family[finalize[i][2]][finalize[j][1]].append([finalize[j][2],finalize[j][3]])#ch
                            j=j+1
                        else:
                            self.family[finalize[i][2]][finalize[j][1]]=[finalize[j][2],finalize[j][3]]#ch
                            #print(family)
                            j=j+1
                    else:
                        j=j+1
                        if(j>=len(finalize)):
                            break
                if not("MARR_DATE" in self.family[finalize[i][2]]):
                    self.family[finalize[i][2]]["MARR_DATE"]="NA"
                else:
                    isLegitDate = us42_tsk01_is_legit_date(self.family[finalize[i][2]]["MARR_DATE"][0])
                    if(isLegitDate == True):
                        con_date=datetime.datetime.strptime(self.family[finalize[i][2]]["MARR_DATE"][0],'%d %b %Y')
                        self.family[finalize[i][2]]["MARR_DATE"]=[con_date.strftime('%Y-%m-%d'),finalize[i][3]]#ch
                    else:
                        self.family[finalize[i][2]]["MARR_DATE"]="Invalid"
                if not("DIV_DATE" in self.family[finalize[i][2]]):
                    self.family[finalize[i][2]]["DIV_DATE"]="NA"
                else:
                    isLegitDate = us42_tsk01_is_legit_date(self.family[finalize[i][2]]["DIV_DATE"][0])
                    if(isLegitDate == True):
                        con_date=datetime.datetime.strptime(self.family[finalize[i][2]]["DIV_DATE"][0],'%d %b %Y')
                        self.family[finalize[i][2]]["DIV_DATE"]=[con_date.strftime('%Y-%m-%d'),finalize[i][3]]#ch
                    else:
                        self.family[finalize[i][2]]["DIV_DATE"]="Invalid"
                i=j
            else:
                i=i+1
        print(self.ind)
        print(self.family)

    def print_gedcom(self):
        indi = PrettyTable()
        indi.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
        fam = PrettyTable()
        fam.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]

        for key, values in self.ind.items():
            arr = list()
            
            arr.append(key)
            if values.__contains__("NAME"):
                arr.append (self.ind[key]["NAME"][0])
            else:
                arr.append("NA")
            if values.__contains__("SEX"):
                arr.append (self.ind[key]["SEX"][0])
            else:
                arr.append("NA")
            if values.__contains__("BIRT_DATE"):
                arr.append (self.ind[key]["BIRT_DATE"][0] if (self.ind[key]["BIRT_DATE"]!='NA' and self.ind[key]["BIRT_DATE"]!='Invalid') else self.ind[key]["BIRT_DATE"])
            else:
                arr.append("NA")
            if values.__contains__("AGE"):
                arr.append (self.ind[key]["AGE"])
            else:
                arr.append("NA")
            if values.__contains__("ALIVE"):
                arr.append (self.ind[key]["ALIVE"])
            else:
                arr.append("NA")
            if values.__contains__("DEAT_DATE"):
                arr.append (self.ind[key]["DEAT_DATE"][0] if (self.ind[key]["DEAT_DATE"]!='NA' and self.ind[key]["DEAT_DATE"]!='Invalid') else self.ind[key]["DEAT_DATE"])
            else:
                arr.append("NA")
            if values.__contains__("FAMC"):
                arr.append (self.ind[key]["FAMC"])
            else:
                arr.append("NA")
            if values.__contains__("FAMS"):
                arr.append (self.ind[key]["FAMS"])
            else:
                arr.append("NA")
            
            indi.add_row(arr)
            
        for key, values  in self.family.items():
            arr = list()
            husID = ""
            wifeID = ""
            arr.append(key)
            if values.__contains__("MARR_DATE"):
                arr.append (self.family[key]["MARR_DATE"][0] if (self.family[key]["MARR_DATE"]!='NA' and self.family[key]["MARR_DATE"]!='Invalid') else self.family[key]["MARR_DATE"])
            else:
                arr.append("NA")
            if values.__contains__("DIV_DATE"):
                arr.append (self.family[key]["DIV_DATE"][0] if (self.family[key]["DIV_DATE"]!='NA' and self.family[key]["DIV_DATE"]!='Invalid') else self.family[key]["DIV_DATE"])
            else:
                arr.append("NA")
            if values.__contains__("HUSB"):
                arr.append (self.family[key]["HUSB"][0])
                husID = self.family[key]["HUSB"][0]
                arr.append(self.ind[husID]["NAME"])
            else:
                arr.append("NA")
                arr.append("NA")
            
            if values.__contains__("WIFE"):
                arr.append (self.family[key]["WIFE"][0])
                wifeID = self.family[key]["WIFE"][0]
                arr.append(self.ind[wifeID]["NAME"])
            else:
                arr.append("NA")
                arr.append("NA")
            
            if values.__contains__("CHIL"):
                arr.append (self.family[key]["CHIL"])
            else:
                arr.append("NA")
            fam.add_row(arr)
        #print(arr)

        print("Individuals")
        print(indi)
        print("Family")
        print(fam)
        # print(error)

    # Call your user story method here if it is related to search and display
    def print_all(self):
        self.print_gedcom()
        #User Story 35
        us35_ppl_born_last_30days(self.ind, self.family)

    # Call your user story method here if it is related to search and validate
    def validate_all(self):
        # User Story 01
        #us01_date_b4_now(self.ind, self.family)
<<<<<<< HEAD

        # User Story 02
        us02_birth_before_marriage(self.ind, self.family)



        # User Story 7
        US04.parse_data_04(self.family)
        # US07.parse_data_07(self.ind)
        try:
            val_us_07 = us07_rs.siblingCount(self.family)
            if val_us_07 is True:
                print("Userstory 7 successful")
        except ValueError as err:
            print(err)
=======
        # User Story 4 and 7
        us04_an.parse_data_04(self.family)
        us07_an.parse_data_07(self.ind)
        
>>>>>>> b7a43d4f463d0c2ddb5ea80bc95fd9dcf0a4fae5
        # User Story 42
        us42_legit_date(self.ind, self.family)
        # User Story 15
        try:
            test_val_15 = us_rs.siblingCount(self.family)
            if(test_val_15):
                print("Userstory 15 is Successful")
        except ValueError as err:
            print(err)
        except TypeError as err:
            print(err)
<<<<<<< HEAD
        
=======
        # User Story 02
        #us02_birth_before_marriage(self.ind, self.family)
>>>>>>> b7a43d4f463d0c2ddb5ea80bc95fd9dcf0a4fae5
        

def main():
    gedcom = Gedcom("My-Family-27-Jan-2019-275.ged")
    gedcom.print_all()
    gedcom.validate_all()

if __name__ == '__main__':
    main()
