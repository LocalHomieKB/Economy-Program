Wild West Notes

  
  

let’s simply make this small part of the program, that’s it, no more events,

 no randomising just this simple static little visual text based game.

"""

  
  

    ◦   use script scheme from economy simulation, use

     also character generation and a simple economy scheme.

     based on The economy  three arrows down to booze, ladies,

      robberies. Your economy relies on the amount and strength

      of these 3 products. Therefore the stronger these 3 are the

      stronger your economy, the higher your immigration rate,

      lowering these numbers down again. In an ideal world each

      person has traits affecting the amount of each he will want.

       With only 3 each person can have a base and one up and one

        down for each one based on a dice roll. Something like a

        dwarf fortress interface i would like but honestly every

        game maker seems like dog shit made for 2d side scrollers

        or 3rd person games. I just need a strategy game game maker.

        Maybe we could jerry rig a rpg maker game into this.

         The economy is a figure known as accountant. Each dialogue

         choice says the abundance of each product. Too much of

         certain ones should bring their own impacts, as well as

          too little of some. Then the 3 products are represented

           by another figure each. And then we could think about

            1 or 2 figures underneath each one. To reduce the

             feeling of an rpg you could send people on missions,

             after which recovery would also be based on the 3 products.

             At the start it will be easy to meta and it will likely be

             very short days, but with more random events it could be

             better. stage one accountant and all in the bar. He just

            works at one of the tables with a ledger in front of him and

            other papers. Stage 2 an office for you as the mayor and the

             accountant and 3 representatives in each of their respective

              areas e.g. distillery/bar, brothel, bar for robbers

    ◦   Step 1 Download the most compatible RPG maker or GM maker or something else you find for 2d strategy even something like civ ffs. Potentially defold, use something called an ECS, do i need c++ to do this?

    ◦   step 2 Tile set if needed new or find one

    ◦   step 3 Now the accountant design

    ◦   step 4 the three products looks

    ◦   step 5 now dialog for accountant

    ◦   step 6 now dialog for 3 products

    ◦   step 7 scripting with 50 50 chance for an increase in a products abundance .

"""

  
  

#Economy - Booze, Ladies, Robbery

# Booze - Distilling, Trade

# Ladies - Kidnapping, buying

# Robbery - On the road, in the town

# Distilling - Distillery owner

# Trade - Merchant

# Kidnapping - Highway robber

# Buying - Pimp

# On the road - Highway robber #2

# In the town - Scallywag

  

Each of these topics would be covered by a character and

their associated image, he'd discuss its current situation

how to change it, and direct actions to influence it.

  

Actual picture could either be a rpg maker character

a picture like in King of dragon pass, or as a building

or symbol for a building. or just as words for a menu

  
  

# actually maybe it’s just a town in the wild west, with a tavern, and movement is

# likely. Though if you provide the right

# services there’s a chance people coming through will settle, if they’re cowboys

# they’ll have specific traits and jobs

# that help your town uniquely to them. These guys can settle impromptu without

# a house, but some types like accountants

# will need their own space. The game should start with a group of cowboys,

# each can be assigned to any job and

# although

#     they’re jack of all trades there is some levity in their skills. For example

#      for 5 stats there’s maximum of 4 skill

#     points up it could go down, at a chance of 1% that it could go this high,

#     for example perception 9 instead of 5

#     besides

#      any other changes would take a 1% odd. So after a while of operating and

#      getting some immigrants you can build

#      specialised buildings for them. ANd start replacing cowboys with

#      profesional workers, after all not everyone wants

#       a knife wielding gunslinger as their barber. The growth and birth

#       randomisation can be imported. The chances of

#       immigration and all that simulation can also be imported, to at the

#       beginning happen turn based with eventual

#       real time changing with natural changes in migration, although most

#       likely like this. You’re in the centre of

#       5 towns around you, north, south east, south west, east and west,

#       for someone from the north to go south east

#       it is very likely they will go through you, if either your area is

#       appealing enough or if it is too dangerous

#       to move through the wild west they’ll stay with you, either for a

#        night or more, maybe convince them with some

#       escorts to see if you could get that towns favour.

  
  
  

*/

  

Commodities and trading:

  

#An event. Trader invests in stock of commodity. Fetches the position of the commodity, then fetches the price of the commodity and name.

#A fixed list makes this easier.

  

//When a trader visits the town, they compare what they need in their origin town, compare to stock in this town, and

//decide based on price how much they should buy. Price needs to move dynamically

  

    //AI Caravans

    //  Its rules:

        # (Town Name), (Town location) wants to trade with (TN), (TL). If adjacent it

#  simulates it. Trade Value for TN1 + 3(they sell and buy in one turn),Trade

#   value for TN2+2(they sell bormally but buy a limited amount from the caravan).

  

# # These decisions should be based on what the caravan either specifically

# holds(Developed after it become a game) or predicted to (What the town produces

#  versus how much the other town needs it) If a towns specialty is oil gathering

#  its priority to sell would be at some point 100% meaning up to 25% percent of

#   its holding caravan space would be designated for it. If another town is oil

#   processing regardless of what size it has a high priority to buy this up to

#    the point where it has reserves for at least 7 turns. Trade happens every

#    7 turns.

# Trade happens every 7 turns. They schedule imports 2 days before this? If we are

#  to simulate an external economy this would be needed to ensure these towns

#  don’t die. So if we have two primary food producers, one oil producer, one

#  construction material producer, and one population producer .

  
  

# Chance of a caravan being caught should have a number peaking between 8pm and

# 6am.  lowest between 12pm and 3pm And a static 10% chance for all other hours.

# CHance of succes should be based on each event, although some shouldn’t be all

# bad. Think oregon valley. There should be a choice to designate a patrol of

# some size to decrease chance of bad events in one or all 5 paths between your

# town and others. Sometimes you may get missions to patrol these when there’s

# rare cargo, important people or simply a relationship boost at hand.