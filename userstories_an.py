class userstory_an():

    def us_04(mar,div,i):   
        if div!='NA' and mar!='NA' and mar[0]!='Invalid' and div[0]!='Invalid':
            if mar[0]>div[0]:
                return "Error US04 in line " + str(div[1]) +" or line "+ str(mar[1])+":Marriage date occurs after Divorce date in "+ i +" family"
            else:
                return 0
        else:
            return 0

    def us_07(birth,death,Age,i):
        if Age!='NA' and Age!='Invalid':
            if Age>=150:
                if death!='NA':
                    return "Error US07 in line "+ str(birth[1]) +" or line "+ str(death[1])+":Age of person is 150 years with "+ i +" id"
                else:
                    return "Error US07 in line "+ str(birth[1]) +":Age of person is 150 years with "+ i +" id"
            else:
                return 0
        else:
            return 0
    
    def us_21(a,b,i,j,k):
        temp=[]#here temp is used for storing errors
        if a[0]=='M'or a[0]=='NA':
            temp.append(0)
        else:
            temp.append("Error US21 in line "+ str(a[1]) +":Gender of husband with "+str(j)+ " id is not male in "+ str(i)+" family")
        if b[0]=='F' or b[0]=='NA':
            temp.append(0)
        else:
            temp.append("Error US21 in line "+ str(b[1]) +":Gender of wife with "+str(k)+ " id is not female in "+ str(i)+" family")
        return temp

    def us_33(hus,wif,chil_age,chil):
        if hus!='NA'and wif!='NA':
            if hus[0]!='Invalid' and wif[0]!='Invalid':
                if chil_age!='NA' and chil_age!='Invalid' and chil_age<18:
                    return chil
                else:
                    return 0
            else:
                return 0
        else:
            return 0

    def parse_data_04(family):
        for x in family:#here x is family_id
            answer=userstory_an.us_04(family[x]['MARR_DATE'],family[x]['DIV_DATE'],x)
            if answer!=0:
                print(answer)
        return 0

    def parse_data_07(ind):
        for x in ind:#here x is individual persons id
            answer=userstory_an.us_07(ind[x]['BIRT_DATE'],ind[x]['DEAT_DATE'],ind[x]['AGE'],x)
            if answer!=0:
                print(answer)
        return 0

    def parse_data_21(ind,family):
        for x in family:#here x is family_id
            if ('HUSB' in family[x]) and (family[x]['HUSB'][0] in ind) and ('SEX' in ind[family[x]['HUSB'][0]]):
                a=ind[family[x]['HUSB'][0]]['SEX']
                c=family[x]['HUSB'][0]
                
            else:
                a=['NA',-1]#a is husband's sex
                c='NA'#c is hysband's id
            
            if ('WIFE' in family[x]) and (family[x]['WIFE'][0] in ind) and ('SEX' in ind[family[x]['WIFE'][0]]):
                b=ind[family[x]['WIFE'][0]]['SEX']
                d=family[x]['WIFE'][0]
                
            else:
                b=['NA',-1]#b is wife's sex
                d='NA'#d is wife's id
            answer=userstory_an.us_21(a,b,x,c,d)
            for i in answer:
                if i!=0:
                    print(i)
        return 0

    def parse_data_33(ind,family):
        orphan_chil=[]
        for x in family:#here x is family_id
            if ('HUSB' in family[x]) and ('WIFE' in family[x]) and ('CHIL' in family[x]) and (family[x]['HUSB'][0] in ind) and (family[x]['WIFE'][0] in ind):
                for y in family[x]['CHIL']:#here y is children id in each family
                    if (y[0] in ind):
                        answer=userstory_an.us_33(ind[family[x]['HUSB'][0]]['DEAT_DATE'],ind[family[x]['WIFE'][0]]['DEAT_DATE'],ind[y[0]]['AGE'],y[0])
                        if answer!=0:
                            orphan_chil.append(answer)
        print("List of id's of orpan children is: "+ str(orphan_chil))