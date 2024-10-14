/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    let stack = [];
    let ht = {
        "+" : (a,b)=> a + b,
        "-" : (a,b)=> a-b,
        "*" : (a,b)=> a*b,
        '/': (a, b) => a / b >= 0 ? Math.floor(a / b) : Math.ceil(a / b),
     }

     for(let i=0;i<tokens.length;i++){
        if(ht[tokens[i]]){
            let firstVal = stack.pop()
            let secondVal = stack.pop()
            stack.push(ht[tokens[i]](secondVal,firstVal))
        }else{
            stack.push(Number(tokens[i]))
        }
     }

     return stack.pop()

};