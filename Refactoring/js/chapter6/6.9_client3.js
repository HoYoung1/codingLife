import acquireReading from './6.9.js';
import Reading from './6.9_1.js';
import baseRate from './6.9.js';


// 클라이언트 3
const rawReading = acquireReading();
const aReading = new Reading(rawReading);
// const basicChargeAmount = calculateBaseCharge(aReading);
const basicChargeAmount = aReading.calculateBaseCharge();
console.log(basicChargeAmount);