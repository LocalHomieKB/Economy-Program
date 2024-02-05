# -*- coding: utf-8 -*-
"""
Created on Sun May 14 18:12:16 2023

@author: local_u1od3t5
"""

class CollateralPool:
    def __init__(self, NumberOfReferenceEntities, ParValueOfEachBond, WeightedAverageCoupon,
                 WeightedAverageLifeInYears, RecoveryRate, CouponFrequency, NumberOfOverlappingEntities)
    self.NumberOfReferenceEntities = RefEntities
    self.ParValueOfEachBond = ParValuePerBond
    self.WeightedAverageCoupon = WeightedAverageCoupon
    self.WeightedAverageLifeInYears = WeightedAverageLife
    self.RecoveryRate = RecoveryRate
    self.CouponFrequency = CouponFrequency # For semiannual = 1, annual =2 e.t.c
    self.NumberOfOverlappingEntities = RefOverlapping
    
InnerCDO01 = CollateralPool(100, 1, 0.08, 10, 0.4, 1, 0)
InnerCDO02 = CollateralPool(100,1,0.08,10,0.4,,1,-)
    
