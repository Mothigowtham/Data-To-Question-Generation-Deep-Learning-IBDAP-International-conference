def ques(sql,col,df,sher_pred):
    import random
    #print(sql)
    name = sql[5]
    print("SQL string 5th index ",name)
    x = col[col["Column"] == name]
    #print("Col name ques ",x)
    des = x["Description1"].tolist()[0]
    #print("Col Des ques ",des)
    col1 = list(df.columns)

    if "*" in sql:
        print("Show all the records where", des, "are", sql[6],sql[7],"?")
    else:
        name1 = sql[1]
        print("name1",name1)
        x1 = col[col["Column"] == name1]
        #print("x1",x1)
        des1 = x1["Description1"].tolist()[0]
        #print("des1", des1)
        if 'year' in sher_pred:
            if 'year' in sql[5]:
                a3 = random.randint(0,3)
                if a3 == 0:
                    print('In which year', des1, 'was maximum')
                    print ("SQL", sql)
                elif a3 == 1:
                    print('In which year', des1, 'was minimum')
                    print ("SQL", sql)
                elif a3 == 2:
                    print('In which year', des1, 'was below average')
                    print (sql)
                else:
                    print('In which year', des1, 'was above average')
                    rint ("SQL", sql)
        else:
            if (sql[6] == "Minimum"):
                a1 = random.randint(0,1)
                if a1 == 1:
                    ques = "What is the minimum " + des + " among all " + des1 + " ?"
                    print(ques)
                    rint ("SQL", sql)
                else:
                    ques = "Which "+ des1 + " has the least "+ des + " ?"
                    print(ques)
                    rint ("SQL", sql)      
            elif (sql[6] == "Maximum"):
                a2 = random.randint(0,1)
                if a2 == 1:
                    ques = "What is the maximum "+des+" among all "+des1
                    print(ques)
                    rint ("SQL", sql)
                else:
                    ques = "Which "+des1+" has the highest "+des+" ?"
                    print(ques)
                    rint ("SQL", sql)    
            elif (sql[6] == "Average "):
                r1 = random.randint(0,1)
                if r1 == 0:
                    print("What is the average",des,"among all",des1)
                    ans = df[name].mean()
                    print ("SQL", sql)
                else:
                    guess = random.randint(0,len(df[sql[1]])-1)
                    value = df[sql[1]].iloc[guess]
                    guess1 = random.randint(0,len(df[sql[1]])-1)
                    value1 = df[sql[1]].iloc[guess1]
                    print("What is the average",des,"where",des1,"is",value,"and",value1)
                    print ("SQL", sql)
            elif (sql[6] == "COUNT"):
                import random
                guess = random.randint(0,len(df[sql[1]])-1)
                value = df[sql[1]].iloc[guess]
                print("How many instances in the record has",des1,"equal to",value)
                print ("SQL", sql)
            elif (sql[6] == "sum of"):
                import random
                guess = random.randint(0,len(df[sql[1]])-1)
                value = df[sql[1]].iloc[guess]
                guess1 = random.randint(0,len(df[sql[1]])-1)
                value1 = df[sql[1]].iloc[guess1]
                print("What is the Sum of",des,"in",des1,value,"and",value1)
                print ("SQL", sql)
            else:
                import random
                r = random.randint(0,1)
                if r == 0:
                    print("Which",des1, "has",des ,sql[6],sql[7], "?")
                    print ("SQL", sql)
                    if(sql[6] == "Equal to"):
                        ans = df[df[name] == sql[7]][name1]
                    elif (sql[6] == "Not Equal to"):
                        ans = df[df[name] != sql[7]][name1]
                    elif (sql[6] == "Lesser than"):
                        ans = df[df[name] < sql[7]][name1]
                    else:
                        ans = df[df[name] > sql[7]][name1]
                else:
                    print("What is the", des1 , "where", des  ,sql[6], sql[7], "?")
                    print ("SQL", sql)
                    if(sql[6] == "Equal to"):
                        ans = df[df[name] == sql[7]][name1]
                    elif (sql[6] == "Not Equal to"):
                        ans = df[df[name] != sql[7]][name1]
                    elif (sql[6] == "Lesser than"):
                        ans = df[df[name] < sql[7]][name1]
                    else:
                        ans = df[df[name] > sql[7]][name1]