import os,sys
import datetime
from prettytable import PrettyTable
from us_ny import *
from us_rs import us_rs
from userstories_sp import *
from userstories_an import *
# !To developers: please call all your user story methods in either print_all() or 
# validate_all() as the name implies
FILENAME="My-Family-27-Jan-2019-275.ged"
#FILENAME = "GEDCOM_input.ged"

class Gedcom():
    
    def __init__(self, filename):
        ged=open(filename,'r')
        a=ged.read()
        b=a.split("\n")
        #print(b)
        self.tagCheck = []
        self.ind={}
        self.family={}
        self.family_obj = {}
        matrix = self._preprocess_file(b)
        self._matrix_to_dict(matrix) 

    def _debug_print(self):
        for i in range(0,len(self.tagCheck)):
            print(self.tagCheck[i])
        for x, y in self.ind.items():
            print(x, y)
        for x, y in self.family.items():
            print(x, y)

    def _preprocess_file(self, b):
        c=[]      
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

        # print(c)
        for i in range(0,len(c)):
            if(c[i][0]=="" and c[i][1]=="" and c[i][2]==""):
                temporary="temporary"#used as a place holder
            else:
                self.tagCheck.append("-->"+b[i])
                if c[i][0]=='0':
                    if (c[i][1] in check[c[i][0]]) and (c[i][1]=="HEAD" or c[i][1]=="TRLR" or c[i][1]=="NOTE"):
                        if (c[i][1]=="HEAD" or c[i][1]=="TRLR") and (c[i][2]==""):
                            #print("valid\n")
                            self.tagCheck.append("<--"+c[i][0]+"|"+c[i][1]+"|Y"+c[i][2]+"\n")
                            finalize.append(c[i])
                        elif c[i][1]=="NOTE" and c[i][2]!="":
                            #print("valid\n")
                            self.tagCheck.append("<--"+c[i][0]+"|"+c[i][1]+"|Y|"+c[i][2]+"\n")
                            finalize.append(c[i])
                        else:
                            #print("invalid")
                            if c[i][2]=="":
                                self.tagCheck.append("<--"+c[i][0]+"|"+c[i][1]+"|N"+c[i][2]+"\n")                              
                            else:
                                self.tagCheck.append("<--"+c[i][0]+"|"+c[i][1]+"|N|"+c[i][2]+"\n")
                    elif (c[i][2] in check[c[i][0]]) and (c[i][2]=="INDI" or c[i][2]=="FAM"):
                        #print("valid\n")
                        self.tagCheck.append("<--"+c[i][0]+"|"+c[i][2]+"|Y|"+c[i][1]+"\n")
                        temp=[c[i][0],c[i][2],c[i][1],i+1]
                        finalize.append(temp)
                    else:
                        #print("invalid\n")
                        if c[i][2]=="":
                            self.tagCheck.append("<--"+c[i][0]+"|"+c[i][1]+"|N"+c[i][2]+"\n")
                        else:
                            self.tagCheck.append("<--"+c[i][0]+"|"+c[i][1]+"|N|"+c[i][2]+"\n")
                elif (c[i][0]=='1') and (c[i][1] in check[c[i][0]]):
                    if (c[i][1]=="BIRT" or c[i][1]=="DEAT" or c[i][1]=="MARR" or c[i][1]=="DIV" ) and (c[i][2]==""):
                        #print("valid\n")
                        self.tagCheck.append("<--"+c[i][0]+"|"+c[i][1]+"|Y"+c[i][2]+"\n")
                        finalize.append(c[i])
                    elif (c[i][1]!="BIRT" or c[i][1]!="DEAT" or c[i][1]!="MARR" or c[i][1]!="DIV" ):
                        if (c[i][1]=="SEX"):
                            if (c[i][2]=='M' or c[i][2]=='F'):
                                #print("valid\n")
                                self.tagCheck.append("<--"+c[i][0]+"|"+c[i][1]+"|Y|"+c[i][2]+"\n")
                                finalize.append(c[i])
                            else:
                                #print("invalid\n")
                                if c[i][2]=="":
                                    self.tagCheck.append("<--"+c[i][0]+"|"+c[i][1]+"|N"+c[i][2]+"\n")
                                else:
                                    self.tagCheck.append("<--"+c[i][0]+"|"+c[i][1]+"|N|"+c[i][2]+"\n")
                        else:
                            #print("valid\n")
                            self.tagCheck.append("<--"+c[i][0]+"|"+c[i][1]+"|Y|"+c[i][2]+"\n")
                            finalize.append(c[i])
                elif (c[i][0]=='2') and (c[i][1] in check[c[i][0]]):
                    #print("valid\n")
                    self.tagCheck.append("<--"+c[i][0]+"|"+c[i][1]+"|Y|"+c[i][2]+"\n")
                    finalize.append(c[i])
                else:
                    #print("invalid\n")
                    if c[i][2]=="":
                        self.tagCheck.append("<--"+c[i][0]+"|"+c[i][1]+"|N"+c[i][2]+"\n")
                    else:
                        self.tagCheck.append("<--"+c[i][0]+"|"+c[i][1]+"|N|"+c[i][2]+"\n")

        #print(finalize)
        return finalize
    def storeFam(self):
        return self.family_obj
    def storeInd(self):
        return self.ind
    def _matrix_to_dict(self, finalize):
        check={'0':["HEAD","NOTE","TRLR","INDI","FAM"],
        '1':["NAME","SEX","BIRT","DEAT","FAMC","FAMS","MARR","HUSB","WIFE","CHIL","DIV",],
        '2':["DATE"]}
        i=0
        while i<len(finalize):
            if finalize[i][0]=="0" and finalize[i][1]=="INDI":
                #User story 22
                if finalize[i][2] in self.ind :
                    print("ERROR US22 for ID  "+finalize[i][2]+": All individual IDs should be unique and all family IDs should be unique")
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
                        self.ind[finalize[i][2]]["DEAT_DATE"]=[dea_date.strftime('%Y-%m-%d'),self.ind[finalize[i][2]]["DEAT_DATE"][1]]
                    else:
                        dea_date = "Invalid"
                        self.ind[finalize[i][2]]["DEAT_DATE"]= ["Invalid",self.ind[finalize[i][2]]["DEAT_DATE"][1]]
                    self.ind[finalize[i][2]]["ALIVE"]="False"

                if not("BIRT_DATE" in self.ind[finalize[i][2]]):
                    self.ind[finalize[i][2]]["BIRT_DATE"]="NA"
                    self.ind[finalize[i][2]]["AGE"]="NA"
                    self.ind[finalize[i][2]]["ALIVE"]="False" #changed
                else:
                    isLegitDate = us42_tsk01_is_legit_date(self.ind[finalize[i][2]]["BIRT_DATE"][0])
                    if(isLegitDate == True):
                        con_date=datetime.datetime.strptime(self.ind[finalize[i][2]]["BIRT_DATE"][0],'%d %b %Y')
                        self.ind[finalize[i][2]]["BIRT_DATE"]=[con_date.strftime('%Y-%m-%d'),self.ind[finalize[i][2]]["BIRT_DATE"][1]]
                        if (dea_date != "Invalid"):
                            self.ind[finalize[i][2]]["AGE"]=int(((dea_date)-(con_date)).days/365.25)
                        else:
                            self.ind[finalize[i][2]]["AGE"]="Invalid"
                    else:
                        self.ind[finalize[i][2]]["BIRT_DATE"]=["Invalid",self.ind[finalize[i][2]]["BIRT_DATE"][1]]
                        self.ind[finalize[i][2]]["AGE"]="Invalid"
                
                if not("FAMC" in self.ind[finalize[i][2]]):
                    self.ind[finalize[i][2]]["FAMC"]="None"

                if not("FAMS" in self.ind[finalize[i][2]]):
                    self.ind[finalize[i][2]]["FAMS"]="NA"

                if not("NAME" in self.ind[finalize[i][2]]):
                    self.ind[finalize[i][2]]["NAME"]="NA"
                
                i=j
            elif finalize[i][0]=="0" and finalize[i][1]=="FAM":
                #User story 22
                if finalize[i][2] in self.family :
                    print("ERROR US22 for ID  "+finalize[i][2]+": All individual IDs should be unique and all family IDs should be unique")
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
                        self.family[finalize[i][2]]["MARR_DATE"]=[con_date.strftime('%Y-%m-%d'),self.family[finalize[i][2]]["MARR_DATE"][1]]#ch
                    else:
                        self.family[finalize[i][2]]["MARR_DATE"]=["Invalid",self.family[finalize[i][2]]["MARR_DATE"][1]]
                if not("DIV_DATE" in self.family[finalize[i][2]]):
                    self.family[finalize[i][2]]["DIV_DATE"]="NA"
                else:
                    isLegitDate = us42_tsk01_is_legit_date(self.family[finalize[i][2]]["DIV_DATE"][0])
                    if(isLegitDate == True):
                        con_date=datetime.datetime.strptime(self.family[finalize[i][2]]["DIV_DATE"][0],'%d %b %Y')
                        self.family[finalize[i][2]]["DIV_DATE"]=[con_date.strftime('%Y-%m-%d'),self.family[finalize[i][2]]["DIV_DATE"][1]]#ch
                    else:
                        self.family[finalize[i][2]]["DIV_DATE"]=["Invalid",self.family[finalize[i][2]]["DIV_DATE"][1]]
                i=j
            else:
                i=i+1
    
        self.family_obj = self.family
        # !Should disable _debug_print at the end of each sprint
        #self._debug_print()
        
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
                if self.ind[key]["FAMC"]!="None":
                    famc_list=[]
                    for i in range(0,len(self.ind[key]["FAMC"])):
                        famc_list.append(self.ind[key]["FAMC"][i][0])
                    #print(famc_list)
                    arr.append(famc_list)
                else:
                    arr.append(self.ind[key]["FAMC"])
            else:
                arr.append("NA")
            if values.__contains__("FAMS"):
                if self.ind[key]["FAMS"]!="NA":
                    fams_list=[]
                    for i in range(0,len(self.ind[key]["FAMS"])):
                        fams_list.append(self.ind[key]["FAMS"][i][0])
                    #print(fams_list)
                    arr.append(fams_list)
                else:
                    arr.append(self.ind[key]["FAMS"])
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
                arr.append(self.ind[husID]["NAME"][0])
            else:
                arr.append("NA")
                arr.append("NA")
            
            if values.__contains__("WIFE"):
                arr.append (self.family[key]["WIFE"][0])
                wifeID = self.family[key]["WIFE"][0]
                arr.append(self.ind[wifeID]["NAME"][0])
            else:
                arr.append("NA")
                arr.append("NA")
            
            if values.__contains__("CHIL"):
                chil_list=[]
                for i in range(0,len(self.family[key]["CHIL"])):
                    chil_list.append(self.family[key]["CHIL"][i][0])
                    #print(fams_list)
                arr.append(chil_list)
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
        userstories_sp.us35_ppl_born_last_30days(self.ind)
        #User Story 36
        userstories_sp.us36_ppl_died_last_30days(self.ind)
        #User Story 33
        userstory_an.parse_data_33(self.ind,self.family)
        # User Story 34
        us34_list_big_age_diff(self.ind,self.family)
        #User story 38
        userstory_an.parse_data_38(self.ind)
        # User Story 29
        us29_list_dead(self.ind)
        # User story 30
        us30_list_living_married(self.ind, self.family)
        # User Story 28
        us_rs.listChildrenDecreasingOrderOfAge(self.ind, self.family)
        # User Story 31
        us_rs.listSinglePeopleOver30(self.ind)

    # Call your user story method here if it is related to search and validate
    def validate_all(self):
        # User Story 01
        us01_date_b4_now(self.ind, self.family)
        #User story 03
        userstory_an.parse_data_03(self.ind)
        # User Story 4 and 7
        #print(self.ind)
        userstory_an.parse_data_04(self.family)
        userstory_an.parse_data_07(self.ind)
        #User Story 21
        userstory_an.parse_data_21(self.ind,self.family)
        # User Story 42
        us42_legit_date(self.ind, self.family)
        # User Story 15        
        test_val_15 = us_rs.siblingCount(self.family)              
        # User Story 02
        userstories_sp.us02_birth_before_marriage(self.ind, self.family)
        # User Story 10
        us10_marriage_after_14(self.ind, self.family)
        # User story 06
        us_rs.divorceBeforeDeath(self.ind, self.family)
        # User Story 23
        us_rs.uniqueNameAndBirthdayCheck(self.ind)
        # User story 12
        userstories_sp.us12_parent_child_agediff_limit(self.ind, self.family)
        # User Story 08
        userstories_sp.us08_child_born_after_parents_marriagedate(self.ind, self.family)
        # User Story 26
        us26_match_entries(self.ind, self.family)
        # User story 25
        us_rs.uniqueChildNameCheck(self.ind, self.family)
        # User story 05
        us_rs.marriageBeforeDeath(self.ind, self.family)
        # User Story 09
        userstories_sp.us09_child_birth_parent_death(self.ind, self.family)
        # User Story 18
        us18_sibling_marriage(self.family)


def main():
    gedcom = Gedcom(FILENAME)
    gedcom.print_all()
    gedcom.validate_all()
    

if __name__ == '__main__':
    main()
