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

columnsData=list(pd.DataFrame(data2Dict).columns)

df1=pd.DataFrame(data1Dict)
df2=pd.DataFrame(data2Dict)
listData=[]
for i in range(len(columnsData)):
    if columnsData[i]=="Messgae":
        break
    data1=list(df1[columnsData[i]])
    data2=list(df2[columnsData[i]])

    if columnsData[i]=="km":
        print("Km")

   
    for Data in range(len(data1)):
        if data1[Data] != data2[Data] :
        # if data1[Data] not in data2 :
            newMessage=""
            # message1="{} not available in DF-2".format(data1[Data])
            message1="{} not available in DF-2".format(columnsData[i])  # for column name
            if len(listData)==0:
                listData.append(message1)
            else:
                if len(listData)<=Data:
                    listData.append(message1)
                elif listData[Data]!="":
                    newMessage=listData[Data]+","+message1
                    listData[Data]=newMessage
                    newMessage=""
                    
                else:
                    dataWithCommaSep=listData[Data]
                    if dataWithCommaSep!="":
                        NewMessageData=dataWithCommaSep+","+message1
                        listData.insert(Data,NewMessageData)
                        NewMessageData=""

                    elif dataWithCommaSep=="":
                        listData[Data]=message1
                        # listData.insert(Data,message1)

        else:
            if len(listData)<=Data:
                listData.append("")

            elif listData[Data]=="":
                listData[Data]=""




listData2=[]
for i in range(len(columnsData)):
    if columnsData[i]=="Messgae":
        break
    data1=list(df1[columnsData[i]])
    data2=list(df2[columnsData[i]])
   
    for Data in range(len(data2)):
        if data2[Data] != data1[Data] :
        # if data1[Data] not in data2 :
            newMessage=""
            # message1="{} not available in DF-2".format(data1[Data])
            message1="{} not available in DF-1".format(columnsData[i])  # for column name
            if len(listData2)==0:
                listData2.append(message1)
            else:
                if len(listData2)<=Data:
                    listData2.append(message1)
                elif listData2[Data]!="":
                    newMessage=listData2[Data]+","+message1
                    listData2[Data]=newMessage
                    newMessage=""
                    
                else:
                    dataWithCommaSep=listData2[Data]
                    if dataWithCommaSep!="":
                        NewMessageData=dataWithCommaSep+","+message1
                        listData2.insert(Data,NewMessageData)
                        NewMessageData=""

                    elif dataWithCommaSep=="":
                        listData2[Data]=message1
                        # listData.insert(Data,message1)

        else:
            if len(listData2)<=Data:
                listData2.append("")

            elif listData2[Data]=="":
                listData2[Data]=""


data1Dict["Messgae"]=listData
data2Dict["Messgae"]=listData2
newDataFrame1=pd.DataFrame(data1Dict)
newDataFrame2=pd.DataFrame(data2Dict)
print(newDataFrame1)
print(newDataFrame2)


# ['', '200 not available in DF-2', '10 not available in DF-2', '25 not available in DF-2', '100 not available in DF-2', '', 'Kolkata not available in DF-2']