import requests #url:get 요청
import csv #csv로 저장
import os  #폴더생성
from datetime import datetime # 시간변환
WEATHER_API_KEY=os.getenv("WEATHER_API_KEY")
city="seoul"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
response = requests.get(url)
result = response.json()
#현재기온,습도,날씨상태,현재시각
temp = result["main"]["temp"]
humidity = result["main"]["humidity"]
weather = result["weather"][0]["main"]
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#csv
header =["current_time","weather","temp","humidity"]

#만약,seoul_weather.csv 없으면 만들고 있으면 덮어쓰기
csv_exist =os.path.exists("seoul_weather.csv")

with open("seoul_weather.csv","a") as file:
    writer = csv.writer(file)

    # csv가 한 번도 안 만들어졌다면, 헤더추가
    if not csv_exist:
        writer.writerow(header)

    writer.writerow([current_time, weather, temp, humidity])
    print("서울기온 저장 완료")
