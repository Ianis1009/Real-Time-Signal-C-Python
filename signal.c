#include <stdio.h>
#include <math.h>
#include <unistd.h>

#define STEP 0.03
#define MS_DELAY 50000
#define LOOP 1

double t = 0.0;
double alpha = 0.1;
double omega = 2.0;

int main() {
    

    while (LOOP) {
        
        double f_t = exp(-alpha * t) * sin(omega * t);
        printf("%f\n", f_t);
        fflush(stdout);
        t += STEP;
        usleep(MS_DELAY);
    }

    return 0;
}