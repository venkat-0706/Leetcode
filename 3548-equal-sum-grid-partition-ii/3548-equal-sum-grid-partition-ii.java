class Solution {
    int m;
    int n;
    public boolean canPartitionGrid(int[][] grid) {
        long totalSum = 0;
        m = grid.length;
        n = grid[0].length;
        
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                totalSum += grid[i][j];
            }
        }
        long sum = 0;
        HashSet<Long> potentialHalfValue = new HashSet<>();
        HashMap<Long, List<int[]>> map = new HashMap<>();
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                long val = grid[i][j];
                sum += val;
                if (!map.containsKey(val)) {
                    map.put(val, new ArrayList<>());
                    if ((totalSum+val)%2 == 0)
                        potentialHalfValue.add((totalSum+val)/2);
                }
                map.get(val).add(new int[]{i,j}); 
            }
            if (sum*2 == totalSum) return true;//no-removing Case
            if (potentialHalfValue.contains(sum)){ //remove one cell
                long removingValue = sum*2-totalSum;
                if(connectCheck(map.get(removingValue), i, -1)) return true;
            }
        }
        sum = 0;
        map.clear();
        potentialHalfValue.clear();
        for (int i = m-1; i >= 0; i--){
            for (int j = 0; j < n; j++){
                long val = grid[i][j];
                sum += val;
                if (!map.containsKey(val)) {
                    map.put(val, new ArrayList<>());
                    if ((totalSum+val)%2 == 0)
                        potentialHalfValue.add((totalSum+val)/2);
                }
                map.get(val).add(new int[]{i,j}); 
            }
            if (sum*2 == totalSum) return true;//no-removing Case
            if (potentialHalfValue.contains(sum)){ //remove one cell
                long removingValue = sum*2-totalSum;
                if(connectCheck(map.get(removingValue), i, -1)) return true;
            }
        }
        sum = 0;
        map.clear();
        potentialHalfValue.clear();
        for (int j = 0; j < n; j++){
            for (int i = 0; i < m; i++){
                long val = grid[i][j];
                sum += val;
                if (!map.containsKey(val)) {
                    map.put(val, new ArrayList<>());
                    if ((totalSum+val)%2 == 0)
                        potentialHalfValue.add((totalSum+val)/2);
                }
                map.get(val).add(new int[]{i,j}); 
            }
            if (sum*2 == totalSum) return true;//no-removing Case
            if (potentialHalfValue.contains(sum)){ //remove one cell
                long removingValue = sum*2-totalSum;
                if(connectCheck(map.get(removingValue), -1, j)) return true;
            }
        }
        sum = 0;
        map.clear();
        potentialHalfValue.clear();
        for (int j = n-1; j >= 0; j--){
            for (int i = 0; i < m; i++){
                long val = grid[i][j];
                sum += val;
                if (!map.containsKey(val)) {
                    map.put(val, new ArrayList<>());
                    if ((totalSum+val)%2 == 0)
                        potentialHalfValue.add((totalSum+val)/2);
                }
                map.get(val).add(new int[]{i,j}); 
            }
            if (sum*2 == totalSum) return true;//no-removing Case
            if (potentialHalfValue.contains(sum)){ //remove one cell
                long removingValue = sum*2-totalSum;
                if(connectCheck(map.get(removingValue), -1, j)) return true;
            }
        }
        return false;
    }
    private boolean connectCheck(List<int[]> positions, int row, int col){
        for (int[] posi : positions){
            boolean valid = true;
            if (row == 0 || row == m-1){ //one part is single row, we can only remove from two end
                if (posi[1]!=0 && posi[1]!=n-1) valid = false;
            }else if (col == 0 || col == n-1){ //one part is single column, we can only remove from two end
                if (posi[0]!=0 && posi[0]!=m-1) valid = false;
            }
            if (row > 0 && n == 1){ //for single column matrix, only three cell are safe to remove
                if (posi[0] != 0 && posi[0] != m-1 && posi[0] != row ) valid = false;
            }else if (col > 0 && m == 1){ //for single row matrix, only three cell are safe to remove
                if (posi[1] != 0 && posi[1] != n-1 && posi[1] != col) valid = false;
            }
            if (valid) return true;
        }
        return false;
    }
}