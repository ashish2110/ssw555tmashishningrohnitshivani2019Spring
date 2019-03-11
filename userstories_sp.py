
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
                                    break

        
    #Refactored to remove uncessary logic as it was already handled 
    #changes in code to shorten length
    def us02_birth_is_before_marriage(birth_date,marriage_date):
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
       
        

    #Refactored to remove uncessary logic as it was already handled
    #changes in code to shorten length
    def us35_ppl_born_last_30days_check(birth_date):
        return birth_date >= str(datetime.date.today()-datetime.timedelta(days=30)) and birth_date < str(datetime.date.today())
            