# Entranched.
# A tranche creation and education program

import random
from random import randint
import time
from time import sleep
print("What is a tranche"
      "A tranche is a 'basket' of non physical 'credit obligations' and physical 'assets'"
      "CDO - Credit Debt Obligation, gambling on the ability of a company to pay its debt"
      "CDS - Credit Default Swap, gambling on the ability of mortgage payees not defaulting on payments, and when "
      "they do depending on your position in the tranche you may lose your position"
      "Tranches depend on ratings from ratings agencies such as 'Moodys' in order to inform investors on the safety"
      "of their investment"
      "Ratings range from FFF rating at its lowest to AAA for the best quality"
      ""
      "Default values:"
      "'Equity' tranche = 3% losses"
      "'Mezzanine' tranche = 3%-7% losses (insulated by the 'equity' tranche up to 3% losses)"
      "'Junior Senior' tranche = 7%-10% losses (insulated by 'Mezzanine' tranche up to 7% losses)"
      "'Regular Senior' tranche = 10%-15% losses (insulated by 'Junior Senior' tranche up to 10% losses"
      "'Super Senior' tranche = 15%-30% losses (insulated by 'Regular Senior' tranche up to 15% losses safest tranche)"
      ""
      "The expected tranche sizes depend on the number and timing of any future default and the expected costs of"
      "these future defaults(ie recovery rates)"
      "Pricing tranches:"
      "The premium on a tranche is the spread paid by the protection buyer that equates the expected present value of"
      "default costs to be borne by the protection seller('protection leg') to the expected present value of investing"
      "in the tranche('premium leg')"
      "(Source(Amato,Gyntelberg/BIS (2005))"
      "The value of the premium leg is present value of spread payments the protection seller receives from the "
      "protection buyer"
      "Expected present value of 'Premium leg': V(sub)prem = S*E[sigma(super)M(sub)i-1*D(0,t(sub)i)*N(t(sub)i)"
      "t being the quartely payment date M(t=t(sub)1,t(sub)2...t(sub)M"
      "D(0,t(sub)i) is the uncertain discount factor of expected future income streams"
      "Tranche premium = S"
      "The present value of the 'premium leg' is made smaller by: low premium, low recovery rate, default losses"
      "incurred early"
      "Expected present value of the 'protection leg': "
      "V(sub)prot=E[sigma(super)M(sub)i-1*D(0,t(sub)i)*(N(t(sub)i)-N(t(sub)i-1))"
      "The present value of the 'protection leg' is made smaller by: tranche size unchanged, high recovery rate,"
      "defaults occure late during the contract period "
      "'Tranche premium' : (Solve) V(sub)prem=V(sub)prot /(or just)V(sub)prem/V(sub)prot"
      ""
      "Information is based on BIS quarterly review March 2005 unless specified differently"
      "To determine S you need to know the discount factors and future tranche sizes,"
      "For more on discount factors see Rebonato (2002)"
      "For more on future tranche sizes see below:"
      "1) losses-given-default:"
      "     -Assume a constant recovery rate of 40%, 1-recovery rate is the losses given default"
      "         -The recovery rate can also be estimate from CDS spreads but in this case we use the average historical"
      "          recovery rate on senior unsecured bonds for US corporations"
      "2) number of defaults:"
      "     -Estimated directly from single-name CDS spreads, directly from equity prices(Check Moody's KMV's expected"
      "      default frequencies)"
      "         -A recovery rate assumption is neded to extract default probabilities from CDS spreads"
      "3) timing of defaults:"
      "     -Timing of defaults for the N entities over the lifetime of the contract can be calculated from a joint"
      "      default time probability distribution. This is unknown assume default times follow an N-dimensional"
      "      multivariate normal distribution, ie the so-called Gaussian copula(see Nelsen(1999), Li(2000) and"
      "      Cherubini et al(2004))"
      "         -Example:one-factor Gaussian copula model is as follows and contains a latent random variable X(sub)i"
      "         -X(sub)i=(sqroot(p))*M+(sqroot(1-0))*Z(sub)i"
      "              Assumptions/Definitions"
      "             -M is a normally distributed random variable"
      "             -Z(sub)i's are mutually uncorrelated and normally distributed random variables"
      "             -(-1<p<1) is the constant pairwise correlation between default times"
      "                 -Hull and White(2004)"
      "                 -Estimated from correlatiions of equity returns in the range 0-30%"
      "             -Identical constant pairwise default time correlations"
      "             -Normally distributed default times"
      "             -Normal joint default probability distribution"
      "         -The model above can be interpreted to mean X(sub)i is the value of assets held by entity i, entity i"
      "          defaults if its assets fall below some threshold"
      "         -This model can be assumed to be a market standard for pricing tranches and see Nelsen(1999) for more"
      "         -This model is also simple thanks to its straightforward and easy to obtain(shorten) assumptions")

