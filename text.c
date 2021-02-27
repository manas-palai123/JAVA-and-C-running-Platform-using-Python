#include <stdio.h>
float f(long,long); 
int main(){
	float res = f(2,3);
	printf("result = %d\n",(int)res );
	return 0;
}
float f(long m,long n){
	float result = (float)m/(float)n;
	if(m < 0 || n < 0){
		return 0.0f;
	}
	else
	{
		return result+=f(m*2,n*3);
	}
}




























