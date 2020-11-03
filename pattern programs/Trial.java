package dummy;

public class Trial
{
	public static void main(String[] args)
	{
		for(int i=1;i<=15;i++)
		{
			for(int j=1;j<i;j++)
			{
				System.out.print("  ");
			}
			System.out.print(" "+i);
			for(int l=58;l>2*i;l--) 
			{
				System.out.print(" ");
			}
			for(int n=15;n>i;n--)
			{
				System.out.print("  ");
			}
			if(i<10)
			{
				System.out.print(" ");
			}
			
			for(int m=1;m<=1 ;m++)
			{
				System.out.print("  "+i);
			}
			System.out.println();
		}
		for(int i=14;i>=1;i--)
		{
			for(int j=1;j<i;j++)
			{
				System.out.print("  ");
			}
			System.out.print(i);
			for(int l=60;l>2*i;l--) 
			{
				System.out.print(" ");
			}
			for(int n=15;n>i;n--)
			{
				System.out.print("  ");
			}
			if(i<10)
			{
				System.out.print(" ");
			}
			System.out.print(" "+i);
			System.out.println();
			
		}
	}
}