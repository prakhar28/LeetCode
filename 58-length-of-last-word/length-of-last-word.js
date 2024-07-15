/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    const trimmed = s.trim()
    const arr = trimmed.split(" ")
    const lastWord = arr.pop()
    return lastWord.length
};