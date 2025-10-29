"""
Flight ticket scraper module.
This module fetches flight information from ticket-charter.com
"""

from bs4 import BeautifulSoup
import requests
from datetime import datetime


def flights_handler(departureCity, destinationCity, dateOrder):
    """
    Fetch flight information from ticket-charter.com.
    
    Args:
        departureCity (str): Departure city name
        destinationCity (str): Destination city name
        dateOrder (str): Flight date in Jalali format
    
    Returns:
        dict or False: Dictionary of available flights or False if no flights found
    """
    url = f'http://ticket-charter.com/Ticket-{departureCity}-{destinationCity}.html?t={dateOrder}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching flight data: {e}")
        return False
    
    soup = BeautifulSoup(response.text, 'html.parser')
    records = soup.find_all("div", class_="resu")
    results_dictionary = {}

    for j, record in enumerate(records):
        try:
            # Extract price information
            price_div = record.find("div", class_="price")
            if not price_div or not price_div.span:
                continue
                
            ticket_price = price_div.span.text.replace(" ", "").replace("\n", "").replace("\r", "")
            
            # Skip closed or cancelled tickets
            if ticket_price in ["CLOSE", "CANCEL"]:
                continue
            
            ticket_price_digit = ticket_price.replace(",", "")
            
            # Extract ticket type
            ticket_type = None
            if price_div.find("div", class_="icon11"):
                ticket_type = price_div.find("div", class_="icon11").text.strip()
            elif price_div.find("div", class_="icon10"):
                ticket_type = price_div.find("div", class_="icon10").text.strip()
            
            # Extract flight details
            flight_hour = record.find(class_="date").text.strip() if record.find(class_="date") else "N/A"
            flight_free_seats = record.find(class_="user").text.strip() if record.find(class_="user") else "0"
            
            # Skip if no seats available
            if flight_free_seats == '0':
                continue
            
            # Extract company and flight number
            info_div = record.find("div", class_="info_parvaz efitooltip_bg")
            if info_div:
                airline_elem = info_div.find(class_="airline_name")
                flight_company = airline_elem.text.strip() if airline_elem else "N/A"
            else:
                flight_company = "N/A"
            
            code_div = record.find("div", class_="code")
            if code_div:
                code_span = code_div.find("span", class_="code_inn")
                flight_number = code_span.text.strip() if code_span else "N/A"
            else:
                flight_number = "N/A"

            results_dictionary[j] = {
                "price": ticket_price,
                "priceDigit": int(ticket_price_digit),
                "ticketType": ticket_type or "اکونومی",
                "freeSeats": flight_free_seats,
                "departure": flight_hour,
                "company": flight_company,
                "flightNumber": flight_number,
            }
        except (AttributeError, ValueError) as e:
            print(f"Error parsing flight record {j}: {e}")
            continue

    return results_dictionary if results_dictionary else False