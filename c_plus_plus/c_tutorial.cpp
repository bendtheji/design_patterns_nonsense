#include <iostream>
#include <cstring>
using namespace std;

int main(){
	char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};

	cout << strchr(greeting, '\0') << endl;

	return 0;
}