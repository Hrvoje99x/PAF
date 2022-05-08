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
        float vy;
        float t = 0;
        Particle(float v, float kut_, float x_, float y_);

    private:

        float __move(float dt);

    public:

        float range(float dt);
        float time(float dt);
};