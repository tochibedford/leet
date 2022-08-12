/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 var isAnagram = function(s, t) {
    const sObject = {}
    for(i in s){
        if(s[i] in sObject){
            sObject[s[i]] += 1
        }else{
            sObject[s[i]] = 1
        }
    }

    for(i in t){
        if(t[i] in sObject){
            sObject[t[i]] -= 1
            if(sObject[t[i]] == 0){
                delete sObject[t[i]]
            }
        }else{
            return false
        }
    }
    if(Object.keys(sObject).length){
        return false
    }else{
        return true
    }
};

console.log(isAnagram(s = "anagram", t = "nagaram"))
console.log(isAnagram(s = "rat", t = "car"))
console.log(isAnagram(s = "ab", t = "a"))