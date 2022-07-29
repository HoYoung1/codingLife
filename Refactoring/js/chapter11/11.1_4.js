function alertForMiscreant(people) {
    // for (const p of people) {
    //     if (p === "조커") {
    //         setOffAlarms();
    //         return
    //     }
    //     if (p === "사루만") {
    //         setOffAlarms();
    //         return
    //     }
    // }
    // return
    if (findMiscreant(people) != ""){
        setOffAlarms();
    }
}


function findMiscreant(people) {
    for (const p of people) {
        if (p === "조커") {
            return "조커";
        }
        if (p === "사루만") {
            return "사루만";
        }
    }
    return "";
}


const people = ["조커", "사루만"]
// found = alertForMiscreant(people)
found = findMiscreant(people)
alertForMiscreant(people)
console.log(found)
