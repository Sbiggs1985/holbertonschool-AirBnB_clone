
            HBNBCommand().onecmd("quit")
        # modelling what happens when someone types `quit`
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        # modelling when user types `quit anything`
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    # Test cases for EOF
    def test_do_EOF(self):
        """Tests the EOF commmand"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        # modelling what happens when user types `quit`
        msg = f.getvalue()
        self.assertTrue(len(msg) == 1)
        self.assertEqual("\n", msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF garbage")
        # modelling when user types `EOF anything`
        msg = f.getvalue()
        self.assertTrue(len(msg) == 1)
        self.assertEqual("\n", msg)

    # Test cases for emptyline
    def test_do_emptyline(self):
        """Tests the emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        # modelling what happens when user doesn't type anything
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                     \n")
        # modelling when user types lots of whitespaces & enter
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    # Test cases for do_all
    def test_do_all(self):
        """Tests the do_all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")

    # Test cases for do_count
    # Test cases for do_show
    # Test cases for do_create
    # Test cases for do_update
    # Test cases for do_destroy


if __name__ == "__main__":
    unittest.main()
