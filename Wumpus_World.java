public class WumpusWorld {
    public static void main(String[] args) {
        
    }

    public WumpusFrame() extends JFrame {
        WumpusWorld world = new WumpusWorld();

    }

    public WumpusPanel extends JPanel implements ActionListener {
        private WumpusWorld world;

        public static final int PLAYING = 0;
        public static final int DEAD =1;
        public static final int WON = 2;
        public static final int STATUS = PLAYING;
        

        private int status = STATUS;
        private WumpusPlayer player = new WumpusPlayer();
        private WumpusMap map = new WumpusMap();
        
        public WumpusPanel(WumpusWorld world) {
            this.world = world;
        }

        
        public void actionPerformed(ActionEvent e) {
            
        }
    }
}