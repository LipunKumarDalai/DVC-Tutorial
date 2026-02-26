import os
import pandas as pd



dic = pd.DataFrame({
    "Fname":["Lipu","John","eoung"],
    "Lname":["Dalai","Folks","Si"]
})

dic.loc[len(dic)] = ["Alice","Young"]
dic.loc[len(dic)] = ["Viola","Young"]

dir = "data"
os.makedirs(dir,exist_ok=True)


dic.to_csv("data/mydata.csv")