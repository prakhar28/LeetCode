/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    const map = new Map()
    const len = nums.length
    for(let i of nums) {
        if(map.has(i)){
            map.set(i, map.get(i)+1)
            
        } else {
            map.set(i, 1)
        }
        if(map.get(i) > (len/2)) return i
    }
};