interface IBird {
    name: string
    type: string
    numberOfCoconuts: number
    voltage: number
    isNailed: boolean
}

class Bird {
    bird: IBird

    constructor(bird: IBird) {
        this.bird = bird
    }

    get plumage(): string { // 깃털 상태
        return "알 수 없다";
    }
    
    get airSpeedVelocity(): number | null { // 비행속도
        return null;
    }
}
class EuropeanSwallow extends Bird {
    get plumage(): string { // 깃털 상태
         return '보통이다';
    }
    
    get airSpeedVelocity(): number | null { // 비행속도
        return 35;
    }
}
class AfricanSwallow extends Bird {
    get plumage(): string { // 깃털 상태
       return (this.bird.numberOfCoconuts > 2) ? "지쳤다" : "보통이다";
    }
    
    get airSpeedVelocity(): number | null { // 비행속도
       return 40 - 2 * this.bird.numberOfCoconuts;
    }
}
class NorwegianBlueParrot extends Bird {
    get plumage(): string { // 깃털 상태
       return (this.bird.voltage > 100) ? "그을렸다": "예쁘다";
    }
    
    get airSpeedVelocity(): number | null { // 비행속도
        return (this.bird.isNailed) ? 0: 10 + this.bird.voltage / 10;
    }
}