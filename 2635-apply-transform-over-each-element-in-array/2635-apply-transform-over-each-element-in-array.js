/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const transformedArr = [];
    arr.forEach((ele, index)=>{
        transformedArr[index] = fn(ele , index);
    });
    return transformedArr;
};