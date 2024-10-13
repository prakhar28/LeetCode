/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const myMap = new Map()
    for(let i = 0; i< nums.length; i++){
        let rem = target - nums[i]
        if(myMap.has(rem)) return [myMap.get(rem), i]
        else {
            myMap.set(nums[i], i)
        }
    }
};