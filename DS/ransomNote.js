// JS because why not

/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    const magazineObject = {}
    for(i in magazine){
        if(magazine[i] in magazineObject){
            magazineObject[magazine[i]] += 1
        }else{
            magazineObject[magazine[i]] = 1
        }
    }

    for(i in ransomNote){
        if(ransomNote[i] in magazineObject){
            magazineObject[ransomNote[i]] -= 1
            if(magazineObject[ransomNote[i]] == 0){
                delete magazineObject[ransomNote[i]]
            }
        }else{
            return false
        }
    }
    return true

};

console.log(canConstruct(ransomNote = "a", magazine = "b"))
console.log(canConstruct(ransomNote = "aa", magazine = "ab"))
console.log(canConstruct(ransomNote = "aa", magazine = "aab"))