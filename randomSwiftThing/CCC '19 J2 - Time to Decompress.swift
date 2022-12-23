/*var str = "Hello, playground"

let entry = readLine()!.split(separator: " ").map(String.init)
let num = Int(entry[0])
let sym = entry[1]
print(num!*2)

var num

for index in 1...5 {
    print("\(index) times 5 is \(index * 5)")
}*/

let num = readLine()
let n = Int(num!)
for i in stride(from:0, to: n!, by:1){
    let temp = readLine()!.split(separator: " ").map(String.init)
    let num = Int(temp[0])
    let sym = temp[1]
    let ans = String(repeating: sym, count: num!)
    print(ans)
}