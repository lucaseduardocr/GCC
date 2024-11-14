from database import *


class Login():
    def __init__(self, gui):
        self.gui = gui

    def login_verification(self):
        connection = database.create_connection()
        c = connection.cursor()
        email = self.gui.email_box_entry.get()
        password = self.gui.password_entry.get()
        print(f"Login Email = {email}")
        try:
            verification_email = c.execute("""SELECT EXISTS(SELECT 1 FROM users WHERE email = %s);""", (email,))
            result_email = c.fetchone()
            print(f"Resultado Busca email: {result_email}")
            if result_email == (True,):
                verification_password = c.execute("""SELECT EXISTS(SELECT 1 FROM users WHERE password = %s);""", (password,))
                result_password = c.fetchone()
                print(f"Email = {result_email} e Senha = {result_password}")
            else:
                print("email não encontrado!")
        finally:
            c.close()
            print("Servidor Fechado")
        