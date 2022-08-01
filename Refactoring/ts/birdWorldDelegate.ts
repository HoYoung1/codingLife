interface IBird {
    name: string
    type: string
    numberOfCoconuts: number
    voltage: number
    isNailed: boolean
    plumage: string
}

export function plumages(birds: IBird[]) {
    return new Map(birds.map(b => [b.name, plumage(b)]))
}


export function speeds(birds: IBird[]) {
    return new Map(birds.map(b => [b.name, airSpeedVelocity(b)]))
}

function createBird(data: IBird): Bird {
    return new Bird(data);
}

function plumage(bird: IBird): string { // 깃털 상태
    return createBird(bird).plumage    
}

function airSpeedVelocity(bird: IBird): number | null { // 비행속도
    return createBird(bird).airSpeedVelocity
}

export class WildDelegate {}

export class Bird {
    private _name: string;
    private _plumage: string;
    private _speciesDelegate: SpeciesDelegate;

    constructor(data: IBird) {
        this._name = data.name;
        this._plumage = data.plumage;
        this._speciesDelegate = this.selectSpeciesDelegate(data);
    }

    get name(): string { return this._name; }
    get plumage(): string { return this._speciesDelegate.plumage; }
    get airSpeedVelocity(): number { return this._speciesDelegate.airSpeedVelocity; }

    selectSpeciesDelegate(data: IBird) {
        switch (data.type) {
            case '유럽 제비':
                return new EuropeanSwallowDelegate(data, this);
            case '아프리카 제비':
                return new AfricanSwallowDelegate(data, this);
            case '노르웨이 파랑 앵무':
                return new NorwegianBlueParrotDelegate(data, this);
            default:
                return new SpeciesDelegate(data, this);
        }
    }
}

export class SpeciesDelegate {
    protected _bird: Bird; 
    
    constructor(data: IBird, bird: Bird) {
        this._bird = bird;
    }

    get plumage(): string {
        return this._bird.plumage || "보통이다";
    }

    get airSpeedVelocity(): number {
        throw new Error("Should be called in subclass");
    }
}

export class EuropeanSwallowDelegate extends SpeciesDelegate { 
    constructor(data: IBird, bird: Bird) {
        super(data, bird);
    }

    get airSpeedVelocity(): number {
        return 35;
    }
}

export class AfricanSwallowDelegate extends SpeciesDelegate {
    private _numberOfCoconuts: number; 

    constructor(data: IBird, bird: Bird) {
        super(data, bird);
        this._numberOfCoconuts = data.numberOfCoconuts;
    }

    get airSpeedVelocity(): number {
        return 40 - 2 * this._numberOfCoconuts;
    }
}

export class NorwegianBlueParrotDelegate extends SpeciesDelegate {
    private _voltage: number;
    private _isNailed: boolean;

    constructor(data: IBird, bird: Bird) {
        super(data, bird); 
        this._voltage = data.voltage; 
        this._isNailed = data.isNailed;
    }

    get airSpeedVelocity() {
        return (this._isNailed) ? 0 : 10 + this._voltage / 10;
    }

    get plumage() {
        if (this._voltage > 100) 
            return "그을렸다"; 
        else 
            return this._bird.plumage || "예쁘다";
    }
        
}