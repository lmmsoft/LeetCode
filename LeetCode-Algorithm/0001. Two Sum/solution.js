/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    var hash = {};
    var res = [];
    for (var i = 0; i < nums.length; ++i) {
        n = nums[i];
        if (hash[target - n] === undefined) {
            hash[n] = i;
        } else {
            res.push(hash[target - n]);
            res.push(i);
            return res;
        }
    }
};


const twoSum2 = (arr, target) => {
    let map = {}, results = [];
    for (let i = 0; i < arr.length; i++) {
        if (map[arr[i]] !== undefined) {
            results.push(map[arr[i]]);
            results.push(i);
            return results;
        } else {
            map[target - arr[i]] = i;
        }
    }
};