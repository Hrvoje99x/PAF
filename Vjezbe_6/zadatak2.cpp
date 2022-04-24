#include <iostream>
#include <cmath>

void  udaljenost_tocke(float x1,float y1,float x2,float y2,float r)
{
    float x;

    x = pow((x1-x2),2) + pow((y1-y2),2);

    float d;

    d = sqrt(x);

    float epsilon = 0.01;

    if (d<r){
        std::cout << "Točka se nalazi unutar kružnice" << std::endl;
    }
    else if ( r-epsilon < d < r+epsilon){
        std::cout << "Točka se nalazi na kružnici" << std::endl;
    }
    else{
        std::cout << "Točka se nalazi izvan kružnice" << std::endl;
    }
}

int main(){
    udaljenost_tocke(3,2,7,4,5);
    return 0;
}