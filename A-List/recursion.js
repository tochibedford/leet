function recursionSum( yourArray, total=0){
    if(yourArray.length == 1){ //base case
        return yourArray[0]
    }else{ // recursive case
        total = yourArray[0] + recursionSum(yourArray.slice(1,), total) 
    }
    return total
}


x = [2,3,4,5,6,7]
console.log(recursionSum(x))
/**
 * 2 + [3,4,5,6,7]
 * 
 * 3 + [4,5,6,7]
 * 
 * 4 + [5,6,7]
 * 
 * 5 + [6,7]
 * 
 * 6 + [7]
 * 
 * 7
 *  .
 *  .
 *  .
 *[6,7]
 * 6 + [7]
 * 
 */