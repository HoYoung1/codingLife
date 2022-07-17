interface IBird {
    name: string
    type: string
    numberOfCoconuts: number
    voltage: number
    isNailed: boolean
}

export function plumages(birds: IBird[]) {
    // return new Map(birds.map(b => [b.name, plumage(b)]))
    return new Map(birds.map(b => [b.name, createBird(b).plumage]))
}


export function speeds(birds: IBird[]) {
    // return new Map(birds.map(b => [b.name, airSpeedVelocity(b)]))
    return new Map(birds.map(b => [b.name, createBird(b).airSpeedVelocity]))
}


class Bird {
    bird: IBird;

    constructor(bird: IBird) {
        this.bird = bird;
    }

    get plumage(): string { // 깃털 상태
        switch (this.bird.type) {
            case '유럽 제비':
                return '보통이다';
            case '아프리카 제비':
                return (this.bird.numberOfCoconuts > 2) ? "지쳤다" : "보통이다";
            case '노르웨이 파랑 앵무':
                return (this.bird.voltage > 100) ? "그을렸다" : "예쁘다";
            default:
                return "알 수 없다";
        }
    }

    get airSpeedVelocity(): number | null { // 비행속도
        switch (this.bird.type) {
            case '유럽 제비':
                return 35;
            case '아프리카 제비':
                return 40 - 2 * this.bird.numberOfCoconuts;
            case '노르웨이 파랑 앵무':
                return (this.bird.isNailed) ? 0 : 10 + this.bird.voltage / 10;
            default:
                return null;
        }
    }
}


class EuropeanSwallow extends Bird { 
    get plumage(): string { // 깃털 상태
        switch (this.bird.type) {
            case '유럽 제비':
                return '보통이다';
            case '아프리카 제비':
                return (this.bird.numberOfCoconuts > 2) ? "지쳤다" : "보통이다";
            case '노르웨이 파랑 앵무':
                return (this.bird.voltage > 100) ? "그을렸다" : "예쁘다";
            default:
                return "알 수 없다";
        }
    }

    get airSpeedVelocity(): number | null { // 비행속도
        switch (this.bird.type) {
            case '유럽 제비':
                return 35;
            case '아프리카 제비':
                return 40 - 2 * this.bird.numberOfCoconuts;
            case '노르웨이 파랑 앵무':
                return (this.bird.isNailed) ? 0 : 10 + this.bird.voltage / 10;
            default:
                return null;
        }
    }
}
class AfricanSwallow extends Bird {
    get plumage(): string { // 깃털 상태
        switch (this.bird.type) {
            case '유럽 제비':
                return '보통이다';
            case '아프리카 제비':
                return (this.bird.numberOfCoconuts > 2) ? "지쳤다" : "보통이다";
            case '노르웨이 파랑 앵무':
                return (this.bird.voltage > 100) ? "그을렸다" : "예쁘다";
            default:
                return "알 수 없다";
        }
    }

    get airSpeedVelocity(): number | null { // 비행속도
        switch (this.bird.type) {
            case '유럽 제비':
                return 35;
            case '아프리카 제비':
                return 40 - 2 * this.bird.numberOfCoconuts;
            case '노르웨이 파랑 앵무':
                return (this.bird.isNailed) ? 0 : 10 + this.bird.voltage / 10;
            default:
                return null;
        }
    }
 }
class NorwegianBlueParrot extends Bird {
    get plumage(): string { // 깃털 상태
        switch (this.bird.type) {
            case '유럽 제비':
                return '보통이다';
            case '아프리카 제비':
                return (this.bird.numberOfCoconuts > 2) ? "지쳤다" : "보통이다";
            case '노르웨이 파랑 앵무':
                return (this.bird.voltage > 100) ? "그을렸다" : "예쁘다";
            default:
                return "알 수 없다";
        }
    }

    get airSpeedVelocity(): number | null { // 비행속도
        switch (this.bird.type) {
            case '유럽 제비':
                return 35;
            case '아프리카 제비':
                return 40 - 2 * this.bird.numberOfCoconuts;
            case '노르웨이 파랑 앵무':
                return (this.bird.isNailed) ? 0 : 10 + this.bird.voltage / 10;
            default:
                return null;
        }
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
