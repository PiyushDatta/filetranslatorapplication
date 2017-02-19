from javax.swing import (BoxLayout, ImageIcon, JButton, JFrame, JPanel,
        JPasswordField, JLabel, JTextArea, JTextField, JScrollPane,
        SwingConstants, WindowConstants)
from java.awt import Component, GridLayout, GridBagLayout, GridBagConstraints, BorderLayout


class main_app():
    def __init__(self):
        # Make the frame and set its properties
        self.frame = JFrame("File Translator", defaultCloseOperation=WindowConstants.EXIT_ON_CLOSE,
                            layout=GridBagLayout())
        self.frame.setSize(1200, 800)

        # Make a GridBagLayout for this frame
        gridbag = GridBagLayout()
        constraints = GridBagConstraints()
        constraints.fill = GridBagConstraints.CENTER

        # Make sure to have a panel to hold everything
        self.loginPanel = JPanel(GridLayout(0, 2))
        self.frame.add(self.loginPanel)
        gridbag.setConstraints(self.loginPanel, constraints)
        self.loginPanel.setLayout(gridbag)

        # Entry for the path
        self.usernameField = JTextField('', 30)
        self.loginPanel.add(JLabel("username:"))
        self.loginPanel.add(self.usernameField)

        # Entry for the number of pages
        self.textField = JTextField('', 30)
        self.loginPanel.add(JLabel("password:"))
        self.loginPanel.add(self.textField)

        # Make a button to enter the information
        self.loginButton = JButton('Enter', actionPerformed=enter_button)
        self.loginPanel.add(self.loginButton)
        self.frame.add(self.loginPanel)

        # Make everything visible and make sure it starts at centre of screen
        self.frame.pack()
        self.frame.setLocationRelativeTo(None)
        self.frame.setVisible(True)


def enter_button(event):
    print('Clicked!')


if __name__ == '__main__':
    win = main_app()
