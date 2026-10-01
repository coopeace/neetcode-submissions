class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n,1);
        int prefix = 1;
        int suffix = 1;
        int left = 0;
        int right = n - 1;
        while (left != n && right != -1){
            res[left] *= prefix;
            res[right] *= suffix;
            prefix *= nums[left];
            suffix *= nums[right];
            left += 1;
            right -=1;
        }
        return res;

    }
};
