import os
from yandex_geocoder import Client
from dotenv import load_dotenv, find_dotenv
import openpyxl
import csv
load_dotenv(find_dotenv())
client = Client(os.getenv("API_KEY"))
print(client.address(30.359966, 59.930182))


""" wb = openpyxl.load_workbook('./house_list.xlsx')
wb.active = 0
sheet = wb.active

houses=[]
for i in range(1, sheet.max_row):
    house_address = sheet['A' + str(i)].value + sheet['B' + str(i)].value
    coord = client.coordinates(house_address)
    full_address = client.address(coord[0], coord[1]).split(', ')
    full_address.append(coord[1])
    full_address.append(coord[0])
    houses.append(full_address)
    print(coord[1],', ',coord[0])
    '''
    sheet1['A' + str(i)] = full_address
    sheet1['B' + str(i)] = full_address[-2] # Название улицы
    sheet1['C' + str(i)] = full_address[-3] # Номер дома
    sheet1['D' + str(i)] = coord[1] # Координата X  
    sheet1['E' + str(i)] = coord[0] # Координата Y 
    '''

with open('houses.csv', "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(houses) """