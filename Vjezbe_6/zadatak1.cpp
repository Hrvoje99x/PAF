#include <iostream>

void pravac(float x1,float y1, float x2, float y2)
{
    float k;
    k = (y2-y1)/(x2-x1);
    std::cout << "jednadzba pravca: y-" << y1 << "="<< k <<"(x-"<<x1<<")" << std::endl;
}

int main(){
    pravac(3,2,7,4);
}