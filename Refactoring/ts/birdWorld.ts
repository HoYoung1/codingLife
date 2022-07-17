interface IBird {
    name: string
    type: string
    numberOfCoconuts: number
    voltage: number
    isNailed: boolean
}

export function plumages(birds: IBird[]) {
    return new Map(birds.map(b => [b.name, plumage(b)]))
}


export function speeds(birds: IBird[]) {
    return new Map(birds.map(b => [b.name, airSpeedVelocity(b)]))
}

function plumage(bird: IBird): string { // 깃털 상태
    return createBird(bird).plumage    
}

function airSpeedVelocity(bird: IBird): number | null { // 비행속도
    return createBird(bird).airSpeedVelocity
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

function createBird(bird: IBird): Bird {
    switch (bird.type) {
        case '유럽 제비':
            return new EuropeanSwallow(bird);
        case '아프리카 제비':
            return new AfricanSwallow(bird);
        case '노르웨이 파랑 앵무':
            return new NorwegianBlueParrot(bird);
        default:
            return new Bird(bird);
    }
}