import pandas as pd

data1Dict={
    "City":["Delhi","Bengaluru","Chennai","Mumbai","Kolkata"],
    "km":[500,200,100,200,500],
    "Charges":[50,25,10,25,50],
    "Messgae":""
}
data2Dict={
    "City":["Delhi","Bengaluru","Chennai","Mumbai","Sikkim"],
    "km":[500,100,75,200,500],
    "Charges":[50,25,90,100,50],
    "Messgae":""
}
#metaching City

df1=pd.DataFrame(data1Dict)
df2=pd.DataFrame(data2Dict)

listData1=[""]
for i in df1:
    data1=list(df1[i])
    data2=list(df2[i])
    message1=""
    for DataList in data1:
       
        if DataList not in data2:
            message1="{} not available in DF-2".format(i)
            listData1.append(message1)
            # data1Dict["Messgae"]=message
            # print(data1Dict)
        # else:
        #     listData1.append("")
    
    data1Dict["Messgae"]=listData1
    if message1=="":
        listData1.append("")
    else:
        data1Dict["Messgae"]=listData1
listData2=[]
for i in df2:
    data1=list(df1[i])
    data2=list(df2[i])
    message=""

    tempList=[]
    
    for DataList in data2:
        
        if DataList not in data1:
            message="{} not available in DF-1".format(i)
            # data2Dict["Messgae"]=message
            listData2.append(message)
            
            # print(pd.DataFrame(data2Dict))
        
        # else:
        #     listData2.append("")
    
    # data2Dict["Messgae"]=listData2

    if message=="":
        listData2.append("")
    else:
        data2Dict["Messgae"]=listData2


newDataFrame1=pd.DataFrame(data1Dict)
newDataFrame2=pd.DataFrame(data2Dict)
print(newDataFrame1)
print(newDataFrame2)
