int main()
{
	int a = 0;
	int b = 0;
	int temp = 1;
	int array[2000];
	char ch = 'R';
	for (temp = 112; temp < 1000; temp = temp + 1)
	{
		b = b + 1;
		temp = temp + 1;
		array[temp] = 1;
    }
	temp = temp - 900;
	for (temp = 1; temp < 100; temp = temp + 1)
	{
		b = b - 1;
		array[temp]=array[temp] + 1;
	}
	int c = 0;
	while (b < c)
	{
		b = b + 1;
		while (a < 10240)
		{
			a = a + 1;
			if (a > 100)
			{
				a = a + 9;
				b = b + 1;
			}
			array[a] = a;
		}
	}
	while (a > 0)
	{
		a = a - 1;
		//printf("%c",ch);
		while (b > 0)
		{
			b = b - 1;
			//printf("%c",ch);
		}
	}
}

/*

	while(a){
		a=a-1;
		printf("%c",ch);
		while(b){
			b=b-1;
			printf("%c",ch);
		}
	}

*/