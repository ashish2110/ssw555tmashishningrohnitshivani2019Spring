import datetime

def us01_date_b4_now(ind, family):
    for key, values in ind.items():
        if (values.__contains__("BIRT_DATE") and ind[key]["BIRT_DATE"] != "NA"):
            isB4Now = us01_tsk01_is_b4_now(ind[key]["BIRT_DATE"][0])
            if (isB4Now == False):
                print('Error US01 in line', ind[key]["BIRT_DATE"][1],': Birth date of', ind[key]["NAME"][0], '(', key ,') occurs after current date.')
        if (values.__contains__("DEAT_DATE") and ind[key]["DEAT_DATE"] != "NA"):
            isB4Now = us01_tsk01_is_b4_now(ind[key]["DEAT_DATE"][0])
            if (isB4Now == False):
                print('Error US01 in line', ind[key]["DEAT_DATE"][1], ': Death date of', ind[key]["NAME"][0], '(', key ,') occurs after current date.')

    for key, values in family.items():
        if (values.__contains__("MARR_DATE") and family[key]["MARR_DATE"] != "NA"):
            isB4Now = us01_tsk01_is_b4_now(family[key]["MARR_DATE"][0])
            if (isB4Now == False):
                husID = family[key]["HUSB"][0]
                wifeID = family[key]["WIFE"][0]
                print('Error US01 in line', family[key]["MARR_DATE"][1],': Marriage date of ', ind[husID]["NAME"][0],'(', husID, ') and', ind[wifeID]["NAME"][0],'(', wifeID,') in Family (', key,') occurs after current date.')
        if (values.__contains__("DIV_DATE") and family[key]["DIV_DATE"] != "NA"):
            isB4Now = us01_tsk01_is_b4_now(family[key]["DIV_DATE"][0])
            if (isB4Now == False):
                husID = family[key]["HUSB"][0]
                wifeID = family[key]["WIFE"][0]
                print('Error US01 in line', family[key]["DIV_DATE"][1],': Divorce date of ', ind[husID]["NAME"][0],'(', husID, ') and', ind[wifeID]["NAME"][0],'(', wifeID,') in Family (', key,') occurs after current date.')

def us01_tsk01_is_b4_now(dateString):
    isParsable = us01_tsk02_is_parsable(dateString)

    if(isParsable):
        nowDate = datetime.datetime.now()
        subjectDate = datetime.datetime.strptime(dateString, '%Y-%m-%d')
        return (subjectDate < nowDate)
    else:
        #if input date is NA or invalid, it is considered as true
        return True

def us01_tsk02_is_parsable(dateString):
    try:
        dateInput = datetime.datetime.strptime(dateString, '%Y-%m-%d')
        return True
    except ValueError:
        return False