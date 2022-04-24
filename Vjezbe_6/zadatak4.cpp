#include <iostream>

float jednadzba(float a1,float b1, float c1,float a2,float b2, float c2)
{
    float x; 
    x = (b1*c2-b2*c1)/(b1*a2-a1*b2);

    float y;
    y = (c1-a1*x)/b1;

   std::cout << "x:" << x << "y:" << y << std::endl;
    
}

int main()
{
    jednadzba(4,3,7,2,-1,8);
     return 0;
}