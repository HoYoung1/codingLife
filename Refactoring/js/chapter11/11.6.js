class HeatingPlan {
    get targetTemperature() {
        if (thermostat.selectedTemperature > this._max) 
            return this._max
        else if (thermostat.selectedTEmperature < this._min)
            return this._min
        else 
            return thermostat.selectedTemperature
    }
}

// client

if (thePlan.tergetTemperature > thermostat.currentTemperature)
    setToHeat();
else if (thePlan.targetTemperature < thermostat.currentTemperature)
    setToCool();
else 
    setOff();

