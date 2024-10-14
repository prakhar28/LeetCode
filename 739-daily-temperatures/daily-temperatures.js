/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    const n = temperatures.length;
    const result = new Array(n).fill(0);
    const stack = []; // This will store the indices of the temperatures array

    for (let i = 0; i < n; i++) {
        // While the stack is not empty and the current temperature is greater than 
        // the temperature at the index stored at the top of the stack
        while (stack.length > 0 && temperatures[i] > temperatures[stack[stack.length - 1]]) {
            // Pop the index from the stack
            const index = stack.pop();
            // Calculate the number of days until a warmer temperature
            result[index] = i - index; // i is the current day
        }
        // Push the current index onto the stack
        stack.push(i);
    }

    return result;
};