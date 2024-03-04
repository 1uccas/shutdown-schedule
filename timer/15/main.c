#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
void timeShutdown(int request){
	int seconds=0, minutes=request, hour=0;
	
    
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE); /*PROPRIEDADE DE CORES*/

  	SetConsoleTextAttribute(hConsole, FOREGROUND_GREEN); /*COR VERDE EM TODO O TERMINAL*/
    while(1) {
        seconds--;
        if(seconds < 0){
            minutes--;
            seconds=59;
        }
        if(minutes < 0){
            hour--;
            minutes=59;
        }
        if(minutes == 0 && seconds==0 && hour == 0){
            break;
        }
        system("cls");
        printf("$ %02d : %02d  : %02d", hour, minutes, seconds);
        sleep(1); 
        system("cls");
    }
	SetConsoleTextAttribute(hConsole, FOREGROUND_RED);
	printf("$ Windows Desligado! ");
}
int main(int argc, char *argv[]) {
	timeShutdown(15);
	return 0;
}
