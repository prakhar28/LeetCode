/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [];
    const pairs = { ')': '(', '}' : '{', ']' : '[' };

    for (let char of s) {
        if (char === '(' || char === '{' || char === '[') {
            stack.push(char);
        } else {
            // Check if stack is empty before popping
            if (stack.length === 0) {
                return false;
            }
            const top = stack.pop();
            if (top !== pairs[char]) {
                return false;
            }
        }
    }

    // Ensure the stack is empty for valid parentheses
    return stack.length === 0;
};