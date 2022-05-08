#include <iostream>
#include <math.h>

class Particle{
    public:

        float brzina;
        float kut;
        float x;
        float y;
        float pi = 3.14;
        float g = 9.81;
        float kut2; 
        float vx;
        float  vy;
        float t = 0;

        Particle(float v, float kut_, float x_, float y_){

        brzina = v;
        kut = kut_;
        x =  x_;
        y = y_;

        float kut2_;
        kut2_= kut_*pi/180;

        vx = v*cos(kut2_);
        vy = v*sin(kut2_);
        

       
        }

    private: 

        float __move(float dt){
            
           
            x = x + vx*dt;
            vy = vy - g*dt;
            y = y + vy*dt;
            t = t + dt;
            
            }
            
    public:  

        float range(float dt){
            
           
            
            do{
                __move(dt);
            }
            while (y>=0);
           
            

            std::cout << x << std::endl;
        }
        
        float time(float dt){
            
            do{
                __move(dt);
            }
            while (y>=0);
            
            std::cout << t << std::endl;
            
        }

        

};


int main(){

   Particle p1(10,45,0,0);
   p1.range(0.01);
   p1.time(0.01);

   Particle p2(30,60,0,0);
   p2.range(0.01);
   p2.time(0.01);
}