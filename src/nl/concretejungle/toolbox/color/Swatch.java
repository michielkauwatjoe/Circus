package nl.concretejungle.toolbox.color;

import java.util.ArrayList;
import java.util.Collections;

public class Swatch {
	ArrayList<Integer> hexvalues;
	public String name;

	public Swatch(String name, ArrayList<Integer> hexvalues) {
		this.name = name;
		this.hexvalues = hexvalues;
	}
	
	public int size() {
		return hexvalues.size();
	}
	
	public int getColor(int i) {
		return hexvalues.get(i);
	}
	
	public void shuffle() {
		Collections.shuffle(hexvalues);
	}
	
	public int getRandomColor() {
		float max = (float) (size() - 1);
		int index = (int) (Math.random() * max);
		return hexvalues.get(index);
	}
}
