pricingPlan = retrievePricingPlan()
order = retreiveOrder()
baseCharge = pricingPlan.base
charge = None
chargePerUnit = pricingPlan.charge
units = order.units
discount = None
charge = baseCharge + units * chargePerUnit
discountableUnits = max(units - pricingPlan.discountThreshold, 0)
discount = discountableUnits * pricingPlan.discountFactor
if order.isRepeat:
    discount += 20
charge = charge - discount
chargeOrder(charge)
