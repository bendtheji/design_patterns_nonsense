#include <iostream>
//using namespace std;

class Box{
	public:
		double length;
		double width;
		double height;
		double getVolume(void);
};

double Box::getVolume(void){
	return length*width*height;
}

int main(void){
	Box box1;

	box1.length = 10.0;
	box1.width = 3.0;
	box1.height = 5.0;

	std::cout << box1.getVolume() << std::endl;

	return 0;
}