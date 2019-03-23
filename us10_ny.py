import datetime
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