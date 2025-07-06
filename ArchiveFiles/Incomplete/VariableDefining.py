#Variable Defining:
#Merge these variables:
#All this code needs to implement gradual changes not new definitions each time
LITERACY += TOTAL_WELFARE * 0.00001 - LITERACY * 0.01 + 0.005
PUBLIC_SPENDING = 0.1 * GDP
HEALTHCAREEFFICIENCY = ((PUBLIC_SPENDING / 1000000) / 2 + 0.4) #THis results in it being equal to 0.6 at start
# The 1000000 is only suitable for small simulations, it will represent
#the peak of GDP that should be attainable meaning more can be spent on healthcare
#0.4 represents base healthcare, which at its lowest should equal this
#in year 1 with no other changes it should equal 0.45
#unsure code :YEARLY_MORTALITY_RATE = ((((2/3) * 0.0076 * POPULATION) + (0.0024 * POPULATION)) / POPULATION)
#first bracket=Elderly Death second bracketHealth Related Deaths
#unsure code:IMMIGRATION_RATE = 0.005 * POPULATION - (CRIME * 1000) + (HEALTHCARE * 1000) - (YEARLY_MORTALITY_RATE * POPULATION)
#POPULATION =(100 * IMMIGRATION_RATE * 0.06) - (YEARLY_MORTALITY_RATE) For debugging pop increases by 100 each year
POPULATION += 100
#Bad Code : events already determined : CRIME = 0.07952 * POPULATION
WORKING_AGE_POPULATION = (0.6 * POPULATION) - (HOMELESSRATE * POPULATION)
UNEMPLOYED_POPULATION = (0.1 * POPULATION) + (HOMELESSRATE * POPULATION)
#Bad Code : just use a real equation : GDP = WORK_EFFICIENCY * (0.6 * POPULATION)
TOTAL_SALARIES_PAID = WORKING_AGE_POPULATION * 5
TOTAL_WELFARE = (UNEMPLOYED_POPULATION * 2) + (HOMELESSRATE * POPULATION * 4)
TAXINCOME = POPULATION * 10
CAPITAL_AVAILABLE = TAXINCOME - TOTAL_WELFARE - TOTAL_SALARIES_PAID - PUBLIC_SPENDING 
#Needs to calculate tax income somehow
YEAR = 1960
TAXINCOME = 50000
#TaxRate = 0.05
POPULATION = 5000
WORK_EFFICIENCY = 0.6 #Based partially on: technology, education, resistance by working class
LITERACY = 0.5
PUBLIC_SPENDING = 20000
IMMIGRATION_RATE = 0.05 #Needs to represent emigration-immigration
WORKING_AGE_POPULATION = 3000
UNEMPLOYED_POPULATION = 500
#RichPopValue = RichPopulation * 100
#WorkingPopValue = (WorkEfficiency * WorkingAgePopulation) * (24 * 7) * 350
#WorkingAgePopulation = 0.8 * Population
#UnemployedPopulation = 0.2 * Population
#RichPopulation = 0.1 * Population
TOTAL_SALARIES_PAID = 15000
#TotalSalariesPaid = WorkingAgePopulation * 400
#TotalWelfare = UnemployedPopulation * 150
#TotalScore = 90348800000
#ValueOfTown = 1129360000
TOTAL_WELFARE = 1000
GDP = 100000
YEARLY_MORTALITY_RATE = 0.035
HEALTHCAREEFFICIENCY = 0.6
ECONOMICDEVELOPMENT = 0.5
HOMELESSRATE = 0.05