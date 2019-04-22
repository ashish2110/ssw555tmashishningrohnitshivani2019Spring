class us_rs:
    def printError(lineNumber, UserstoryName, message):
        print("ERROR " + UserstoryName + " in line " + str(lineNumber) + ". " + message )
    
    def firstName(name):
        nameArr = name.split(" ")
        return nameArr[0]

    def ageOfInd(indId, ind_object):
        
        return ind_object[indId]["AGE"]

    # UserStory 15
    def siblingCount(family):
        validity = True
        if(type(family) is not (dict)):
            print("Argument isn't an dict")
            validity = False
        
        for x, values in family.items():
            
            if values.__contains__("CHIL"):
                length = len(values["CHIL"])    
            else:
                length = 0
            if length > 15:
                validity = False
                us_rs.printError(values['CHIL'][0][1], "US 15", "There are more than 15 siblings for family.")
                         
        return validity

    #Userstory 6 - Divorce can only occur before death of both spouses
    def divorceBeforeDeath(individual, family):
        flag = True
        error = []
        for famid, famvalue in family.items():
            divorceDate = famvalue['DIV_DATE']
            if divorceDate == "NA":
                flag = True
                continue 
            husbandDeath = individual[famvalue['HUSB'][0]]['DEAT_DATE']
            wifeDeath = individual[famvalue['WIFE'][0]]['DEAT_DATE']  
            if(husbandDeath[0] < divorceDate[0]):
                error.append(str(husbandDeath[1]))
                flag = False
            if(wifeDeath[0] < divorceDate[0]):
                error.append(str(wifeDeath[1]))
                flag = False
        if(len(error)>0):
            for err in error:
                us_rs.printError(err, "US 06", "Check the provided death date at the line. It occurs before the divorce.")
        return flag

    # user story 23: Unique Name and birthday
    def uniqueNameAndBirthdayCheck(individual):
        flag = True
        datadict = []
        for indid, indvalue in individual.items():
            element = []
            element.append(indvalue['NAME'])
            element.append(indvalue['BIRT_DATE'])
            datadict.append(element)

        i = 0
        while i < len(datadict):
            j = i + 1
            while j < len(datadict):
                if datadict[i][0][0] == datadict[j][0][0]:
                    if datadict[i][1][0] == datadict[j][1][0]:

                        us_rs.printError(datadict[i][0][1], 'US 23', "The name and birthdate is not unique.")
                        flag = False
                j += 1
            i += 1

        return flag
    # Userstory 5 - Marriage can occur before death         
    def marriageBeforeDeath(individual, family):
        flag = True
        error = []
        for famid, famvalue in family.items():
            marriageDate = famvalue['MARR_DATE']
            if marriageDate == "NA":
                flag = True
                continue 
            husbandDeath = individual[famvalue['HUSB'][0]]['DEAT_DATE']
            wifeDeath = individual[famvalue['WIFE'][0]]['DEAT_DATE']  
            if(husbandDeath[0] < marriageDate[0]):
                error.append(str(husbandDeath[1]))
                flag = False
            if(wifeDeath[0] < marriageDate[0]):
                error.append(str(wifeDeath[1]))
                flag = False
        if(len(error)>0):
            for err in error:
                us_rs.printError(err, "US 05", "Check the provided death date at the line. It occurs before the marriage.")
        return flag
  
    # User Story 25 - No more than one child with the same name and birth date should appear in a family
    def uniqueChildNameCheck(individual, family):
        childrenNames = []
        flag = True
        childrenIds = []
        for famid, famvalue in family.items():
            if famvalue.__contains__("CHIL"):
                childrenIds = famvalue["CHIL"]
            '''
            for childId in childrenIds:
                if(childId in individual.keys()):
                    childName = individual[childId[0]]["NAME"]
                    childrenNames.append(childName)
            '''
            for index in range(0, len(family[famid]["CHIL"])):
                childId = family[famid]["CHIL"][index][0]
                if(childId in individual.keys()):
                    childName = individual[childId]["NAME"]
                    childrenNames.append(childName)
            i = 0
            
            if(len(childrenNames) > 1):
                while(i < len(childrenNames)):
                    j = i + 1
                    while(j < len(childrenNames)):
                        # print(childrenNames[i][0])
                        # cprint(childrenNames[j][0])
                        name_1 = us_rs.firstName(childrenNames[i][0])
                        name_2 = us_rs.firstName(childrenNames[j][0])
                        # print(name_1 + " and " + name_2 )
                        if (name_1 == name_2):
                            us_rs.printError(childrenNames[i][1], "US 25", "The Family has multiple children with the same first name.")
                            flag = False
                            return flag
                    
                        j += 1
                    i += 1
            childrenNames.clear()

        return flag


    # User Story 28 - List siblings in families by decreasing age, i.e. oldest siblings first

    def listChildrenDecreasingOrderOfAge(individual, family):
        print("Listing siblings (if listed in the individual table) in a family in a decreasing order of their ages.")
        
        for famid, famvalue in family.items():
            indAndAgeArray = []
            if famvalue.__contains__("CHIL"):
                
                print("Family " + famid + ":")
                for child in famvalue["CHIL"]:
                    childAndAge =[]
                    childAndAge.append(child[0])
                    if child[0] in individual:
                        childAndAge.append(us_rs.ageOfInd(child[0], individual))
                        indAndAgeArray.append(childAndAge)
                        
                        childAndAge = []

                for item in indAndAgeArray:
                    if not isinstance(item[1], int):
                        item[1] = 0
                
                indAndAgeArray = sorted(indAndAgeArray, key=lambda x: x[1], reverse=True)       
                print([i[0] for i in indAndAgeArray])
        
        return [i[0] for i in indAndAgeArray] ;

    # User Story 31 - List all living people over 30 who have never been married in a GEDCOM file
    def listSinglePeopleOver30(individual):
        listOfInd = []
        flag = False
        for indId, indValue in individual.items():
            # print(str(indValue['FAMS'])+ " " +str(indValue['AGE']) + " " + indValue['ALIVE'])
            if((indValue['FAMS'] == 'NA') and  (indValue['ALIVE'] == 'True') and indValue["AGE"] > 30):
                listOfInd.append(indId)
                flag = True
        print("US 31: List of all living people over 30 who have never been married: ")
        print(listOfInd)
        return flag
        
                

  


