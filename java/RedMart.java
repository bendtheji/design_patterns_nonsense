import java.util.*;

public class RedMart {
	public static void main(String [] args){

		int[][] mainArray;
		Integer[][] pathLength =  new Integer[1][1];
		Integer[][] heightDifference = new Integer[1][1];

		mainArray = formArrayFromInput(pathLength, heightDifference);
		System.out.println(Arrays.deepToString(pathLength));
	}

	public static int[][] formArrayFromInput(Integer[][] pathLength, Integer[][] heightDifference){

		int iteration = 0;
		int[][] mainArray = new int[1][1];
		try {
			Scanner scan = new Scanner(System.in);

			while (scan.hasNextLine()){
				String string = scan.nextLine();

				if(string == ""){
					break;
				}

				// assign length and width of array
				if(iteration == 0){
					System.out.println("Setting measurements");
					String[] measurements = string.split(" ");
					int x = Integer.parseInt(measurements[0]);
					int y = Integer.parseInt(measurements[1]);
					mainArray = new int[x][y];
					pathLength = new Integer[x][y];
					heightDifference = new Integer[x][y];
					iteration++;
				}
				else if (iteration > 0){
					System.out.println("Setting matrix");
					String[] elevations = string.split(" ");
					mainArray[iteration-1][0] = Integer.parseInt(elevations[0]);
					mainArray[iteration-1][1] = Integer.parseInt(elevations[1]);
					mainArray[iteration-1][2] = Integer.parseInt(elevations[2]);
					mainArray[iteration-1][3] = Integer.parseInt(elevations[3]);
					iteration++;
				}
			}

		}

		catch (Exception e){

		}
		return mainArray;
	}
}