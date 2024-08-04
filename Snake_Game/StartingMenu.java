import javax.swing.*;
import java.awt.event.*;
import java.awt.Button;
import java.awt.*;

/**
 * StartingMenu
 */
public class StartingMenu extends JPanel {
    static final int SCREEN_WIDTH = 600;
    static final int SCREEN_HEIGHT = 600;
    JButton startButton;

    StartingMenu(){
        this.setPreferredSize(new Dimension(SCREEN_WIDTH, SCREEN_HEIGHT));
        this.setBackground(Color.black);
        this.setFocusable(true);

        startButton = new JButton();
        startButton.setFont(new Font("Arial", Font.BOLD, 25));
        startButton.addActionListener(new StartButtonListener());

        this.add(startButton, BorderLayout.CENTER);
    }

    public class StartButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            this.setVisible(false);
        }
    }
}