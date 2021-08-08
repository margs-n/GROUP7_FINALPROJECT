import discord
import os
import requests
import json

#BOT TOKEN
my_secret = 'ODczMzg1MzA3OTc2OTEyOTY2.YQ3pdA.8yY-gZTcHaNTsJY99kYDn7TbSv0'

#PASSWORD
password = "joeisthebest"

#HISTORY
history = {}

#ADMINS LIST
admins_list = []

#DICTIONARIES
loc = {'AFGHANISTAN': 'AFN', 'AKROTIRI AND DHEKELIA': 'EUR', 'ALAND ISLANDS': 'EUR', 'ALBANIA': 'ALL', 'ALGERIA': 'DZD', 'AMERICAN SAMOA': 'USD', 'ANDORRA': 'EUR', 'ANGOLA': 'AOA', 'ANGUILLA': 'XCD', 'ANTIGUA AND BARBUDA': 'XCD', 'ARGENTINA': 'ARS', 'ARMENIA': 'AMD', 'ARUBA': 'AWG', 'ASCENSION ISLAND': 'SHP', 'AUSTRALIA': 'AUD', 'AUSTRIA': 'EUR', 'AZERBAIJAN': 'AZN', 'BAHAMAS': 'BSD', 'BAHRAIN': 'BHD', 'BANGLADESH': 'BDT', 'BARBADOS': 'BBD', 'BELARUS': 'BYN', 'BELGIUM': 'EUR', 'BELIZE': 'BZD', 'BENIN': 'XOF', 'BERMUDA': 'BMD', 'BHUTAN': 'BTN', 'BOLIVIA': 'BOB', 'BONAIRE': 'USD', 'BOSNIA AND HERZEGOVINA': 'BAM', 'BOTSWANA': 'BWP', 'BRAZIL': 'BRL', 'BRITISH INDIAN OCEAN TERRITORY': 'USD', 'BRITISH VIRGIN ISLANDS': 'USD', 'BRUNEI': 'BND', 'BULGARIA': 'BGN', 'BURKINA FASO': 'XOF', 'BURUNDI': 'BIF', 'CABO VERDE': 'CVE', 'CAMBODIA': 'KHR', 'CAMEROON': 'XAF', 'CANADA': 'CAD', 'CARIBBEAN NETHERLANDS': 'USD', 'CAYMAN ISLANDS': 'KYD', 'CENTRAL AFRICAN REPUBLIC': 'XAF', 'CHAD': 'XAF', 'CHATHAM ISLANDS': 'NZD', 'CHILE': 'CLP', 'CHINA': 'CNY', 'CHRISTMAS ISLAND': 'AUD', 'COCOS ISLANDS': 'AUD', 'COLOMBIA': 'COP', 'COMOROS': 'KMF', 'CONGO, DEMOCRATIC REPUBLIC OF THE': 'CDF', 'CONGO, REPUBLIC OF THE': 'XAF', 'COOK ISLANDS': 'NZD', 'COSTA RICA': 'CRC', "COTE D'IVOIRE": 'XOF', 'CROATIA': 'HRK', 'CUBA': 'CUP', 'CURACAO': 'ANG', 'CYPRUS': 'EUR', 'CZECHIA': 'CZK', 'DENMARK': 'DKK', 'DJIBOUTI': 'DJF', 'DOMINICA': 'XCD', 'DOMINICAN REPUBLIC': 'DOP', 'ECUADOR': 'USD', 'EGYPT': 'EGP', 'EL SALVADOR': 'USD', 'EQUATORIAL GUINEA': 'XAF', 'ERITREA': 'ERN', 'ESTONIA': 'EUR', 'ESWATINI': 'SZL', 'ETHIOPIA': 'ETB', 'FALKLAND ISLANDS': 'FKP', 'FAROE ISLANDS': 'DKK', 'FIJI': 'FJD', 'FINLAND': 'EUR', 'FRANCE': 'EUR', 'FRENCH GUIANA': 'EUR', 'FRENCH POLYNESIA': 'XPF', 'GABON': 'XAF', 'GAMBIA': 'GMD', 'GEORGIA': 'GEL', 'GERMANY': 'EUR', 'GHANA': 'GHS', 'GIBRALTAR': 'GIP', 'GREECE': 'EUR', 'GREENLAND': 'DKK', 'GRENADA': 'XCD', 'GUADELOUPE': 'EUR', 'GUAM': 'USD', 'GUATEMALA': 'GTQ', 'GUERNSE': 'GGP', 'GUINEA': 'GNF', 'GUINEA-BISSAU': 'XOF', 'GUYANA': 'GYD', 'HAITI': 'HTG', 'HONDURAS': 'HNL', 'HONG KONG': 'HKD', 'HUNGARY': 'HUF', 'ICELAND': 'ISK', 'INDIA': 'INR', 'INDONESIA': 'IDR', 'INTERNATIONAL MONETARY FUND': 'XDR', 'IRAN': 'IRR', 'IRAQ': 'IQD', 'IRELAND': 'EUR', 'ISLE OF MAN': 'IMP', 'ISRAEL': 'ILS', 'ITALY': 'EUR', 'JAMAICA': 'JMD', 'JAPAN': 'JPY', 'JERSEY': 'JEP', 'JORDAN': 'JOD', 'KAZAKHSTAN': 'KZT', 'KENYA': 'KES', 'KIRIBATI': 'AUD', 'KOSOVO': 'EUR', 'KUWAIT': 'KWD', 'KYRGYZSTAN': 'KGS', 'LAOS': 'LAK', 'LATVIA': 'EUR', 'LEBANON': 'LBP', 'LESOTHO': 'LSL', 'LIBERIA': 'LRD', 'LIBYA': 'LYD', 'LIECHTENSTEIN': 'CHF', 'LITHUANIA': 'EUR', 'LUXEMBOURG': 'EUR', 'MACAU': 'MOP', 'MADAGASCAR': 'MGA', 'MALAWI': 'MWK', 'MALAYSIA': 'MYR', 'MALDIVES': 'MVR', 'MALI': 'XOF', 'MALTA': 'EUR', 'MARSHALL ISLANDS': 'USD', 'MARTINIQUE': 'EUR', 'MAURITANIA': 'MRU', 'MAURITIUS': 'MUR', 'MAYOTTE': 'EUR', 'MEXICO': 'MXN', 'MICRONESIA': 'USD', 'MOLDOVA': 'MDL', 'MONACO': 'EUR', 'MONGOLIA': 'MNT', 'MONTENEGRO': 'EUR', 'MONTSERRAT': 'XCD', 'MOROCCO': 'MAD', 'MOZAMBIQUE': 'MZN', 'MYANMAR': 'MMK', 'NAMIBIA': 'NAD', 'NAURU': 'AUD', 'NEPAL': 'NPR', 'NETHERLANDS': 'EUR', 'NEW CALEDONIA': 'XPF', 'NEW ZEALAND': 'NZD', 'NICARAGUA': 'NIO', 'NIGER': 'XOF', 'NIGERIA': 'NGN', 'NIUE': 'NZD', 'NORFOLK ISLAND': 'AUD', 'NORTHERN MARIANA ISLANDS': 'USD', 'NORTH KOREA': 'KPW', 'NORTH MACEDONIA': 'MKD', 'NORWAY': 'NOK', 'OMAN': 'OMR', 'PAKISTAN': 'PKR', 'PALAU': 'USD', 'PALESTINE': 'ILS', 'PANAMA': 'USD', 'PAPUA NEW GUINEA': 'PGK', 'PARAGUAY': 'PYG', 'PERU': 'PEN', 'PHILIPPINES': 'PHP', 'PITCAIRN ISLANDS': 'NZD', 'POLAND': 'PLN', 'PORTUGAL': 'EUR', 'PUERTO RICO': 'USD', 'QATAR': 'QAR', 'REUNION': 'EUR', 'ROMANIA': 'RON', 'RUSSIA': 'RUB', 'RWANDA': 'RWF', 'SABA': 'USD', 'SAINT BARTHELEMY': 'EUR', 'SAINT HELENA': 'SHP', 'SAINT KITTS AND NEVIS': 'XCD', 'SAINT LUCIA': 'XCD', 'SAINT MARTIN': 'EUR', 'SAINT PIERRE AND MIQUELON': 'EUR', 'SAINT VINCENT AND THE GRENADINES': 'XCD', 'SAMOA': 'WST', 'SAN MARINO': 'EUR', 'SAO TOME AND PRINCIPE': 'STN', 'SAUDI ARABIA': 'SAR', 'SENEGAL': 'XOF', 'SERBIA': 'RSD', 'SEYCHELLES': 'SCR', 'SIERRA LEONE': 'SLL', 'SINGAPORE': 'SGD', 'SINT EUSTATIUS': 'USD', 'SINT MAARTEN': 'ANG', 'SLOVAKIA': 'EUR', 'SLOVENIA': 'EUR', 'SOLOMON ISLANDS': 'SBD', 'SOMALIA': 'SOS', 'SOUTH AFRICA': 'ZAR', 'SOUTH GEORGIA ISLAND': 'GBP', 'SOUTH KOREA': 'KRW', 'SOUTH SUDAN': 'SSP', 'SPAIN': 'EUR', 'SRI LANKA': 'LKR', 'SUDAN': 'SDG', 'SURINAME': 'SRD', 'SVALBARD AND JAN MAYEN': 'NOK', 'SWEDEN': 'SEK', 'SWITZERLAND': 'CHF', 'SYRIA': 'SYP', 'TAIWAN': 'TWD', 'TAJIKISTAN': 'TJS', 'TANZANIA': 'TZS', 'THAILAND': 'THB', 'TIMOR-LESTE': 'USD', 'TOGO': 'XOF', 'TOKELAU': 'NZD', 'TONGA': 'TOP', 'TRINIDAD AND TOBAGO': 'TTD', 'TRISTAN DA CUNHA': 'GBP', 'TUNISIA': 'TND', 'TURKEY': 'TRY', 'TURKMENISTAN': 'TMT', 'TURKS AND CAICOS ISLANDS': 'USD', 'TUVALU': 'AUD', 'UGANDA': 'UGX', 'UKRAINE': 'UAH', 'UNITED ARAB EMIRATES': 'AED', 'UNITED KINGDOM': 'GBP', 'UNITED STATES OF AMERICA': 'USD', 'URUGUAY': 'UYU', 'US VIRGIN ISLANDS': 'USD', 'UZBEKISTAN': 'UZS', 'VANUATU': 'VUV', 'VATICAN CITY': 'EUR', 'VENEZUELA': 'VES', 'VIETNAM': 'VND', 'WAKE ISLAND': 'USD', 'WALLIS AND FUTUNA': 'XPF', 'YEMEN': 'YER', 'ZAMBIA': 'ZMW', 'ZIMBABWE': 'USD'}

