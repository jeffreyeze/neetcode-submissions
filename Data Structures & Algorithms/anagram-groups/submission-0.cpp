class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        vector<vector<string>> result;
        for(int i = 0; i < strs.size(); i++){
            string key = strs[i];
            sort(key.begin(), key.end());
            groups[key].push_back(strs[i]);
        }
        for (auto& pair : groups) {
            result.push_back(pair.second);
        }
        return result;
    }
};
