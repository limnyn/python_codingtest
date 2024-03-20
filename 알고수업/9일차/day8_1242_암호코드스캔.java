import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

//public class Solution {
public class day8_1242_암호코드스캔 {
	static int[][] map = new int [2000][2000];
	static int [][][] scode = new int [4][3][4];
    static int [] code = new int [9];
	static int x, y, z, codei, ans;
	
	public static void checkCode() {
        int t = (code[1] + code[3] + code[5] + code[7]) * 3 + code[2] + code[4] + code[6] + code[8];
        if (t % 10 == 0) ans += code[1] + code[2] + code[3] + code[4] + code[5] + code[6] + code[7] + code[8];
        codei = 8;
	}
	
	public static int countXYZ(int i, int j) {
        x = y = z = 0;
        while (map[i][j] == 1) { z++; j--; } // 1의 개수
        while (map[i][j] == 0) { y++; j--; } // 0의 개수
        while (map[i][j] == 1) { x++; j--; } // 1의 개수
        return j;
	}
	
	public static void reComputeXYZ() {
        int min = Math.min(Math.min(x, y), z);
        x /= min; y /= min; z /= min;
	}
	
	public static void main(String[] args) throws FileNotFoundException{
		
		System.setIn(new FileInputStream("day8_1242_input.txt"));
        Scanner sc = new Scanner(System.in);

        int TC;
        TC = sc.nextInt();
        
        scode[1][0][0] = 0;
        scode[1][1][0] = 1;
        scode[0][1][1] = 2;
        scode[3][0][0] = 3;
        scode[0][2][1] = 4;
        scode[1][2][0] = 5;
        scode[0][0][3] = 6;
        scode[2][0][1] = 7;
        scode[1][0][2] = 8;
        scode[0][0][1] = 9;

        for(int tc = 1; tc <= TC; tc++) {
            int N, M; // 1 <= N <= 2000, 1 <= M <= 500
            ans = 0;

            N = sc.nextInt();
            M = sc.nextInt();
            sc.nextLine();
            
            for (int i = 0; i < N; i++) 
            {
                String line = sc.nextLine();
                
                for (int j = 0; j < M; j++)
                {
                    int t = Character.getNumericValue(line.charAt(j));
                    
                    for (int k = 3; k > -1; k--)
                    	map[i][j * 4 + (3 - k)] = (t & (1 << k)) == 0 ? 0 : 1; 
                }
            }
            
            codei = 8;
            
            for (int i = 1; i < N - 5; i++)
                for (int j = M * 4 - 1; j > 7; j--)
                {
                    if (map[i][j] == 1 && map[i - 1][j] == 0)
                    {
                    	j = countXYZ(i, j);
                    	reComputeXYZ();

                        code[codei--] = scode[x - 1][y - 1][z - 1];

                        if (codei == 0)	checkCode();
                    }
                }

            System.out.printf("#%d %d\n", tc, ans);
        }
        sc.close();
    }
}
