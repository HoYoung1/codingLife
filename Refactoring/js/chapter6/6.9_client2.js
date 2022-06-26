import acquireReading from './6.9.js'


// 클라이언트 2
const aReading = acquireReading();
const base = (baseRate(aReading.month, aReading.year) * aReading.quantity);



