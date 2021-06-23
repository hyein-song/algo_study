class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<string> s;

        for(int row = 0; row < 9; row++) {
            for(int col = 0; col < 9; col++) {
                if(board[row][col] == '.') continue;
                string rowVal = "row" + to_string(row) + board[row][col];
                string colVal = "col" + to_string(col) + board[row][col];
                string cellVal = "cell" + to_string(row / 3 * 3 + col / 3) + board[row][col];
                if(s.count(rowVal) || s.count(colVal) || s.count(cellVal)) {
                    return false;
                }
                s.insert(rowVal);
                s.insert(colVal);
                s.insert(cellVal);
            }
        }
        return true;
    }
};
