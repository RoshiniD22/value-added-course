import pandas as pd
from twilio.rest import Client
import time
acc_sid="********************************"
auth_token="****************************"
client=Client(acc_sid,auth_token)
df=pd.read_excel("data.xlsx")
for i in range(len(df)):
    name = df.loc[i, "NAME"]
    desig = df.loc[i, "DESIGNATION"]
    number = str(df.loc[i, "NUMBER"])
    number="+91"+number
    messages = {
    'staff': "Good morning",
    'student': "Study well",
    'corpenter': "Have a great day",
    'docter': "Take care",
    'engineer': "Keep building",
    'manager': "Have a productive day"
    }
    msg=messages.get(desig.lower(),"hello")
    final_msg = f"{name}, {msg}"

    client.messages.create(
    from_="whatsapp:+1",
    body=final_msg,
    to=f'whatsapp:{number}'
)
    
    print(f"sent to{name})->{number}")
    time.sleep(1)



