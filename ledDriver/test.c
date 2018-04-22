#include "matLib.c"
int main() {

    setBothMatrices('0', 'o');
    sleep(1);
    cleanBothMatrices();
    sleep(1);
    setBothMatrices('(', ')');

    return 0;
}
