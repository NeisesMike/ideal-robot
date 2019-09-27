function peel(pow, num) {
    var value = Math.pow(20, pow);
    for (var i = 0; i < 20; i++) {
        if ((num - value * i) < 0) {
            return (i - 1);
        }
    }
    return (0);
}
function convert(num10) {
    var temp;
    temp = num10;
    var highestPower;
    var numerals = [];
    if (num10 < 20) {
        numerals[0] = num10;
        console.log(numerals);
        return numerals;
    }
    highestPower = 0;
    while (temp >= 20) {
        highestPower++;
        temp = num10 - Math.pow(20, highestPower);
    }
    highestPower--;
    var tempExp;
    tempExp = highestPower;
    for (var i = 0; i < highestPower; i++) {
        var value = peel(tempExp, num10);
        numerals[i] = value;
        num10 = num10 - value * (Math.pow(20, tempExp));
        tempExp--;
    }
    numerals[highestPower] = num10;
    console.log(numerals);
    return numerals;
}
convert(1234);
