const reading = {
    customer: "ivan",
    quantity: "10",
    month: 5,
    year: 2017
}


export default function acquireReading(){
    return reading;
}

export function baseRate(month, year){
    return month * year * 12;
}



