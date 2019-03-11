import datetime

# User Story #02
"""
Birth should occur before marriage of an individual
"""
def us02_birth_before_marriage(ind, family):
    for key, values in ind.items():
        if (values.__contains__("BIRT_DATE") and ind[key]["BIRT_DATE"] != "NA"):
            if (values.__contains__("FAMS") and ind[key]["FAMS"] != "NA"):
                # print("Family spouse   ",ind[key]["FAMS"])
                # print(type(ind[key]["FAMS"]))
                fam_list = ind[key]["FAMS"]
                # print("fam_list",fam_list)
                for family_id_list in fam_list:

                    for family_id in family_id_list :
                        
                        for key1, values1 in family.items():
                            if (key1 == family_id and values1.__contains__("MARR_DATE") and family[key1]["MARR_DATE"] != "NA"):
                                # print("In User Story 02=====")
                                isvalid = us02_birth_is_before_marriage(ind[key]["BIRT_DATE"][0],family[key1]["MARR_DATE"][0])
                                if (isvalid == False):
                                    print('Error US02 in line',ind[key]["BIRT_DATE"][1],': Birth date of', ind[key]["NAME"][0], '(', key ,') occurs after the marriage date.')
                                    return isvalid
                                break

    
def us02_birth_is_before_marriage(birth_date,marriage_date):
    if(birth_date == "NA" or marriage_date == "NA"):
        return True
    else:
        birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d')
        marriage_date = datetime.datetime.strptime(marriage_date, '%Y-%m-%d')

        if(birth_date < marriage_date):
            return True
        else:
            return False