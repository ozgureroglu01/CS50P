 # Currency Converter
    #### Video Demo:  https://youtu.be/9RrmkgXsUyw
    #### Description: First a little explanation about what a currency converter is:
    A currency converter is a tool or application that allows users to convert the
    value of one currency to another. Currency converters typically use the current exchange
    rate between two currencies to perform the conversion.
    A currency converter can be useful for a variety of purposes, such as traveling,
    online shopping, and financial planning. For example, if someone is planning a trip
    to a foreign country, they may use a currency converter to determine how much money
    they will need to exchange for the local currency. Similarly, if someone is shopping
    online from a website that displays prices in a foreign currency, they may use a currency
    converter to determine the equivalent price in their local currency.
    My program takes two country names from the user then turns the names of the countries to
    respected countries currency and finally converts the one currency for another.First country
    name is the one currency will be converted from. My code take input as country name then converts
    the name into that country's currency after it takes input as another country name this country
    is the one previous currency will be converted to. My code also converts this country's name to
    it's currency. Finally it takes an amount as in money and converts one currency to another.

    More in depth: in the get convert from function it takes the first input(the one currency will be converted from)
    value and gives back the currency name of the said country and it checks if the currency converter apı supports that
    currency (sometimes one country has more than one currency name)by checking the currency name with supported countries
    list of dictionary if it doesn’t it look until it find the one currency name that does and the value(name of the currency)
    gets returned to a variable after that get convert to function also takes the second input(the one currency will be converted to)
    value and gives back the currency name of the said country and it checks if the currency converter apı supports that currency by
    checking the currency name with supported countries list of dictionary (sometimes one country has more than one currency name)
    if it doesn’t it look until it find the one currency name that does and the value(name of the currency) gets returned to a variable
    after that program ask for an amount (of money) than all three values(one from get convert from,one from get convert to,and amount(of money)
    gets pass as an argument to the convert method which converts the first value(ne from get convert from) to second value(one from get convert to)
    and multiply(if necessary) with amount(of money) and returns the final value to be printed out.in a file called test project
    the three functions(get convert from, get convert to and convert) are tested with unit testing methods in an another file called
    requirements txt are the modules you need to execute this program.
    And in the readme.md file is the description fort he program as well as a link to a short video with demonstration

