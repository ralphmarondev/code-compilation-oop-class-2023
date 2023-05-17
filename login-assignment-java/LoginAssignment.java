package assignment20230504.loginassignment;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class LoginAssignment
{
    public static void main(String[] args)
    {
        Login login = new Login();

        login.setBounds(400, 200, 500, 300);
        login.setVisible(true);

    }
}

class Login extends JFrame
{
    JTextField t1, t2;
    JButton b1;
    JButton b2;
    JLabel l1;

    Login()
    {
        setTitle("Hello there");
        setLayout(null);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        l1 = new JLabel("LOGIN");
        l1.setFont(new Font("Courier New", Font.PLAIN, 30));
        l1.setForeground(Color.BLUE);
        l1.setBounds(120, 10, 300, 30);
        add(l1);

        t1 = new JTextField(60);
        t2 = new JPasswordField(60);
        b1 = new JButton("SIGNIN");
        b2 = new JButton("CLEAR");

        t1.setBounds(120, 60, 300, 30);
        t2.setBounds(120, 100, 300, 30);
        b1.setBounds(120, 140, 80, 30);
        b2.setBounds(220, 140, 80, 30);

        add(t1);
        add(t2);
        add(b1);
        add(b2);

        b1.addActionListener(new ActionListener()
        {
            @Override
            public void actionPerformed(ActionEvent e)
            {
                if (t1.getText().toString().equals("root") && t2.getText().toString().equals("toor"))
                {
                    System.out.println("HELLO"); // display on console
                    JOptionPane.showMessageDialog(null, "success");
                }
                else
                {
                    System.out.println("HI"); // display on console
                    JOptionPane.showMessageDialog(null, "failed");
                }
            }
        });

        b2.addActionListener(new ActionListener()
        {
            @Override
            public void actionPerformed(ActionEvent e)
            {
                t1.setText("");
                t2.setText("");
            }
        });
    }
}
