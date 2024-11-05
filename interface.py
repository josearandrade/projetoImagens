import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt

# Funções Python que serão chamadas pelos botões
def say_hello():
    return "Hello, PyQt6!"

def say_goodbye():
    return "Goodbye, PyQt6!"

# Classe que representa a janela principal da aplicação
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configurações básicas da janela
        self.setWindowTitle("Exemplo PyQt6 com Funções Python")
        self.setGeometry(100, 100, 400, 200)

        # Layout principal da janela
        layout = QVBoxLayout()

        # Label para mostrar o resultado da função chamada
        self.label = QLabel("Pressione um botão")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        # Botão que chama a função 'say_hello'
        self.hello_button = QPushButton("Dizer Hello")
        self.hello_button.clicked.connect(self.on_hello_clicked)  # Conecta o clique do botão à função
        layout.addWidget(self.hello_button)

        # Botão que chama a função 'say_goodbye'
        self.goodbye_button = QPushButton("Dizer Goodbye")
        self.goodbye_button.clicked.connect(self.on_goodbye_clicked)
        layout.addWidget(self.goodbye_button)

        # Define o layout principal para a janela
        self.setLayout(layout)

    # Função chamada quando o botão 'Dizer Hello' é clicado
    def on_hello_clicked(self):
        message = say_hello()  # Chama a função Python
        self.label.setText(message)  # Exibe o retorno da função no label

    # Função chamada quando o botão 'Dizer Goodbye' é clicado
    def on_goodbye_clicked(self):
        message = say_goodbye()
        self.label.setText(message)

# Executa a aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Cria a janela principal e exibe
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
