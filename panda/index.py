# import pandas as pd
# # df=pd.read_csv("nyc_weather.csv")

# # maxtemp=df['Temperature'].max()
# # print(maxtemp)
# # me=df['WindSpeedMPH'].mean()
# # print(me)
# # weather_data={
# #     'day':['1/1/2021','1/2/2021','1/3/2021','1/4/2021','1/5/2021','1/6/2021'],
# #     'temperature':[32,45,34,27,31,30],
# #     'windspean':[6,7,5,9,3,4],
# #     'event':['rain','sunny','snow','rain','sunny','snow']

# # }
# # df=pd.DataFrame(weather_data)
# # print(df.columns)
# # df.set_index('day',inplace=True)
# # print(df)


# weather_data={
#     'day':['1/1/2021','1/2/2021','1/3/2021','1/4/2021','1/5/2021','1/6/2021'],
#     'temperature':[32,45,34,27,31,30],
#     'windspean':[6,7,5,9,3,4],
#     'event':['rain','sunny','snow','rain','sunny','snow']
# }


# a=[111,212,343,444,531]
# end=len(a)-1
# while 0<=end:
#     print("hello world")
#     end-=1

s = "anagram"
t = "zagaram"
for i in range(len(t)):
    if t[i] not in s:
       print(t[i])
    