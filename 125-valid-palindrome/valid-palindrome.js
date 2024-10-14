/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const stringOnly = s.replace(/[^a-zA-Z0-9]/g,'').toLowerCase()

    let l = 0
    let r = stringOnly.length - 1

    while (l < r) {
        if (stringOnly[l] !== stringOnly[r]) return false
        else {
            l++ 
            r--
        }
    }
    return true
};