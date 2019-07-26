func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    let count = nums.count
    
    var hashTable = [Int: Int]()
    
    for i in 0..<count {
        let complement = target - nums[i]
        if let temp = hashTable[complement], temp != i {
            return [temp, i]
        }
        hashTable[nums[i]] = i
    }
    
    return []
}

twoSum([2, 7, 11, 15], 9)
