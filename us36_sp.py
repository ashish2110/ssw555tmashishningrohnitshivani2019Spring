import datetime
from us_ny import us01_tsk02_is_parsable
def us36_ppl_died_last_30days(ind, family):
    last_30days_died_list =[]
    for key, values in ind.items():
        if (values.__contains__("DEAT_DATE") and ind[key]["DEAT_DATE"] != "NA"):
           present_date = datetime.datetime.now()
           status = us36_ppl_died_last_30days_check(ind[key]["DEAT_DATE"][0],present_date)
           if status == True:
               new_record = key+str(values)
            #   print(new_record)
            #    print(type(values))
               last_30days_died_list.append(new_record)
    for records in last_30days_died_list:
        print("List of individuals died in the last 30days:  ")
        print(records)


def us36_ppl_died_last_30days_check(death_date,present_date):
    #print(type(death_date))
    if not us01_tsk02_is_parsable(death_date):
        return False

    if(death_date == "NA" or present_date =="NA"):
        return False
    else:
        death_date = datetime.datetime.strptime(death_date, '%Y-%m-%d')

        if present_date + datetime.timedelta(-30) < death_date and  death_date < present_date:
            return True 
        else:
            return False

        