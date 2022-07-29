class HeatingPlan {
    get targetTemperature() {
        this.xxNewtargetTemparture(thermostat.selectedTemperature);
    }

    xxNewtargetTemparture(selectedTemperature) {
        if (selectedTemperature > this._max)
            return this._max;
        else if (selectedTemperature < this._min)
            return this._min;
        else
            return selectedTemperature;
    }
}

// client

if (thePlan.tergetTemperature > thermostat.currentTemperature)
    setToHeat();
else if (thePlan.targetTemperature < thermostat.currentTemperature)
    setToCool();
else 
    setOff();

