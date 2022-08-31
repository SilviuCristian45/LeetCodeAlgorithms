function myAtoi(s: string): number {
    let ans = 0
    let copyS = s.trim()
    let hasSign
    const INT_MAX = 2**31
    const INT_MIN = (-2)**31

    if (copyS[0] == "+" || copyS[0] == "-") {
        hasSign = copyS[0]
        copyS = copyS.substring(1)
    }
    for (let char of copyS) {
        if (char.charCodeAt(0) < 48 || char.charCodeAt(0) > 57) {
            break
        }
        let currentCharCode = char.charCodeAt(0)
        let number = currentCharCode - "0".charCodeAt(0)
        ans = ans * 10 + number
    }
    ans = (hasSign == "-") ? ans * -1 : ans
    if (ans < INT_MIN) {
        ans = INT_MIN
    }
    if (ans >= INT_MAX) {
        ans = INT_MAX-1
    }
    return ans
}

console.log(myAtoi("42"))
console.log(myAtoi("    425"))
console.log(myAtoi("-345"))
console.log(myAtoi("   -42"))
console.log(myAtoi("   -42123withToys"))