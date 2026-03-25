#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();
        vector<int> return_list = {};
        vector<int> seen(n, 0);

        for (int x = 0; x < n; x++) {
            int number = nums[x];
            seen[number - 1] = 1;
        }

        for (int i = 0; i < n; i++) {
            if (seen[i] == 0) {
                return_list.push_back(i + 1);
            }
        }

        return return_list;
    }
};