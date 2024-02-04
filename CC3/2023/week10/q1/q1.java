import java.util.*;
import java.io.*;

public class Ragaman {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		Reader sc = new Reader();

		String s1 = sc.readLine();
		String s2 = sc.readLine();

		HashMap<Character, Integer> m1 = new HashMap<>();
		HashMap<Character, Integer> m2 = new HashMap<>();

		for (int i = 0; i < s1.length(); i++) {
			m1.put(s1.charAt(i), m1.getOrDefault(s1.charAt(i), 0) + 1);
		}

		for (int i = 0; i < s2.length(); i++) {
			m2.put(s2.charAt(i), m2.getOrDefault(s2.charAt(i), 0) + 1);
		}

		if (s1.length() != s2.length()) {
			System.out.println("N");
		} else {

			boolean isGood = true;
			for (Map.Entry<Character, Integer> entry : m2.entrySet()) {
				char curr = entry.getKey();
				int freq = entry.getValue();
				
				int freq1 = 0;
				
				if(m1.get(curr) != null) {
					freq1 = m1.get(curr);
				}
				if(curr != '*') {
				if (freq1 < freq) {
					isGood = false;
					break;
				}
				}
			}

			if (isGood) {
				System.out.println("A");
			} else {
				System.out.println("N");
			}
		}

	}

	static class Reader {
		final private int BUFFER_SIZE = 1 << 16;
		private DataInputStream din;
		private byte[] buffer;
		private int bufferPointer, bytesRead;

		public Reader() {
			din = new DataInputStream(System.in);
			buffer = new byte[BUFFER_SIZE];
			bufferPointer = bytesRead = 0;
		}

		public Reader(String file_name) throws IOException {
			din = new DataInputStream(new FileInputStream(file_name));
			buffer = new byte[BUFFER_SIZE];
			bufferPointer = bytesRead = 0;
		}

		public String readLine() throws IOException {
			byte[] buf = new byte[1000];
			int cnt = 0, c;
			while ((c = read()) != -1) {
				if (c == '\n') {
					if (cnt != 0) {
						break;
					} else {
						continue;
					}
				}
				buf[cnt++] = (byte) c;
			}
			return new String(buf, 0, cnt);
		}

		public int readInt() throws IOException {
			int ret = 0;
			byte c = read();
			while (c <= ' ') {
				c = read();
			}
			boolean neg = (c == '-');
			if (neg)
				c = read();
			do {
				ret = ret * 10 + c - '0';
			} while ((c = read()) >= '0' && c <= '9');
			if (neg)
				return -ret;
			return ret;
		}

		public long readLong() throws IOException {
			long ret = 0;
			byte c = read();
			while (c <= ' ')
				c = read();
			boolean neg = (c == '-');
			if (neg)
				c = read();
			do {
				ret = ret * 10 + c - '0';
			} while ((c = read()) >= '0' && c <= '9');
			if (neg)
				return -ret;
			return ret;
		}

		public double readDouble() throws IOException {
			double ret = 0, div = 1;
			byte c = read();
			while (c <= ' ')
				c = read();
			boolean neg = (c == '-');
			if (neg)
				c = read();
			do {
				ret = ret * 10 + c - '0';
			} while ((c = read()) >= '0' && c <= '9');
			if (c == '.') {
				while ((c = read()) >= '0' && c <= '9') {
					ret += (c - '0') / (div *= 10);
				}
			}
			if (neg)
				return -ret;
			return ret;
		}

		private void fillBuffer() throws IOException {
			bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
			if (bytesRead == -1)
				buffer[0] = -1;
		}

		private byte read() throws IOException {
			if (bufferPointer == bytesRead)
				fillBuffer();
			return buffer[bufferPointer++];
		}

		public void close() throws IOException {
			if (din == null)
				return;
			din.close();
		}
	}

	static String next() throws IOException {
		while (st == null || !st.hasMoreTokens())
			st = new StringTokenizer(br.readLine().trim());
		return st.nextToken();
	}

	static char readCharacter() throws IOException {
		return next().charAt(0);
	}

}