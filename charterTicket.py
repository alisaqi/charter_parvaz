from bs4 import BeautifulSoup
import requests
from datetime import datetime

def flights_handler(departure_city, destination_city, flight_date):
    url = 'http://ticket-charter.com/Ticket' + '-' + departure_city + '-' + destination_city + '.html' + '?' + 't=' + flight_date
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
    }
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.text, 'html.parser')
    records = soup.find_all("div", class_="resu")
    resultsDictionary = {}

    j = 0
    for i in records:
        ticket_price = i.find("div", class_="price").span.text.replace(" ", "").replace("\n", "").replace("\r", "")
        ticket_price_digit = i.find("div", class_="price").span.text.replace(" ", "").replace("\n", "").replace("\r", "").replace(",", "")
        if i.find("div", class_="price").find("div", class_="icon11"):
            ticket_type = i.find("div", class_="price").find("div", class_="icon11").text.replace(" ", "").replace("\n", "").replace("\r", "").replace("\t\t\t\t\t\t\t\t\t\t\t", "")
        elif i.find("div", class_="price").find("div", class_="icon10"):
            ticket_type = i.find("div", class_="price").find("div", class_="icon10").text.replace(" ", "").replace("\n", "").replace("\r", "").replace("\t\t\t\t\t\t\t\t\t\t\t", "")
        flight_hour = i.find(class_="date").text.replace(" ", "").replace("\n", "").replace("\r", "")
        flight_free_seats = i.find(class_="user").text.replace(" ", "").replace("\n", "").replace("\r", "")
        airline = i.find("div", class_="info_parvaz efitooltip_bg").find(class_="efitooltip").find(class_="mkfcol1").find(class_="airline_name").text.replace("\n", "").replace("\r", "")
        flight_number = i.find("div", class_="code").find("span", class_="code_inn").text.replace(" ", "").replace("\n", "")

        if ticket_price != "CLOSE":
            if ticket_price != "CANCEL":
                if flight_free_seats != '0':
                    resultsDictionary[j] = {
                        "price": ticket_price,
                        "priceDigit": int(ticket_price_digit),
                        "ticket_type": ticket_type,
                        "freeSeats": flight_free_seats,
                        "departure": flight_hour,
                        "company": airline,
                        "flight_number": flight_number,
                    }
            # print(resultsDictionary)

        elif ticket_price == "CLOSE" or ticket_price == "CANCEL" or flight_free_seats == '0':
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