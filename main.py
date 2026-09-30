from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

NOME_APP = 'Teste GitHub'
CATEGORIAS = ['principal', 'documentos']


class TelaPrincipal(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(
            orientation="vertical",
            spacing=dp(10),
            padding=dp(15),
            **kwargs
        )

        self.add_widget(
            Label(
                text=NOME_APP,
                font_size="26sp",
                size_hint_y=None,
                height=dp(70)
            )
        )

        self.add_widget(
            Label(
                text="Categorias",
                font_size="18sp",
                size_hint_y=None,
                height=dp(45)
            )
        )

        scroll = ScrollView()

        lista = BoxLayout(
            orientation="vertical",
            spacing=dp(10),
            size_hint_y=None
        )

        lista.bind(
            minimum_height=lista.setter("height")
        )

        for categoria in CATEGORIAS:
            botao = Button(
                text=categoria,
                size_hint_y=None,
                height=dp(65),
                font_size="18sp"
            )

            botao.bind(
                on_release=lambda botao:
                self.selecionar_categoria(botao.text)
            )

            lista.add_widget(botao)

        scroll.add_widget(lista)
        self.add_widget(scroll)

        self.status = Label(
            text="Aplicativo pronto.",
            size_hint_y=None,
            height=dp(50)
        )

        self.add_widget(self.status)

    def selecionar_categoria(self, categoria):
        self.status.text = (
            "Categoria selecionada: "
            + categoria
        )


class AplicativoGerado(App):

    def build(self):
        self.title = NOME_APP
        return TelaPrincipal()


if __name__ == "__main__":
    AplicativoGerado().run()
