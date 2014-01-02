package nl.concretejungle.circus.sketches;
import nl.concretejungle.circus.toolbox.generative.video.BelousovZhabotinsky;
import processing.core.*;


public class BelousovZhabotinskySketch extends PApplet{
	private static final long serialVersionUID = 1L;
	BelousovZhabotinsky bz = new BelousovZhabotinsky();
	
	public void setup() 
	{
		//size (1366, 768, PGraphicsOpenGL.OPENGL);
		size (400, 400);
		colorMode(HSB, 2);		
		bz.bz_setup(this, width, height);
	  
	}

	public void draw() {

		background(0);
		float c = random((float)0.7, (float)1.0);
		colorMode(HSB, c);
		bz.bz_draw(this, width, height);
	}
}
