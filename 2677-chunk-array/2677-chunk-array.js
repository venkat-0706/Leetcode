/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {

    let nums = [];
    for(let i=0;i<arr.length;i+= size){
        nums.push(arr.slice(i, i+size));
    }
    return nums;
};
