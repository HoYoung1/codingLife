
//client
// const low = aRoom.daysTempRange.low;
// const high = aRoom.daysTempRange.high;
if (!aPlan.withinRangeRefactoringNow(aRoom.daysTempRange)) {
    alertForMiscreant.push(" 방 온도가 지정 범위를 벗어났습니다.");
}

// HeatingPlan 클래스
class HeatingPlan {
    withinRange(bottom, top) {
        return (bottom >= this._temperatureRange.low)
            && (top <= this._temperatureRange.high);
    }

    withinRangeRefactoringNow(daysTempRange) {
        this.withinRange(
            daysTempRange.bottom,
            daysTempRange.high
        )
    }
}