#Simulate a tranche of 100 assets of MBS, CDO, bond and residential properties.

print("A tranche of 100 assets is split based on the ratio 25/25/30/20"
      "Varying in price between 80-120, 100-150, 40-100, 300-400"
      "Their probability of default will be mainly random but each has roughy 1.5% chance of failure"
      "An investment in highest tier is safest, most expensive and least return, with an inverese relationship"
      "downwards")

def _RandomSplittingTheTranche_:
      mbs = 0.25
      cdo = 0.25
      bond = 0.3
      residential = 0.2
      junkbond = 0
      percentagesizeoftranche = cdo + mbs + bond + residential
      action = 1
      while action == 1:
            trancheassets = ("MBS", "CDO", "Bond", "Residential", "Junkbond")
            whichtrancheasset = randint(0,4)
            if whichtrancheasset == 0:
                  assetchange = randint(0,100)/100
                  print(str(assetchange))
                  plusorminus= randint(0,1)
                  print(str(plusorminus))
                  if plusorminus == 0:
                        mbs += assetchange
                  else:
                        mbs -= assetchange
            if whichtrancheasset == 1:
                  assetchange = randint(0,100)/100
                  print(str(assetchange))
                  plusorminus= randint(0,1)
                  print(str(plusorminus))
                  if plusorminus == 0:
                        cdo += assetchange
                  else:
                        cdo -= assetchange
            if whichtrancheasset == 2:
                  assetchange = randint(0,100)/100
                  print(str(assetchange))
                  plusorminus= randint(0,1)
                  print(str(plusorminus))
                  if plusorminus == 0:
                        bond += assetchange
                  else:
                        bond -= assetchange
            if whichtrancheasset == 3:
                  assetchange = randint(0,100)/100
                  print(str(assetchange))
                  plusorminus= randint(0,1)
                  print(str(plusorminus))
                  if plusorminus == 0:
                        residential += assetchange
                  else:
                        residential -= assetchange
            if whichtrancheasset == 4:
                  assetchange = randint(0,100)/100
                  print(str(assetchange))
                  plusorminus= randint(0,1)
                  print(str(plusorminus))
                  if plusorminus == 0:
                        cdo -= assetchange/4
                        mbs -= assetchange/4
                        bond -= assetchange/4
                        residential -= assetchange/4
                        junkbond += assetchange
                  else:
                        if junkbond > 0:
                              junkbond -= assetchange
                              if junkbond < 0:
                                    junkbond = 0
                        else:
                              break
            time.sleep(1)
            if percentagesizeoftranche != 1:
                  print("ERROR IN PERCENTAGE SIZE OF TRANCHE, ATTEMPTING REBALANCE:")
                  time.sleep(4)
                  restorationpoints = percentagesizeoftranche-1
                  actualrecoverypoints = restorationpoints / 3
                  if actualrecoverypoints > 0:
                        cdo += actualrecoverypoints
                        mbs += actualrecoverypoints
                        residential += actualrecoverypoints
                  elif actualrecoverypoints < 0:
                        cdo -= actualrecoverypoints
                        mbs -= actualrecoverypoints
                        residential -= actualrecoverypoints
                  if percentagesizeoftranche == 1:
                        print("PERCENTAGE SIZE CORRECT, RESUMING WITH FOLLOWING")
                        print("CDO =", cdo)
                        print("MBS =", mbs)
                        print("Residential =", residential)
                        print("Junkbonds =", junkbond)
            #proportion of tranche:
            print("MBS makes up  = ", mbs, "Proportion of tranche")

