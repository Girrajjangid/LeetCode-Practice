class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x_diff = coordinates[1][0] - coordinates[0][0]
        y_diff = coordinates[1][1] - coordinates[0][1]
        length = len(coordinates)-1
        for i in range(length):
            if (coordinates[i+1][0] - coordinates[i][0])*y_diff != (coordinates[i+1][1] - coordinates[i][1])*x_diff:
                return False
        return True
                
            