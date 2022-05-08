#include <iostream>
#include <math.h>
#include "particle.h"

Particle::Particle(float v, float kut_, float x_, float y_){
        brzina=v;
        kut= kut_;
        x =  x_;
        y = y_;
        float kut2_;
        kut2_= kut_*pi/180;
        vx = v*cos(kut2_);
        vy = v*sin(kut2_);

}

float Particle::__move(float dt){
    
            x = x + vx*dt;
            vy = vy - g*dt;
            y = y + vy*dt;
            t = t + dt;
            }

float Particle::range(float dt){
    
            
            do{
                __move(dt);
            }
            while (y>=0);
           
            

            std::cout << x << std::endl;
        }
        
float Particle::time(float dt){
            
            do{
                __move(dt);
            }
            while (y>=0);
            
            std::cout << t << std::endl;
            
        }