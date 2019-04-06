import datetime
# Sprint 1 user stories
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
        datetime.datetime.strptime(dateString, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def us42_tsk01_is_legit_date(dateString):
    try:
        dateSubject = datetime.datetime.strptime(dateString,'%d %b %Y')
        return True
    except ValueError:
        return False

def us42_legit_date(ind, family):
    for key, values in ind.items():
        if (values.__contains__("BIRT_DATE") and ind[key]["BIRT_DATE"][0] == "Invalid"):
            print('Error US42 in line',ind[key]["BIRT_DATE"][1],': Birth date of', ind[key]["NAME"], '(', key ,') is illegitimate.')
        if (values.__contains__("DEAT_DATE") and ind[key]["DEAT_DATE"][0] == "Invalid"):
            print('Error US42 in line',ind[key]["DEAT_DATE"][1],': Death date of', ind[key]["NAME"], '(', key ,') is illegitimate.')

    for key, values in family.items():
        if (values.__contains__("MARR_DATE") and family[key]["MARR_DATE"][0] == "Invalid"):
            husID = family[key]["HUSB"][0]
            wifeID = family[key]["WIFE"][0]
            print('Error US42 in line',family[key]["MARR_DATE"][1],': Marriage date of ', ind[husID]["NAME"][0],'(', husID, ') and', ind[wifeID]["NAME"][0],'(', wifeID,') in Family (', key,') is illegitimate.')
        if (values.__contains__("DIV_DATE") and family[key]["DIV_DATE"][0] == "Invalid"):
            husID = family[key]["HUSB"][0]
            wifeID = family[key]["WIFE"][0]
            print('Error US42 in line', family[key]["DIV_DATE"][1],': Divorce date of ', ind[husID]["NAME"][0],'(', husID, ') and', ind[wifeID]["NAME"][0],'(', wifeID,') in Family (', key,') is illegitimate.')


#Spring 2 user stories
# Parents must be at least 14 years old when married
def us10_marriage_after_14(ind, family):
    for key, values in family.items():
        if (values.__contains__("MARR_DATE") and family[key]["MARR_DATE"] != "NA"):
            husID = family[key]["HUSB"][0]
            wifeID = family[key]["WIFE"][0]
            # argument sequence: date of marriage, husband date of birth, wife date of birth
            isChildMarriage = us10_tsk01_is_child_marriage(family[key]["MARR_DATE"][0], ind[husID]["BIRT_DATE"][0], ind[wifeID]["BIRT_DATE"][0])
            if(isChildMarriage):
                print('Anomaly US10 in line', family[key]["MARR_DATE"][1],': Marriage of ', ind[husID]["NAME"][0],'(', husID, ') and', ind[wifeID]["NAME"][0],'(', wifeID,') in Family (', key,') occurs before both parents are 14 years old.')
# dom: date of marriage, DOB: date of birth
def us10_tsk01_is_child_marriage(domString, husDOBString, wifeDOBString):
    try:
        dom = datetime.datetime.strptime(domString, '%Y-%m-%d')
        husDOB = datetime.datetime.strptime(husDOBString, '%Y-%m-%d')
        wifeDOB = datetime.datetime.strptime(wifeDOBString, '%Y-%m-%d')
        # if DOM is before DOB, it may be related to US 02 and it is considered False
        if(dom < husDOB or dom < wifeDOB):
            return False
        else:
            return (dates_within(dom, husDOB, 14, 'years') or dates_within(dom, wifeDOB, 14, 'years'))
    except ValueError:
        #if any input date is NA or invalid, it is considered as false
        return False

# dt1, dt2 are instances of datetime
# limit is a number
# units is a string in ('days', 'months', 'years')
# return True if dt1 and dt2 are within limit units
def dates_within(dt1, dt2, limit, units):
    conversion = {'days': 1, 'months': 30.4, 'years': 365.25}
    return (abs((dt1 - dt2).days) / conversion[units]) <= limit

def us34_list_big_age_diff(ind, family):
    print('\nUS34: List of couples whose marriage occurs when older spouse is more than twice as old as younger one.')
    for key, values in family.items():
        if (values.__contains__("MARR_DATE") and family[key]["MARR_DATE"] != "NA"):
            husID = family[key]["HUSB"][0]
            wifeID = family[key]["WIFE"][0]
            # argument sequence: date of marriage, husband date of birth, wife date of birth
            isBigGap = us34_tsk01_is_big_age_gap(family[key]["MARR_DATE"][0], ind[husID]["BIRT_DATE"][0], ind[wifeID]["BIRT_DATE"][0])
            if(isBigGap):
                print('Family', key, 'of husband', ind[husID]["NAME"][0],'(', husID, ') and wife', ind[wifeID]["NAME"][0],'(', wifeID,')')

def us34_tsk01_is_big_age_gap(domString, husDOBString, wifeDOBString):
    try:
        dom = datetime.datetime.strptime(domString, '%Y-%m-%d')
        husDOB = datetime.datetime.strptime(husDOBString, '%Y-%m-%d')
        wifeDOB = datetime.datetime.strptime(wifeDOBString, '%Y-%m-%d')
        # age to be refined
        husAgeByDOM = int((dom-husDOB).days/365)
        wifeAgeByDOM = int((dom-wifeDOB).days/365)
        # if age is negative, it may be related to US 02 and it is considered False
        if(husAgeByDOM < 0 or wifeAgeByDOM < 0):
            return False
        elif(husAgeByDOM > (wifeAgeByDOM * 2) or wifeAgeByDOM > (husAgeByDOM * 2)):
            return True
        else:
            return False
    except ValueError:
        #if any input date is NA or invalid, it is considered as false
        return False


# Sprint 3 user stories
# List all deceased individuals
def us29_list_dead(ind):
    print('\nUS29: List all deceased individuals:')
    for key, values in ind.items():
        if(values.__contains__("ALIVE")):
            if(ind[key]["ALIVE"] == "False"):
                print('US29: Individual', ind[key]["NAME"][0], '(', key ,') died at', ind[key]["DEAT_DATE"][0])