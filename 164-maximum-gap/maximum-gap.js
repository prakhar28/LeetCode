/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumGap = function(nums) {
    if (nums.length < 2) return 0;

    // Step 1: Find the minimum and maximum elements
    let minVal = Math.min(...nums);
    let maxVal = Math.max(...nums);

    if (minVal === maxVal) return 0;  // If all elements are the same, no gap

    // Step 2: Calculate bucket size and count
    let n = nums.length;
    let bucketSize = Math.max(1, Math.floor((maxVal - minVal) / (n - 1)));
    let bucketCount = Math.floor((maxVal - minVal) / bucketSize) + 1;

    // Step 3: Initialize buckets
    let buckets = new Array(bucketCount).fill(null).map(() => [null, null]);

    // Step 4: Place each number in the appropriate bucket
    nums.forEach(num => {
        let idx = Math.floor((num - minVal) / bucketSize);
        let [bucketMin, bucketMax] = buckets[idx];
        
        if (bucketMin === null || num < bucketMin) buckets[idx][0] = num;
        if (bucketMax === null || num > bucketMax) buckets[idx][1] = num;
    });

    // Step 5: Calculate the maximum gap
    let maxGap = 0;
    let prevMax = minVal;

    for (let [bucketMin, bucketMax] of buckets) {
        if (bucketMin === null) continue;  // Skip empty buckets
        // Gap between current bucket's min and previous bucket's max
        maxGap = Math.max(maxGap, bucketMin - prevMax);
        prevMax = bucketMax;  // Update previous max to current bucket's max
    }

    return maxGap;
};