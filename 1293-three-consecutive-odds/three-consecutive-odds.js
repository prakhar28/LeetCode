/**
 * @param {number[]} arr
 * @return {boolean}
 */
var threeConsecutiveOdds = function(arr) {
    for (let i = 0; i < arr.length - 2; i++) {
        let j = i + 1
        let k = i + 2
        if(checkOdd(arr[i]) && checkOdd(arr[j]) && checkOdd(arr[k])) {
            return true
        }
    }
    return false
};

var checkOdd = function(num) {
    return (num % 2 !== 0)
} 