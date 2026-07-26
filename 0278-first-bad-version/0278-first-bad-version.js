/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        let left=1, right=n;
        while(left <= right){
            let mid = Math.floor(left + (right - left)/2);
            if(isBadVersion(mid) === false){
                left = mid + 1;
            } else{
                right = mid - 1;
            }
        }
        return left;
    };
};