import datetime
def us12_parent_child_agediff_limit(ind, family):
    """
    Mother should be less than 60 years older than her children and father should be less than 80 years older than his children
    """
    for key, values in family.items():
        if (values.__contains__("CHIL") and family[key]["CHIL"] != "NA"):
            # print(family[key]["CHIL"])
            for child in family[key]["CHIL"]:
                for key1, value1 in ind.items():
                    # print(child)
                    # print("======")
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
                # print ( "Child :"+child_birth_date+"mother"+mother_birth_date+"Father"+father_birth_date)
                status = us12_parent_child_agediff_limit_check(child_birth_date, mother_birth_date, father_birth_date)
                if status == False:
                    print("ERROR US12 in line :"+str(child_bd_lineno)+" or "+str(mother_bd_lineno)+" or "+str(father_bd_lineno)+": Mother should be less than 60 years older than her children and father should be less than 80 years older than his children")
           


def us12_parent_child_agediff_limit_check(child_birth_date, mother_birth_date, father_birth_date):
    if(child_birth_date == "NA" or mother_birth_date =="NA" or father_birth_date =="NA"):
        return False
    else:
        child_birth_date = datetime.datetime.strptime(child_birth_date, '%Y-%m-%d')
        mother_birth_date = datetime.datetime.strptime(mother_birth_date, '%Y-%m-%d')
        father_birth_date = datetime.datetime.strptime(father_birth_date, '%Y-%m-%d')
        # print(mother_birth_date)
        # print(child_birth_date)
        # print((mother_birth_date - child_birth_date).days)
        if (abs((child_birth_date - mother_birth_date).days)/365.25) < 60 and  (abs((child_birth_date - father_birth_date).days)/365.25) < 80:
            return True 
        else:
            return False
