import pandas as pd

data={
    "City":["Delhi","Bengaluru","Chennai","Mumbai","Kolkata"],
    "Maxtemp":[40,31,35,29,39],
    "MinTemp":[32,25,27,21,23],
    "RainFall":[24.1,36.2,40.8,35.2,41.8]
}
df=pd.DataFrame(data)
sumOfData=df.sum(axis=0)
print("sumData",sumOfData)

print("##################  Mean Data  #################")
meanData=df["RainFall"].mean()
print("meanData",meanData)

print("##################  Median of Maxtemp  #################")

medianData=df["Maxtemp"].median()

print("medianData",medianData)