package STUDY;

public class Car {
	String color;
	int door;
	void dirve() {
		System.out.print("drive");
	}
	
	void stop() {
		System.out.print("stop");
	}
}

class FireEngine extends Car{
	void water() {
		System.out.print("water");
	}
}

class Ambulance extends Car{
	void siren() {
		System.out.print("siren");
	}
}
