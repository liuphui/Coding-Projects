import javax.swing.JFrame;

/**
 * GameFrame
 */
public class GameFrame extends JFrame {
    GameFrame(){
        // this.add(new StartingMenu());
        // this.setTitle("Starting Menu");
        // this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // this.setResizable(false);
        // this.pack();
        // this.setVisible(true);
        // this.setLocationRelativeTo(null);

        this.add(new GamePanel());
        this.setTitle("Snake Game");
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setResizable(false);
        this.pack();
        this.setVisible(true);
        this.setLocationRelativeTo(null);
    }
}