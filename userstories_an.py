class userstory_an():

    def us_04(mar_div_details):
        if mar_div_details[1]!= 'NA' and mar_div_details[0]!= 'NA' and mar_div_details[0][0]!= 'Invalid' and mar_div_details[1][0]!= 'Invalid':
            if mar_div_details[0][0]>mar_div_details[1][0]:
                return "Error US04 in line " + str(mar_div_details[1][1]) + " or line " + str(mar_div_details[0][1]) + ":Marriage date occurs after Divorce date in " + mar_div_details[2] + " family"
            else:
                return 0
        else:
            return 0

    def us_07(date):
        if date[2]!= 'NA' and date[2]!= 'Invalid':
            if date[2]>=150:
                if date[1]!= 'NA':
                    return "Error US07 in line " + str(date[0][1]) + " or line " + str(date[1][1]) + ":Age of person is 150 years with " + date[3] + " id"
                else:
                    return "Error US07 in line " + str(date[0][1]) + ":Age of person is 150 years with " + date[3] + " id"
            else:
                return 0
        else:
            return 0
    
    def us_21(gender_details):
        orphan_children=[]
        if gender_details[0][0]== 'M'or gender_details[0][0]== 'NA':
            orphan_children.append(0)
        else:
            orphan_children.append("Error US21 in line " + str(gender_details[0][1]) + ":Gender of husband with " + str(gender_details[3]) + " id is not male in " + str(gender_details[2]) + " family")
        if gender_details[1][0]== 'F' or gender_details[1][0]== 'NA':
            orphan_children.append(0)
        else:
            orphan_children.append("Error US21 in line " + str(gender_details[1][1]) + ":Gender of wife with " + str(gender_details[4]) + " id is not female in " + str(gender_details[2]) + " family")
        return orphan_children

    def us_33(orphan_details):
        if orphan_details[0]!= 'NA'and orphan_details[1]!= 'NA':
            if orphan_details[0][0]!= 'Invalid' and orphan_details[1][0]!= 'Invalid':
                if orphan_details[2]!= 'NA' and orphan_details[2]!= 'Invalid' and orphan_details[2]<18:
                    return orphan_details[3]
                else:
                    return 0
            else:
                return 0
        else:
            return 0

    def parse_data_04(family):
        for family_id in family:
            input_list=[family[family_id]['MARR_DATE'],family[family_id]['DIV_DATE'],family_id]
            output=userstory_an.us_04(input_list)
            if output!=0:
                print(output)
        return 0

    def parse_data_07(ind):
        for individual_id in ind:
            list_input=[ind[individual_id]['BIRT_DATE'],ind[individual_id]['DEAT_DATE'],ind[individual_id]['AGE'],individual_id]
            output=userstory_an.us_07(list_input)#refactored by shortening the list of parameters by passing a list.
            if output!=0:
                print(output)
        return 0

    def parse_data_21(ind,family):
        for family_id in family:
            if ('HUSB' in family[family_id]) and (family[family_id]['HUSB'][0] in ind) and ('SEX' in ind[family[family_id]['HUSB'][0]]):
                husband_sex=ind[family[family_id]['HUSB'][0]]['SEX']#refactored by renaming variables
                husband_ind_id=family[family_id]['HUSB'][0]#refactored by renaming variable
                
            else:
                husband_sex=['NA',-1]
                husband_ind_id='NA'
            
            if ('WIFE' in family[family_id]) and (family[family_id]['WIFE'][0] in ind) and ('SEX' in ind[family[family_id]['WIFE'][0]]):
                wife_sex=ind[family[family_id]['WIFE'][0]]['SEX']
                wife_ind_id=family[family_id]['WIFE'][0]
                
            else:
                wife_sex=['NA',-1]
                wife_ind_id='NA'
            input_list=[husband_sex,wife_sex,family_id,husband_ind_id,wife_ind_id]
            output=userstory_an.us_21(input_list)
            for i in output:
                if i!=0:
                    print(i)
        return 0

    def parse_data_33(ind,family):
        orphan_children=[]
        for family_id in family:
            if ('HUSB' in family[family_id]) and ('WIFE' in family[family_id]) and ('CHIL' in family[family_id]) and (family[family_id]['HUSB'][0] in ind) and (family[family_id]['WIFE'][0] in ind):
                for child_id in family[family_id]['CHIL']:
                    if (child_id[0] in ind):
                        input_list=[ind[family[family_id]['HUSB'][0]]['DEAT_DATE'],ind[family[family_id]['WIFE'][0]]['DEAT_DATE'],ind[child_id[0]]['AGE'],child_id[0]]
                        output=userstory_an.us_33(input_list)
                        if output!=0:
                            orphan_children.append(output)
        print("US33: List of id's of orpan children is: "+ str(orphan_children))