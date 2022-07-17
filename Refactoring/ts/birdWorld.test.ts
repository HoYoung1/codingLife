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