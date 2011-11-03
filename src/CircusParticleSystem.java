package scope.circus.physics;

import java.util.ArrayList;

import scope.circus.physics.CircusParticle;
import scope.circus.sketches.CircusSketch;
import java.util.Collections;
import scope.toolbox.color.*;
import toxi.physics.*;

public class CircusParticleSystem {
	
	private static final int numberOfParticles = 10;
	
	private CircusSketch sketch;
	ArrayList<Float> attractions;
	
	public CircusParticleSystem(CircusSketch sketch) {
		this.sketch = sketch;
		attractions = new ArrayList<Float>();
		attractions.add(0.0001f);
		attractions.add(0.0004f);
		attractions.add(0.00001f);
		
		CircusParticle p;
		Swatch swatch = sketch.swatches.getSwatch();
		
		for (int i = 0; i < numberOfParticles; i++) {
			int l = (int) ((float) i / 10f * 2000f) + 200;
			float x = (float)sketch.generator.nextFloat() * sketch.width;
			float y = (float) sketch.generator.nextFloat() * sketch.width;
			p = new CircusParticle(x, y, i, sketch, l, swatch);

			for (int j = 0; j < sketch.physics.particles.size(); j+= 2) {
				int n = (int) (sketch.generator.nextFloat() * 3f);
				float d = sketch.generator.nextFloat() * 500f;
				VerletSpring s = new VerletSpring(p, sketch.physics.particles.get(j), d, attractions.get(n));
				sketch.physics.addSpring(s);
			}
			sketch.physics.addParticle(p);
		}
	}
}
