import { plumages, speeds } from './birdWorld'

const birdData = [
    {
        name: "EuropeanSwallow",
        type: "유럽 제비",
        numberOfCoconuts: 0,
        voltage: 0,
        isNailed: false,
    },
    {
        name: "AfricanSwallow",
        type: "아프리카 제비",
        numberOfCoconuts: 3,
        voltage: 0,
        isNailed: false,
    },
    {
        name: "NorwegianBlueParrot",
        type: "노르웨이 파랑 앵무",
        numberOfCoconuts: 0,
        voltage: 300,
        isNailed: true,
    },
]

test('plumage(깃털상태) 확인', () => {
    expect(plumages(birdData)).toEqual(
        new Map([
            ['EuropeanSwallow', '보통이다'],
            ['AfricanSwallow', '지쳤다'],
            ['NorwegianBlueParrot', '그을렸다'],
        ])
    );
})


test('speed(비행속도) 확인', () => {
    expect(speeds(birdData)).toEqual(
        new Map([
            ['EuropeanSwallow', 35],
            ['AfricanSwallow', 34],
            ['NorwegianBlueParrot', 0],
        ])
    );
})


var abnormalData = [
    {
        name: "비정상 데이터",
        type: "유우럽 제비",
        numberOfCoconuts: -1,
        voltage: -1,
        isNailed: false,
    }
]

test('plumage(깃털상태) 비정상데이터', () => {
    expect(plumages(abnormalData)).toEqual(
        new Map([
            ['비정상 데이터', '알 수 없다'],
        ])
    );
})


test('speed(비행속도) 비정상데이터', () => {
    expect(speeds(abnormalData)).toEqual(
        new Map([
            ['비정상 데이터', null],
        ])
    );
})


