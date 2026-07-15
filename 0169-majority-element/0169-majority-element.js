/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let n = nums.length; 
    let max_ele = nums[0];
    for(let i=1;i<n;i++){
        if(nums[i-1] < nums[i]){
            max_ele = nums[i];
            i++;
        }
    }
    return max_ele;
};