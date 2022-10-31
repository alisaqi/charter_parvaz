from bs4 import BeautifulSoup
import requests
from datetime import datetime

def flights_handler(departureCity, destinationCity, dateOrder):
    url = 'http://ticket-charter.com/Ticket' + '-' + departureCity + '-' + destinationCity +'.html'+'?'+'t='+dateOrder
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
    }
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.text, 'html.parser')
    records = soup.find_all("div", class_="resu")
    resultsDictionary = {}

    j = 0
    for i in records:
        ticketPrice = i.find("div", class_="price").span.text.replace(" ", "").replace("\n", "").replace("\r", "")
        ticketPriceDigit = i.find("div", class_="price").span.text.replace(" ", "").replace("\n", "").replace("\r", "").replace(",", "")
        if i.find("div", class_="price").find("div", class_="icon11"):
            ticketType = i.find("div", class_="price").find("div", class_="icon11").text.replace(" ", "").replace("\n", "").replace("\r", "").replace("\t\t\t\t\t\t\t\t\t\t\t", "")
        elif i.find("div", class_="price").find("div", class_="icon10"):
            ticketType = i.find("div", class_="price").find("div", class_="icon10").text.replace(" ", "").replace("\n", "").replace("\r", "").replace("\t\t\t\t\t\t\t\t\t\t\t", "")
        flightHour = i.find(class_="date").text.replace(" ", "").replace("\n", "").replace("\r", "")
        flightFreeSeats = i.find(class_="user").text.replace(" ", "").replace("\n", "").replace("\r", "")
        flightCompany = i.find("div", class_="info_parvaz efitooltip_bg").find(class_="efitooltip").find(class_="mkfcol1").find(class_="airline_name").text.replace("\n", "").replace("\r", "")
        flightNumber = i.find("div", class_="code").find("span", class_="code_inn").text.replace(" ", "").replace("\n", "")

        if ticketPrice != "CLOSE":
            if ticketPrice != "CANCEL":
                if flightFreeSeats != '0':
                    resultsDictionary[j] = {
                        "price": ticketPrice,
                        "priceDigit": int(ticketPriceDigit),
                        "ticketType": ticketType,
                        "freeSeats": flightFreeSeats,
                        "departure": flightHour,
                        "company": flightCompany,
                        "flightNumber": flightNumber,
                    }
            # print(resultsDictionary)

        elif ticketPrice == "CLOSE" or ticketPrice == "CANCEL" or flightFreeSeats == '0':
            pass
        j += 1

    if len(resultsDictionary) == 0:
        return False
    else:
        return resultsDictionary

    # print(resultsDictionary)
    # print(f'Time taken {datetime.now() - start_time}')
#
# flightsHandler('Tehran', 'Mashhad', '1401-08-05')