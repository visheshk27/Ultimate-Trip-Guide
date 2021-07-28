from countryinfo import CountryInfo

def hotel():
  hotel = input("Enter Your location:")
  country = CountryInfo(hotel)

  data = country.capital()
  data1 = country.currencies()
  data2 = country.languages()
  data3 = country.timezones()
  data4 = country.wiki()
  print(data,"\n",data1,"\n",data2,"\n",data3,"\n",data4)