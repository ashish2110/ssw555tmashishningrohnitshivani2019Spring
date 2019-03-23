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

    # Userstory 6 - Divorce can only occur before death of both spouses
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

  


