/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let prevTotal = 0;
    let maxAvg = 0;
    
    // Calculate the total of the first 'k' elements
    for (let i = 0; i < k; i++) {
        prevTotal += nums[i];
    }
    
    // Set the initial max average based on the first 'k' elements
    maxAvg = prevTotal / k;
    
    // Iterate through the rest of the array
    for (let i = 1; i <= nums.length - k; i++) {
        let currTotal = prevTotal - nums[i - 1] + nums[i + k - 1]; // Sliding window logic
        let currAvg = currTotal / k;

        // Update maxAvg if we find a higher average
        if (currAvg > maxAvg) {
            maxAvg = currAvg;
        }
        
        // Update prevTotal for the next iteration
        prevTotal = currTotal;
    }

    return maxAvg;

};