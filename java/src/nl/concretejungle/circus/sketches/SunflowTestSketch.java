package nl.concretejungle.circus.sketches;
import processing.core.*;
import java.io.FileOutputStream;
import java.io.DataOutputStream;


public class SunflowTestSketch extends PApplet{
	private static final long serialVersionUID = 1L;
	
	public void setup() 
	{
		try {
			FileOutputStream fs = new FileOutputStream("/Users/michiel/" + (System.currentTimeMillis() / 1000) + ".pointcloud");
			DataOutputStream ds = new DataOutputStream(fs);
			float x = 0,y = 0,z = 0; // start at origin
			float scl = (float) 0.25;
			float dim = 50;
			
			for (int i = 0; i < 250000; i++) {
				// randomly progress within the bounding box
				x = max(-dim, min(dim, x + random(-1, 1) * scl));
				y = max(-dim, min(dim, y + random(-1, 1) * scl));
				z = max(-dim, min(dim, z + random(-1, 1) * scl));

				// write out coordinates as raw floats
				ds.writeFloat(x);
				ds.writeFloat(y);
				ds.writeFloat(z);
			}
			ds.flush();
			ds.close();
			println("done.");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}