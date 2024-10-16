import requests

useragent = {'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

print("Начал")
for i in range(1,265):
    link = f"https://130122.edgevideo.ru/videos/130122_Xu4wmqsDrFv4loop/segment-{i}-sFullHD-v1-a1.ts"
    response = requests.get(link, headers=useragent)
    with open(f'segment-{i}.ts', "wb") as file:
        file.write(response.content)
    print(i)
print("Закончил")
        
