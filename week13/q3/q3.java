import java.util.*;
import java.io.*;
public class inclass_practice {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    public static void main(String[] args) throws IOException{
    	int T = readInt(), N = readInt();
    	Integer[] distances = new Integer[N + 1];
    	distances[0] = 0;
    	for (int n = 1; n < N + 1; n++) {
    		distances[n] = readInt();
    	}
    	Arrays.sort(distances, (x, y) -> {
    		return Integer.compare(Math.abs(x), Math.abs(y));
    	});
    	int count = 0;
    	for (int i = 1; i < distances.length; i++) {
    		T -= Math.abs(distances[i] - distances[i - 1]);
    		if (T >= 0) {
    			count++;
    		}
    		else {
    			break;
    		}
    		System.out.println(T);
    	}
    	System.out.println(count);
    }
    static class Distance {
    	public Distance (int d) {
    		this.d = d;
    	}
    	public int d;
    }
    static String next () throws IOException {
        while (st == null || ! st.hasMoreTokens())
            st = new StringTokenizer(br.readLine().trim());
        return st.nextToken();
    }
    static long readLong () throws IOException {
        return Long.parseLong(next());
    }
    static int readInt () throws IOException {
        return Integer.parseInt(next());
    }
    static double readDouble () throws IOException {
        return Double.parseDouble(next());
    }
    static char readCharacter () throws IOException {
        return next().charAt(0);
    }
    static String readLine () throws IOException {
        return br.readLine().trim();
    }
}
