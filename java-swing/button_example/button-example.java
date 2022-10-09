import javax.swing.*;
class gui {
	public static void main(String args[]) {
		JFrame frame = new JFrame("My first GUI");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(300,300);
		JButton button = new JButton("Press me. I am a button :)");
		frame.getContentPane().add(button);
		frame.setVisible(true);
	}
}