client = discord.Client()

@client.event
async def on_ready():
  print(f'We have logged in as {client}')
  
@client.event
async def on_message(message): ###################

  #EXCHANGE RATES
  r = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=dabaf50525f859ba84ed0de3775bdb0f")
  dictionary = r.json()
  exchange_rates = dictionary['rates']
  valid_keys = list(exchange_rates.keys())

  msg = message.content
  msg = msg.upper()

  user = str(message.author)
  user_code = user[-4:]
  name = user[0:user.find('#')]

  def convert_message():
    orig_money = round(float(msg[6:msg.find(' ',6)]),2)
    currency1 = msg[msg.find(' ',6)+1:msg.find("TO")-1]
    currency2 = msg[-3:]
    if currency1 in valid_keys and currency2 in valid_keys:
      euro = exchange_rates[currency1]
      conversion = exchange_rates[currency2]/euro
      final_money = orig_money*conversion
      response = (f'\nThe current rate of {currency1} to {currency2} is {conversion}.\n {orig_money} {currency1} is {round(final_money,2)} {currency2}. Thank you! :money_mouth:')
      return response 

  def get_currency():
    country = msg[6:].upper()
    if country in list(loc.keys()): 
       currentcurrency = loc[country]
       response = (f'\nThe currency of {country} is {currentcurrency}. Thank You! :money_mouth:')
       return response

  if message.author == client:
    return

  if msg[0:5].upper() == '#CONV':
    try:
      await message.channel.send(convert_message())
      if name in history:
        history[name].append(msg[6:])
      else:
        history[name] = [msg[6:]] 
    except: 
      await message.channel.send("Converter Bot responses using the **#CONV** function must be formatted as **#CONV [AMOUNT] [CUURENT CURRENCY] TO [DESIRED CURRENCY]**. *EX: #CONV 500 PHP TO USD*. The currency you have inputted might also not be available. For more information please call the function #HELP :cry:")

  if msg[0:5].upper() == '#CURR':
    try:
      await message.channel.send(get_currency())
    except: 
      await message.channel.send("We are sorry but Converter Bot was not able to process your request. We may not have the country's currency that you have inputted or you must have entered the wrong format. Converter Bot responses using the **#CURR** function must be formatted as **#CURR [COUNTRY]**. *EX: #CURR PHILIPPINES*. For more information please call the function **#HELP** :cry:")

  if msg[0:].upper() == "#HELP":
    await message.channel.send('\nRemember the following when using Converter Bot:\n\t**#CONV** function :hugging: : \n\t\tThe **#CONV** function converts an amount of a currency to a specified currency. \n\t\t\t-Converter Bot responses must be formatted as:\n\t\t\t**#CONV [AMOUNT] [CURRENT CURRENCY] TO [DESIRED CURRENCY]**\n\t\t\t-*EX: #CONV 500 PHP TO USD*\n\t\t\t-You must have only one # at the start\n\t\t\t(Please note we do not accept the following currencies and country: **VES (Venezuela)**,\n\t\t\t**SSP (Sao Tome And Principe)**, **STN (South Sudan)**, and **MRU(Mauritania)**\n\n\t**#CURR** function:\n\t\tThe **#CURR** function identifies the currency of a specified country. \n\t\t\t-Converter Bot responses must be formatted as: **#CURR [COUNTRY]**\n\t\t\t-*EX: #CURR PHILIPPINES*\n\n\t**#MYHISTORY** function:\n\t\tThe **#MYHISTORY** function gives your transaction history with us.\n\t\t\t-Converter Bot responses mus be formatted as: **#MYHISTORY**\n\t\t\t-*EX: #MYHISTORY*\n\n\t**#RATES** function:\n\t\tThe **#RATES** function will give you the rates of all available countries from your currency.\n\t\t\t-Converter Bot responses must be formatted as: **#RATES [currency]**\n\t\t\t-*EX: #RATES PHP*')

  if msg.upper() == '#HISTORY':
    if user_code in admins_list:
      await message.channel.send(history)
    else:
      await message.channel.send(f"I'm sorry {name} but you do not have authorization to use this command. If you are an admin please input the password after **#PASSWORD**")
  
  if msg.upper() == "#MYHISTORY":
    try:
      await message.channel.send(f'Hi {name} here is a list of your previous transactions:\n{history[name]}')
    except:
      await message.channel.send(f"Sorry {name}, you have not made any transactions with me yet! :cry:")

  if msg.upper()[0:6] == "#RATES":
    rate_list = []
    currency = msg[7:10]
    if currency in valid_keys:
      for j in exchange_rates:
        euro = exchange_rates[currency]      
        conversion = round(exchange_rates[j]/euro,2)
        rate_list.append([j,conversion])
      await message.channel.send(f'Hi {name} here are the current conversion rates for {currency} :\n\n {rate_list[0:84]}')
      await message.channel.send(rate_list[84:]) 
    else:
      await message.channel.send(f"Sorry {name} but we do not carry the currency: '{msg[7:]}' :cry: ")

  if message.content.upper()[0:9] == "#PASSWORD":
    if message.content[10:] == password:
      admins_list.append(user_code)
      await message.channel.purge(limit=1)
      await message.channel.send("You have inputted the correct password. You are now an admin.")
    else:
      await message.channel.send('You have inputted an incorrect password')

client.run(my_secret)