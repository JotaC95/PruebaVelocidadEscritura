import tkinter as tk
import time


class TypingTest:
    # El constructor de la clase configura la ventana de la aplicación
    def __init__(self, root):
        self.root = root
        self.root.title("Prueba de escritura")

        # Configuración de los cronómetros
        self.start_time = 0
        self.stop_time = 0

        # Primera entrada para la palabra que se usa de modelo
        self.label_phrase_modelo = tk.Label(root, text="Ingresa la frase a copiar")
        self.label_phrase_modelo.pack()  # Anade el elemento a la ventana
        # Entrada de texto para la frase a copiar
        self.entry_phrase_modelo = tk.Entry(root, width=50)
        self.entry_phrase_modelo.pack()

        # Boton que llama a la funcion cuando es aplastado
        self.btn_inicio = tk.Button(root, text="Inicio", command=self.start_test)
        self.btn_inicio.pack()

        # Tipeo de la primera frase
        self.typing_phrase = tk.Label(
            root, text="Empieza a escribir la frase que ingresaste"
        )
        self.typing_phrase.pack()

        # Entrada de texto para copiar la frase
        self.entry_phrase_typing = tk.Entry(root, width=50)
        self.entry_phrase_typing.pack()
        self.entry_phrase_typing.bind(
            "<Return>", self.end_test
        )  # Llama a la funcion cuando el evento tecla enter es activado

        # Label de istruccion para terminar y obtener el tiempo
        self.final_label = tk.Label(root, text="Aplasta la tecla enter al terminar!")
        self.final_label.pack()

        # label para guardar el texto del tiempo final que toma typear la frase
        self.result = tk.Label(root, text="")
        self.result.pack()

    # Funciom que se inicia al activar el boton desactuva el label de frase modelo, inicia el contador
    # Elimina informacion anterios de los entry y mueve el puntero a la entrada de la frese typeada
    def start_test(self):
        self.entry_phrase_modelo.config(state="disabled")
        self.start_time = time.time()
        self.result.config(text="")
        self.entry_phrase_typing.delete(0, tk.END)
        self.entry_phrase_typing.focus()

    # Se activa con el evento de la tecla enter que es pasado como objeto de parametro, toma el tiempo final
    # y calcula el tiempo de escritura, compara el texto modelo con el ingresado por el usuario
    # muestra el resultado en el label
    def end_test(self, event):
        self.stop_time = time.time()
        original_phrase = self.entry_phrase_modelo.get()
        typed_phrase = self.entry_phrase_modelo.get()

        if original_phrase == typed_phrase:
            final_time = self.stop_time - self.start_time
            self.result.config(text=f"Te tomó: {final_time:.2f} segundos")
        else:
            self.result.config(text="Tienes un error, inténtalo otra vez")
            self.entry_phrase_modelo.config(state="normal")

        # Habilitar la entrada de la frase original para la siguiente prueba
        self.entry_phrase_modelo.config(state="normal")


# Inicio del programa crea un objeto root para pa ventana principal, crea una instancia con la clase e
# inicia el bucle principal
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTest(root)
    root.mainloop()
