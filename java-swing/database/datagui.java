import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class database_manager {
	public static void main(String args[]) {
		JFrame frame = new JFrame("Database manager");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(600,400);

		JMenuBar mb = new JMenuBar();
		JMenu m1 = new JMenu("File");
		JMenu m2 = new JMenu("Help");
		mb.add(m1);
		mb.add(m2);
		JMenuItem m11 = new JMenuItem("New");
		JMenuItem m12 = new JMenuItem("Open");
		JMenuItem m13 = new JMenuItem("Save as");
		JMenuItem m14 = new JMenuItem("Save");
		JMenuItem m21 = new JMenuItem("Get Online Help");
		m1.add(m11);
		m1.add(m12);
		m1.add(m13);
		m1.add(m14);
		m2.add(m21);

		JPanel panel = new JPanel();
		JLabel label1 = new JLabel("Value 1");
		JTextField tf1 = new JTextField(10);
		JLabel label2 = new JLabel("Value 2");
		JTextField tf2 = new JTextField(10);
		JButton insert = new JButton("Insert");
		JLabel label3 = new JLabel("Delete by id");
		JTextField tf3 = new JTextField(4);
		JButton remove = new JButton("Delete");
		panel.add(label1);
		panel.add(tf1);
		panel.add(label2);
		panel.add(tf2);
		panel.add(insert);
		panel.add(label3);
		panel.add(tf3);
		panel.add(remove);

		JPanel table = new JPanel();
		JLabel tabletxt = new JLabel();
		tabletxt.setText("Ola mundo");
		table.add(tabletxt);

		frame.getContentPane().add(BorderLayout.SOUTH, panel);
		frame.getContentPane().add(BorderLayout.NORTH, mb);
		frame.getContentPane().add(BorderLayout.CENTER, table);
		frame.setVisible(true);
	}
}
	


