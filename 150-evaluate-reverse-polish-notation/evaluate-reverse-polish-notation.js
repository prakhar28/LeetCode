/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    const stack = [];
    
    // Operator map for evaluation
    const operators = {
        "+": (a, b) => a + b,
        "-": (a, b) => a - b,
        "*": (a, b) => a * b,
        "/": (a, b) => a / b >= 0 ? Math.floor(a / b) : Math.ceil(a / b)
    };

    for (const token of tokens) {
        // Check if the token is an operator
        if (operators[token]) {
            const secondVal = stack.pop();
            const firstVal = stack.pop();
            const result = operators[token](firstVal, secondVal);
            stack.push(result); // Push the result back onto the stack
        } else {
            // Token is a number, push it onto the stack
            stack.push(parseInt(token, 10)); // Convert string to integer
        }
    }
    
    return stack.pop();

};