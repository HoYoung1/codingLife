function alertForMiscreant(people) {
    for (const p of people) {
        if (p === "조커") {
            setOffAlarms();
            return "조커";
        }
        if (p === "사루만") {
            setOffAlarms();
            return "사루만";
        }
    }
}

miscreant = ["조커", "사루만"]

function findMiscreant(people) {
    people.forEach(p => {
        if(miscreant.contains(p)){
            setOffA1larms();
            return p
        }
    });    
}