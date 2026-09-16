class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int maxWater = 0;
        //pointer!
        while(left < right){
            int currentWater = (right - left) * min(height[left], height[right]);
            if(currentWater > maxWater){
                maxWater = currentWater;
            }
            if(height[left] < height[right]){
                left++;
            }
            else{
                right--;
            }
        }
        return maxWater;
    }
};

