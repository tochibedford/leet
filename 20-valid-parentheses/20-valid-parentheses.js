let Stack = function(){
    this.innerStack = []
    this.push = (val)=>{
        this.innerStack.push(val)
    }
    this.pop = ()=>{
        const popped = this.innerStack.splice(this.innerStack.length-1)
        return popped[0]
    }
    this.getLength = ()=>{
        return this.innerStack.length
    }
}

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const parenthStack = new Stack()
    const lookUpDict = {
        '}':'{',
        ')':'(',
        ']':'['
    }
    for(i in s){
        if(s[i] === '{' || s[i] === '[' || s[i] === '('){
            parenthStack.push(s[i])
        }else{
            let popped = parenthStack.pop();
            if(popped !== lookUpDict[s[i]]){
                return false
            }
        }
    }
    
    if(parenthStack.getLength() === 0){
        return true
    }
    return false
};

// learned I can just push the closing parentheses into the stack rather than looking it up from a map or dictionary all the time