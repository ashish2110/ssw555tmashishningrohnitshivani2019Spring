class us_rs:
    def printError(lineNumber, UserstoryName, message):
        print("ERROR " + UserstoryName + " in line " + str(lineNumber) + ". " + message )

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



                

  


