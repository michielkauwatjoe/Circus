package nl.concretejungle.circus.sketches;

import processing.core.*;
import processing.video.*;
import nl.concretejungle.circus.physics.*;
import nl.concretejungle.toolbox.color.*;
import toxi.physics.*;
import toxi.geom.*;
import java.util.Random;
import processing.opengl.*;
import javax.media.opengl.*;


public class CircusSketch extends PApplet{
	
	private static final long serialVersionUID = 1L;
	private static final boolean record = false;
	
	public Random generator;
	public VerletPhysics physics;
	public int width;
	public int height;
	public Swatches swatches;
	
	float eyex;
	float eyey;
	float eyez;
	float centerx;
	float centery;
	float centerz;
	float upx;
	float upy;
	float upz;
	
	float rotatex = -PI/ (float)6;
	float rotatey = -PI/ (float)3;
	
	private int fr;
	private String moviepath;
	private CircusParticleSystem circusParticleSystem;
	private MovieMaker mm;  // Declare MovieMaker object.
	
	private void initializeApplet() {
		width = 1024;
		height = 768;
		fr = 30;
		size(width, height, OPENGL);
		smooth();
		frameRate(fr);
		eyex = width / (float) 2.0;
		eyey = height / (float) 2.0;
		eyez = (height / (float) 2.0) / tan((float) PI * (float) 60.0 / (float) 360.0) + 2000;
		centerx = eyex;
		centery = eyey;
		centerz = 0;
		upx = 0;
		upy = 1;
		upz = 0;
		camera(eyex, eyey, eyez,
				centerx, centery, centerz,
				upx, upy, upz);
		
	}
	
	public void setup() {
		initializeApplet();
		generator = new Random();
		swatches = new Swatches();
		if (record) {
			moviepath = new String("/Users/michiel/drawing.mov");
			mm = new MovieMaker(this, width, height, moviepath, fr, MovieMaker.RAW, MovieMaker.LOSSLESS);
		}

		initializePhysics();
		circusParticleSystem = new CircusParticleSystem(this);
	}
	
	private void initializePhysics() {
		physics = new VerletPhysics();
		float x = 0.0f;
		float y = 0.00001f;
		float z = 0.0f;

		Vec3D vector = new Vec3D(x, y, z);
		physics.gravity = vector;
		
		// This is the center of the world.
		Vec3D center = new Vec3D(width / 2,height / 2, 0);
		// These are the worlds dimensions (a vector pointing out from the center).
		Vec3D extent = new Vec3D(width / 2, height / 2, 0);
		
		// Set the world's axis-aligned bounding box.
		AABB aabb = new AABB(center, extent);
		physics.setWorldBounds(aabb);
	}
	
	private void physicsCallback() {
		/**
		 *  Displays the particles.
		 */
		for (int i = physics.particles.size() - 1; i > 0; i--) {
			CircusParticle cp = (CircusParticle) physics.particles.get(i);
			cp.display();
		}
	}

	public void draw() {
		/**
		 * PApplet callback function.
		 */
		physics.update();							// Update the physics world
		background(0);
		physicsCallback();
		eyez -= 10.0;
		rotatex += 10;
		rotatey += 20;
		rotateX(rotatex);
		rotateY(rotatey);

		
		camera(eyex, eyey, eyez,
				centerx, centery, centerz,
				upx, upy, upz);

		if (record) {
			mm.addFrame();			
		}
	}
	
	public void keyPressed() {
		  if (record && key == ' ') {
		    mm.finish();  // Finish the movie if space bar is pressed!
		  }
	}
}