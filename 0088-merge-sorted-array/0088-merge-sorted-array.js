/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {

    let i = 0;
    let j = 0;
    let k = 0;

    let new_arr = new Array(m + n);

    while(i < m && j < n){
        if(nums1[i] <= nums2[j]){
            new_arr[k] = nums1[i];
            i++;
        }else{
            new_arr[k] = nums2[j];
            j++;
        }
        k++;
    }

    while(i < m){
        new_arr[k] = nums1[i];
        i++;
        k++;
    }

    while(j < n){
        new_arr[k] = nums2[j];
        j++;
        k++;
    }

    for(let x = 0; x < m + n; x++){
        nums1[x] = new_arr[x];
    }
};