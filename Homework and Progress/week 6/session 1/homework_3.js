// Write a method in Javascript that rolls X dice, and discards the Y lowest rolls, then returns the sum of the rest.


var totalRolls = 3; //change x to number of rolls
var currentRoll = [];
var randomRoll;




function diceRoll(minSides, maxSides) {
    for (roll = 0; roll < totalRolls; roll++) {
        randomRoll = Math.floor(Math.random() * (maxSides - minSides) + minSides);
        currentRoll.push(randomRoll);
    }
    console.log(currentRoll);
    return currentRoll;
}





function compareRolls(x) {

    rollSorted = x.sort(function (a, b) { return b - a });
    removeLast = rollSorted.pop();
    sumArray = rollSorted.reduce(function(a, b){return a + b });
    console.log(rollSorted);
    console.log(removeLast);
    return sumArray;
}

diceRoll(1,7);

compareRolls(currentRoll);

