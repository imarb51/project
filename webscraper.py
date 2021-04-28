import requests
from bs4 import BeautifulSoup
import pandas

oyo_url ="https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num_=3

for page_num in range(1,page_num_):
    req = requests.get(oyo_url + str(page_num))
    content=req.content

    soup = BeautifulSoup(content , "html.parser")

    all_hotels=soup.find_all("div", {"class" : "HotelCardListing"})
    scraped_info_list=[]

    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["name"] = hotels.find("h3", {"class": "ListingHotelDescription_hotelName"}).text
        hotel_dict["address"]=hotels.find("span",{"itemprop" : "StreetAddress"}).text
        hotel_dict["price"] = hotel.find("span", {"class": "lstingPrice__finalPrice"}).text
        try:
            hotel_dict["rating"] = hotel.find("span", {"class": "hotelRating__ratingSummary"}).text
        except ArithmeticError:
            pass

        parent_amenities_elements=hottel.find("div" , {"class": "amenityWrapper"})

        amenities_list=[]
        for amenity in parent_amenities_elements.find_all("div" , {"class": "amenityWrapper__amenity"}):
            amenities_list.append(amenity.find("span", {"class" : "d-body-sm"}).text.strip())

        hotel_dict["amenities"] = ', '.join(amenities_list[:-1])

        scraped_info_list.append(hotel_dict)

    dataFrame=pandas.DataFrame(scraped_info_list)
    dataFrame.to_csv("Oyo.csv")


