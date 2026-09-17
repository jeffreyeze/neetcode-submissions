class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPriceSoFar = prices[0];
        int maxProfit = 0;
        for(int i = 1; i < prices.size(); i++){
            if(prices[i] < minPriceSoFar){
                minPriceSoFar = prices[i];
            }
            int currentProfit = prices[i] - minPriceSoFar;
            if(currentProfit > maxProfit){
                maxProfit = currentProfit;
            }

        }
        return maxProfit;
        
    }
};
