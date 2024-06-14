import pandas as pd

Data = [
    {"name":"minali","age":25,"city":"udaipur"},
    {"name":"sunny","age":27,"city":"jaipur"},
    {"name":"krish","age":29,"city":"lucknow"},
    {"name":"elon mask","age":31,"city":"london"}


]

Data = pd.DataFrame(Data)

Data.to_csv("data/data.csv",index=False)