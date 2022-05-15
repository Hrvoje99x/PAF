
#include <iostream>
#include <cmath>


class HarmonicOscillator{

    public:

            float k;
            float m;
            float x;
            float v;
            float a = -k*x/m;
            float t = 0;
        
            
               
            HarmonicOscillator(float k_, float m_, float x_, float v_){

                k = k_;
                m = m_;
                x = x_;
                v = v_;
            }

            int oscillate(float dt, float t_){
                
                float N_ = t_/dt;
                float round(float N_);
                
                for (int i =0; i<N_; i++){

                a = -k*x/m;
                v = v + a*dt;
                x = x + v*dt;
                t = t + dt;
                std::cout << x << std::endl;

                }
            }
};

int main(){

    HarmonicOscillator ho1(10, 2, 0.5, 0);
    ho1.oscillate(0.01, 5);
    return 0;
}