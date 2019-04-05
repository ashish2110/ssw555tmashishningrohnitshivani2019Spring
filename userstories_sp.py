
#Refactored code to make a single class for all the userstories
import datetime
class userstories_sp():

    #refactored for date conversion to reduce duplicate code as it would be used even in future user stories
    def date_conversion(date):
        return datetime.datetime.strptime(date, '%Y-%m-%d')

    #refactored for list display for user stories that print list of certain records
    def print_recordlist(record_list):
        for records in record_list:
            print(records)
            print()
        

    # User Story #02
    """
    Birth should occur before marriage of an individual
    """
    def us02_birth_before_marriage(ind, family):
        for key, values in ind.items():
            if (values.__contains__("BIRT_DATE") and ind[key]["BIRT_DATE"][0] != "NA"):
                if (values.__contains__("FAMS") and ind[key]["FAMS"] != "NA"):
                    for family_id_list in ind[key]["FAMS"]:
                        for family_id in family_id_list : 
                            for key1, values1 in family.items():
                                if (key1 == family_id and values1.__contains__("MARR_DATE") and family[key1]["MARR_DATE"][0] != "NA"):
                                    isvalid = userstories_sp.us02_birth_is_before_marriage(ind[key]["BIRT_DATE"][0],family[key1]["MARR_DATE"][0])
                                    if (isvalid == False):
                                        print('Error US02 in line',ind[key]["BIRT_DATE"][1],': Birth date of', ind[key]["NAME"][0], '(', key ,') occurs after the marriage date.')
                                    #return False
                                    break
                                #else: 
                                    #return False
            else: 
                return False

        

    #changes in code to shorten length
    def us02_birth_is_before_marriage(birth_date,marriage_date):
        if(birth_date == "NA" or marriage_date == "NA"):
            return True
        else:
            birth_date = userstories_sp.date_conversion(birth_date)
            marriage_date = userstories_sp.date_conversion(marriage_date)
            return birth_date < marriage_date
            

    # User Story #35
    """
    List all people in a GEDCOM file who were born in the last 30 days
    """
    def us35_ppl_born_last_30days(ind):
        last_30days_born_list =[]
        for key, values in ind.items():
            if (values.__contains__("BIRT_DATE") and ind[key]["BIRT_DATE"][0] != "NA"):
                status = userstories_sp.us35_ppl_born_last_30days_check(ind[key]["BIRT_DATE"][0])
                if status == True:
                    last_30days_born_list.append(key+str(values))
                    
        print("US35: List of individuals born in the last 30days:  ")
        userstories_sp.print_recordlist(last_30days_born_list)
       
        

 
    #changes in code to shorten length
    def us35_ppl_born_last_30days_check(birth_date):
        if(birth_date == "NA"):
            return False
        else:
            return birth_date >= str(datetime.date.today()-datetime.timedelta(days=30)) and birth_date < str(datetime.date.today())
            


    # User Story #36
    """
    List all people in a GEDCOM file who were born in the last 30 days
    """
    def us36_ppl_died_last_30days(ind):
        last_30days_died_list =[]
        for key, values in ind.items():
            if (values.__contains__("DEAT_DATE") and ind[key]["DEAT_DATE"][0] != "NA"):
                status = userstories_sp.us36_ppl_died_last_30days_check(ind[key]["DEAT_DATE"][0])
                if status == True:
                    last_30days_died_list.append(key+str(values))
        
        print("US36: List of individuals died in the last 30days:  ")
        userstories_sp.print_recordlist(last_30days_died_list)


    def us36_ppl_died_last_30days_check(death_date):
        if(death_date == "NA"):
            return False
        else:
            return death_date >= str(datetime.date.today()-datetime.timedelta(days=30)) and death_date < str(datetime.date.today())


    # User Story #12
    """
    Mother should be less than 60 years older than her children and father should be less than 80 years older than his children
    """
    def us12_parent_child_agediff_limit(ind, family):
        for key, values in family.items():
            if (values.__contains__("CHIL") and family[key]["CHIL"] != "NA"):
                for child in family[key]["CHIL"]:
                    for key1, value1 in ind.items():
                        if (value1.__contains__("BIRT_DATE") and ind[key1]["BIRT_DATE"][0] != "NA"):
                            if key1 == child[0]:
                                child_birth_date = ind[key1]["BIRT_DATE"][0]
                                child_bd_lineno = ind[key1]["BIRT_DATE"][1]
                            
                            if key1 == family[key]["WIFE"][0]:
                                mother_birth_date = ind[key1]["BIRT_DATE"][0] 
                                mother_bd_lineno = ind[key1]["BIRT_DATE"][1]

                            if key1 == family[key]["HUSB"][0]:
                                father_birth_date = ind[key1]["BIRT_DATE"][0] 
                                father_bd_lineno = ind[key1]["BIRT_DATE"][1]
                    status = userstories_sp.us12_parent_child_agediff_limit_check(child_birth_date, mother_birth_date, father_birth_date)
                    if status == False:
                        print("ERROR US12 in line :"+str(child_bd_lineno)+" or "+str(mother_bd_lineno)+" or "+str(father_bd_lineno)+": Mother should be less than 60 years older than her children and father should be less than 80 years older than his children")
           
    def us12_parent_child_agediff_limit_check(child_birth_date, mother_birth_date, father_birth_date):
        if(child_birth_date == "NA" or mother_birth_date =="NA" or father_birth_date =="NA"):
            return False
        else:
            child_birth_date = userstories_sp.date_conversion(child_birth_date)
            mother_birth_date = userstories_sp.date_conversion(mother_birth_date)
            father_birth_date = userstories_sp.date_conversion(father_birth_date)
            if (abs((child_birth_date - mother_birth_date).days)/365.25) < 60 and  (abs((child_birth_date - father_birth_date).days)/365.25) < 80:
                return True 
            else:
                return False


    # User Story #08
    """
    Children should be born after marriage of parents (and not more than 9 months after their divorce)
    """
    def us08_child_born_after_parents_marriagedate(ind, family):
        for key, values in family.items():
            if (values.__contains__("MARR_DATE") and family[key]["MARR_DATE"] != "NA" and family[key]["CHIL"] != "NA" and values.__contains__("DIV_DATE")):
                for child in family[key]["CHIL"]:
                    for key1, values1 in ind.items():
                        if (key1 == child[0]):
                            if(values1.__contains__("BIRT_DATE") and ind[key1]["BIRT_DATE"][0] != "NA"):
                                status = userstory_sp.us08_child_parents_marriagedate_check(family[key]["MARR_DATE"][0],ind[key1]["BIRT_DATE"][0],family[key]["DIV_DATE"])
                                if (status == False):
                                    print("ERROR US08 in line"+str(ind[key1]["BIRT_DATE"][1])+": Children should be born after marriage of parents (and not more than 9 months after their divorce")

        def us08_child_parents_marriagedate_check(marriage_date,child_birth_date,divorce_date):
            child_birth_date = userstory_sp.date_conversion(child_birth_date)
            marriage_date = userstory_sp.date_conversion(marriage_date)
            if (divorce_date == "NA"):
                return child_birth_date > marriage_date
            else:
                divorce_date = userstory_sp.date_conversion(divorce_date[0])
                diff = relativedelta.relativedelta(child_birth_date, divorce_date)
                return child_birth_date > marriage_date and diff.months < 9 
