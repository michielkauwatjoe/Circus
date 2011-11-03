package scope.circus.physics;

import java.util.ArrayList;
import scope.toolbox.color.*;

import java.util.ArrayList;
import scope.toolbox.color.*;

import toxi.physics.VerletParticle;
import scope.circus.sketches.CircusSketch;

public class CircusParticle extends VerletParticle {
	CircusSketch sketch;
	public int lifespan;
	int maxlifespan;
	float age;
	int color;
	int max = 128;
	ArrayList<Integer> colorset1;
	ArrayList<Integer> colorset2;
	Swatch swatch;
	boolean transparency = true;

	public CircusParticle(float x, float y, float z, CircusSketch sketch, int lifespan, Swatch swatch) {
		super(x, y, z);
		this.sketch = sketch;
		this.maxlifespan = this.lifespan = lifespan;
		this.swatch = swatch;
		this.color = swatch.getRandomColor();
	  }
	
	/**
	 * Get alpha-value for particle transparency.
	 */
	private float getAlpha() {
		float alpha = 255f;
		
		if (lifespan > 0) {
			if (transparency) {
				alpha = age * 230f;
			} else {
				alpha = 230f;
			}
		}
		return alpha;
	}
	
	private void getAge() {
		/**
		 * Converts lifespan to float between 0.0 and 1.0.
		 */
		age = (float) lifespan / (float) maxlifespan;
	}
	
	private int getColor(ArrayList<Integer> colorset) {
		int n = (int) (sketch.generator.nextInt(colorset.size()));
		return colorset.get(n);
	}


	public void display() {
		float alpha;
		getAge();
		alpha = getAlpha();
		//sketch.translate(x, y, z);
		//sketch.sphere(28);
		//drawTarget(alpha);
		drawCube(alpha);
		
		lifespan -= 0.1;
	}
	
	private void drawCube(float alpha) {
		float factor = (float) 1.0;
		sketch.pushMatrix();
		sketch.translate(x * factor, y * factor, z * factor);
		//sketch.rotate(360 / age);
		sketch.fill(color, alpha);
		sketch.noStroke();
		int size = getCubeSize();
		float angle = getRotation();
		sketch.rotate(angle);
		sketch.box(size);
		sketch.popMatrix();
	}
	
	private int getCubeSize() {
		return (int) (age * 200f);
	}

	private float getRotation() {
		return (age * 18f);
	}
	
	private float getSize(int iteration) {
		return 1f / age * max / iteration;
	}

	private void drawTarget(float alpha) {
		
		for (int i = 0; i < swatch.size(); i++) {
			float size = getSize(i);
			sketch.noStroke();
			sketch.fill(swatch.getColor(i), alpha);
			sketch.ellipse(x, y, size, size);
			//sketch.translate(x, y, 0);
			//sketch.sphere(size);
		}
	}
}
