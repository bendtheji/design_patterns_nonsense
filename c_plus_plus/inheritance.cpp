#include <iostream>

using namespace std;

class Shape {
	public:
		void setWidth(int w) {
			width = w;
		}

		void setHeight(int h) {
			height = h;
		}

	protected:
		int width;
		int height;	
};

class PaintCost {
	public:
		int getCost(int area){
			return area * 90;
		}
};

class Rectangle: public Shape, public PaintCost
{
public:
	int getArea(){
		return width*height;
	}
	
};

int main(void){
	Rectangle Rect;

	Rect.setWidth(5);
	Rect.setHeight(7);

	cout << "Total cost: " << Rect.getCost(Rect.getArea()) << endl;

	return 0;
}