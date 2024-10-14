/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const map = new Map();
    for(const num of nums) {
        map.set(num, (map.get(num) || 0) + 1);
    }

    const sortedArr = [...map.keys()].sort((a,b) => map.get(b) - map.get(a))

    return sortedArr.slice(0, k)



};