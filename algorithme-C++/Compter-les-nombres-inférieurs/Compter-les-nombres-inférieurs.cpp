#include <vector>

using namespace std;

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> smallnumber = {};
        int n = nums.size();
        for (int i = 0 ; i < n ; i++) {
            int result = 0;
            for (int x = 0 ; x < n ; x++) {
                if (nums[i] > nums[x]) {
                    result++;
                }
            }
            smallnumber.push_back(result);
        } 
        return smallnumber;
    }
};