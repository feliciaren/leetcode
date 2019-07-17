    // void gridDFS(vector<vector<char>>& grid, vector<vector<bool>>& visited,int i,int j){
    //     if(grid[i][j] == '1'&&!visited[i][j]){
    //         visited[i][j] = true;
    //         if(i>0&&grid[i-1][j]=='1') gridDFS(grid,visited,i-1,j);
    //         if(i<grid.size()-1&&grid[i+1][j]=='1') gridDFS(grid,visited,i+1,j);
    //         if(j>0&&grid[i][j-1]=='1') gridDFS(grid,visited,i,j-1);
    //         if(j<grid[i].size()-1&&grid[i][j+1]) gridDFS(grid,visited,i,j+1);
    //     }
    // }
    // int numIslands(vector<vector<char>>& grid) {
    //     if(grid.empty()||grid[0].empty()) return 0;
    //     int m = grid.size(),n = grid[0].size(),res = 0;
    //     vector<vector<bool>> visited(m,vector<bool>(n));
    //     for(int i = 0;i<m;++i){
    //         for(int j = 0;j<n;++j){
    //             if(grid[i][j]== '0' || visited[i][j]) continue;
    //             gridDFS(grid,visited,i,j);
    //             ++res;
    //         }
    //     }
    //     return res;
    // }
    int numIslands(vector<vector<char>>& grid) {
        if(grid.empty()||grid[0].empty()) return 0;
        int m = grid.size(),n = grid[0].size(),res = 0;
        vector<vector<bool>> visited(m,vector<bool>(n));
        vector<int> dirX{-1, 0, 1, 0}, dirY{0, 1, 0, -1};
        for(int i = 0;i<grid.size();++i){
            for(int j = 0;j<grid[0].size();++j){
                if(grid[i][j]=='0'||visited[i][j]) continue;
                ++res;
                queue<int> q{{i*n+j}};
                while (!q.empty()) {
                    int t = q.front(); q.pop();
                    for (int k = 0; k < 4; ++k) {
                        int x = t / n + dirX[k], y = t % n + dirY[k];
                        if (x < 0 || x >= m || y < 0 || y >= n || grid[x][y] == '0' || visited[x][y]) continue;
                        visited[x][y] = true;
                        q.push(x * n + y);
                    }
                }
            }
        }
        return res;
    }