/* Idealised Belousov–Zhabotinsky reaction 
 * (c) Alasdair Turner 2009 
 * Free Software 
 * Licensed according to the GNU GPL 
 * An implementation note about this algorithm is available here: 
 * http://www.aac.bartlett.ucl.ac.uk/processing/samples/bzr.pdf 
 */

package nl.concretejungle.circus.toolbox.generative.video;
import processing.core.*;

public class BelousovZhabotinsky {
	
	float [][][] a; 
	float [][][] b; 
	float [][][] c; 
	 
	int p = 0, q = 1; 
	
	public void bz_setup(PApplet parent, int width, int height) {
		a = new float [width][height][2];
		  b = new float [width][height][2];
		  c = new float [width][height][2];
		  for (int x = 0; x < width; x++) { 
		    for (int y = 0; y < height; y++) { 
		      a[x][y][p] = parent.random((float) 0.0, (float) 1.0); 
		      b[x][y][p] = parent.random((float) 0.0, (float) 1.0); 
		      c[x][y][p] = parent.random((float) 0.0, (float) 1.0); 
		      
		      float color1 = parent.random((float) 0.0, (float) 1.0) * (float) 0.5;
		      float color2 = parent.random((float) 0.0, (float) 1.0) * (float) 0.7;
		      
		      parent.set(x, y, parent.color(color1, color2, a[x][y][p])); 
		    } 
		  } 
	}
	
	public void bz_draw(PApplet parent, int width, int height) {
		for (int x = 0; x < width; x++) { 
			for (int y = 0; y < height; y++) { 
				float c_a = (float) 0.0; 
				float c_b = (float) 0.0; 
				float c_c = (float) 0.0; 

				for (int i = x - 1; i <= x + 1; i++) { 
					for (int j = y - 1; j <= y+1; j++) { 
						c_a += a[(i + width) % width][(j + height) % height][p]; 
						c_b += b[(i + width) % width][(j + height) % height][p]; 
						c_c += c[(i + width) % width][(j + height) % height][p]; 
					} 
				} 

				c_a /= 9.0;
				c_b /= 9.0;
				c_c /= 9.0;

				// adjust these values to alter behaviour 
				a[x][y][q] = PApplet.constrain(c_a + c_a * (c_b - c_c), 0, 1);
				b[x][y][q] = PApplet.constrain(c_b + c_b * (c_c - c_a), 0, 1);
				c[x][y][q] = PApplet.constrain(c_c + c_c * (c_a - c_b), 0, 1);
				parent.set(x, y, parent.color((float) 0.5, (float) 0.7, a[x][y][q])); 
			} 
		} 

		if (p == 0) { 
			p = 1;
			q = 0;
		} else { 
			p = 0;
			q = 1;
		} 
	}
}
