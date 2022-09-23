

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    Solution() {

    }
    int jump(const vector<int>& nums) {
        int currentLevel = 0, N = nums.size();
        if (N == 1) return 0;
        for (int i = 0; i < N-1; i++) {
            if (i + nums[i] >= N - 1) { currentLevel++; break; }
            if (nums[i] == 0) continue;
            int step = i + 1, maxVal = 0, maxJ = i + 1;
            while (step < N && step <= i + nums[i]) {
                if (step + nums[step] > maxVal) {
                    maxVal = step + nums[step];
                    maxJ = step;
                }
                step ++;
            }
            i = maxJ - 1;
            currentLevel += 1;
        }
        return currentLevel;
    }
};
//1 1 1 1
//level : 0

int main()
{
    Solution s = Solution();
    cout  << s.jump( {2, 3, 1, 1, 4 } );
}