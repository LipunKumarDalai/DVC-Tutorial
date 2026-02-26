import os
import pandas as pd



dic = pd.DataFrame({
    "Fname":["Lipu","John","eoung"],
    "Lname":["Dalai","Folks","Si"]
})

dir = "data"
os.makedirs(dir,exist_ok=True)


dic.to_csv("mydata.csv")