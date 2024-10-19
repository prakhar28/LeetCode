/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    const len = Math.floor(((nums.length)/2))
    nums.sort()
    console.log("nums", nums, len)
    return nums[len]
};