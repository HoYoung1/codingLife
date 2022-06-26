const reading = {
    customer: "ivan",
    quantity: "10",
    month: 5,
    year: 2017
}

export class Reading {
    constructor(data){
        this._customer = data.customer
        this._quantity = data.quantity
        this._month = data.month
        this._year = data.year
    }

    get customer() {return this._customer};
    get quantity() {return this._quantity};
    get month() {return this._month};
    get year() {return this._year};

    // 기본 요금 계산 함수
    get calculateBaseCharge(){
        return baseRate(this.month, this.year) * this.quantity;
    }
    

}

export default function acquireReading(){
    return reading;
}



