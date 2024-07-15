/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    const trimmed = s.trim()
    const arr = trimmed.split(" ")
    return arr.pop().length
};