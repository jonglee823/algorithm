package STUDY;

public class test {

	public static void main(String[] args) {

		Integer i = 0;
		String z = "0";
		String useNewZ = new String("0");
		String useNewX = new String("0");
		
		System.out.println("useNewZ == useNewX : " + useNewZ == useNewX);
		System.out.println("useNewZ.equals(useNewX) : " + useNewZ.equals(useNewX));
		
		System.out.println("i : " + System.identityHashCode(i));
		System.out.println("z : " + System.identityHashCode(z));
		System.out.println("i.toString() : " + System.identityHashCode(i.toString()));
		System.out.println("useNewZ : " + System.identityHashCode(useNewZ));
		System.out.println();
		
		System.out.println("useNewZ == z : " + useNewZ == z);
		System.out.println("useNewZ.equals(z) : " + useNewZ.equals(z));
		
		System.out.println();
		
		System.out.println("z.equals(i) : " + z.equals(i));
		System.out.println("test : " + z == i.toString());
		
		System.out.println();
		System.out.println("z.equals(i.toString()) : " + z.equals(i.toString()));
		System.out.println("useNewZ.equals(i.toString()) : " + useNewZ.equals(i.toString()));
		
		
	}
}
