#include <iostream>
#include <cmath>
#include <algorithm>

void ispis(int polje[], int a, int b){
    for (int i = 0; i<20; i++)
    { 
        if (polje[i] >= a){
            if (polje[i] <= b){
            std::cout << polje[i] << std::endl;
            }
        }
        
    }
}
void zamjena_dva(int polje[], int a, int b){
    int x = polje[a];
    polje[a]=polje[b];
    polje[b]= x;
}
    
void elementi(int polje[]) {
        for ( int i = 0; i<20; i++){
        std::cout << polje[i] << std::endl;
    }
}

int main(){
    int polje[20]= {-10,2,34,11,-32,13,56,-23,43,1,0,-5,4,14,-15,16,-17,18,-19,20};
    ispis(polje,-5,15);
    zamjena_dva(polje,1,15);
    elementi(polje);
    std::sort(std::begin(polje), std::end(polje));
    elementi(polje);

    std::reverse(std::begin(polje), std::end(polje));
    elementi(polje);
    return 0;
}