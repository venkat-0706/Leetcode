var twoSum = function(nums, target) {
    // Map elements to objects containing value and original index
    let indexedNums = nums.map((num, index) => ({ value: num, index: index }));
    
    // Fix: Sort numerically using a comparator function
    indexedNums.sort((a, b) => a.value - b.value);
    
    let i = 0;
    let j = indexedNums.length - 1;
    
    while (i < j) { // Changed to i < j since elements cannot pair with themselves
        let sum = indexedNums[i].value + indexedNums[j].value;
        
        if (sum === target) {
            return [indexedNums[i].index, indexedNums[j].index]; // Return original indices
        } else if (sum < target) {
            i++;
        } else {
            j--;
        }
    }
};