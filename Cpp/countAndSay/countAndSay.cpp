#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
	string countAndSay(int n) {
		string precedent_str, ans_str;
		int i = 0, j = 0, count = 0;
		if (n == 1) {
			return "1";
		}
		precedent_str = countAndSay(n - 1);
		while (precedent_str[i] != '\0')
		{
			count = 1;
			while (precedent_str[i] == precedent_str[i + 1]) {
				count++;
				i++;
			}
			ans_str.append(to_string(count));
			ans_str.append(precedent_str, i, 1);
			i++;
		}

		return ans_str;
	}
};

int main() {
	int n;
	Solution s;
	cin >> n;
	cout << "your input number is:" << n << '\n';
	cout << s.countAndSay(n);

	return 0;
}