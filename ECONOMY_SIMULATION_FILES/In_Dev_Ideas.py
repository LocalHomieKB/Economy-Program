"""
Developing the datainputter function to a usable and eventually an advanced state akin to a simulation of Vic 2
#Immigration_percent is dependent on literacy,GDP,employment_rate (lower=high_immigration)
# total_welfare(higher better), taxes.
#In order of importance highest to lowest. With high mid and low being referred to.
#Immigrants will be defined as separate classes of high, mid, low and refugee.
#for lower class population: total welfare, literacy, taxes, employment_rate, GDP
# for middle class population: employment_rate, GDP, literacy, taxes, total welfare
# for upper class population: literacy, taxes, employment_rate, GDP, total welfare
# For immigrants the categories of desire are:
# for lower class population: employment_rate, total welfare, literacy, taxes, GDP
# for middle class population: employment_rate, employment_rate(intentional double),
# literacy, taxes, GDP,total welfare
# for upper class population: employment_rate(relative to base e.g. assume the home countries
# employment rate to be base, unless theyre 3rd country in which case a separate variable is necessary
# , 3rd countries will have a minute upper attraction. Its guiding features will be,
# the country attractiveness relevant to the home and tourist country,
# So consider what affects immigration as what is better about this country in comparison to that one,
# Ideally 3 variables will exist. Neighbour, continent, interglobal. Typed in order
# of relative immigration amounts. Even if employment is high a 3rd world country
# will only have so many people capable of purchasing VISA's etc. One change will be 
# upper populations have refugees as well as the other regions. 3rd class will have highest
# , mid will have a very small amount apart from criminal asylums. The high class
# may have more appearance in rich countries due to tax asylums and/or other fraud related 
# crimes. literacy, taxes, GDP, total welfare
# for refugee class population: employment_rate, total welfare, literacy, taxes, GDP
# employment must be more important for middle than low, welfare most for low, taxes for the rich,
#  are highest then middle and low are the same. GDP high, mid, low, lit high, mid, low.
#  For most variables, desirability is in order of which class you desire.


Additionally the following features would revolutionise the program:
Industrial performance
Residential performance
Construction index
Resource economy (Each country,city,region analysed shall be defined by three tangible resources:
Beyond which population factors in but isn't a part of. For a country like Greece it would be:
Fish? Cars? fraud?
Capital uncertainity: Similar to the evaluation of stock traders based on its performance:
    - Recession
    - Long time weak performance
    - 1.00 indicates great capital certainity, any number below is poor and has integral effects on:
        - Stock investments
        - Trade
        - Immigration
        - High wealth class spending
    
Trade - defined by random non printed events(unless printed for debugging reason to introduce:
    -Randomness
    -Replayability

Random or pre-defined or self-defined or self-defining trade acts. These will have some arbitrary
some free-from effects on public services, resource economy e.t.c. Think "Democracy 2016", HOI4
focuses. And other Paradox game idea systems
"""