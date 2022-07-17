import { plumages, speeds } from './birdWorld'

const birdData = [
    {
        name: "새1",
        type: "유럽 제비",
        numberOfCoconuts: 0,
        voltage: 0,
        isNailed: false,
    },
    {
        name: "새2",
        type: "아프리카 제비",
        numberOfCoconuts: 3,
        voltage: 0,
        isNailed: false,
    },
    {
        name: "새3",
        type: "노르웨이 파랑 앵무",
        numberOfCoconuts: 0,
        voltage: 300,
        isNailed: true,
    },
]

test('plumage(깃털상태) 확인', () => {
    expect(plumages(birdData)).toEqual(
        new Map([
            ['새1', '보통이다'],
            ['새2', '지쳤다'],
            ['새3', '그을렸다'],
        ])
    );
})


test('speed(비행속도) 확인', () => {
    expect(speeds(birdData)).toEqual(
        new Map([
            ['새1', 35],
            ['새2', 34],
            ['새3', 0],
        ])
    );
})