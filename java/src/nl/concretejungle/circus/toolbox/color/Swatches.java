package nl.concretejungle.circus.toolbox.color;

import java.util.ArrayList;
import java.util.Random;

public class Swatches {
	private ArrayList<Swatch> swatches;
	private Random generator;
	
	public Swatches () {
		swatches = new ArrayList<Swatch>();
		generator = new Random();
		buildSwatches();
	}
	
	private void buildSwatches() {
		ArrayList<Integer> arraylist = new ArrayList<Integer>();
		arraylist.add(0xffedfa59);
		arraylist.add(0xffa9af65);
		arraylist.add(0xff35352f);
		arraylist.add(0xff614f79);
		arraylist.add(0xffa66ae8);
		
		Swatch addTwoToHannah = new Swatch("Add Two To Hannah", arraylist);
		swatches.add(addTwoToHannah);

		arraylist = new ArrayList<Integer>();
		arraylist.add(0xffcfce97);
		arraylist.add(0xff9fac8a);
		arraylist.add(0xff5c604d);
		arraylist.add(0xff292329);
		arraylist.add(0xff29031b);
		
		Swatch toscana = new Swatch("Toscana", arraylist);
		swatches.add(toscana);

		arraylist = new ArrayList<Integer>();
		arraylist.add(0xff35384c);
		arraylist.add(0xffa7adc5);
		arraylist.add(0xffa7adc5);
		arraylist.add(0xfff8c5ff);
		arraylist.add(0xffff83e3);
		
		Swatch ceoBarbie = new Swatch("CEO Barbie", arraylist);
		swatches.add(ceoBarbie);

		arraylist = new ArrayList<Integer>();
		arraylist.add(0xfffffcc8);
		arraylist.add(0xffffd989);
		arraylist.add(0xfff8ab71);
		arraylist.add(0xfff16152);
		arraylist.add(0xffe80133);
		
		Swatch addToNicola = new Swatch("Add 2 Nicola (Piahr1)", arraylist);
		swatches.add(addToNicola);

		arraylist = new ArrayList<Integer>();
		arraylist.add(0xfff1e8b8);
		arraylist.add(0xffe3e0a6);
		arraylist.add(0xffd4dc8f);
		arraylist.add(0xffc7d28e);
		arraylist.add(0xffb7c297);
		
		Swatch fineMistOfBuds = new Swatch("Fine Mist Of Buds", arraylist);
		swatches.add(fineMistOfBuds);
	}
	
	public Swatch getSwatch() {
		int i = (int) generator.nextInt(swatches.size());
		System.out.println(i);
		Swatch swatch = swatches.get(i);
		swatch.shuffle();
		return swatch;
	}

}
