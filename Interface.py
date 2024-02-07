import replicate
import os
import tkinter as tk
from tkinter import scrolledtext
import threading

class ChatInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("🦙💬 Llama 2 Chatbot")

        os.environ['REPLICATE_API_TOKEN'] = 'r8_FRW14AR69kzo3zmaeHEoUhj4c7OKayG3h5puK'

        self.pre_prompt = "Você é um assistente útil. Você não responde como 'Usuário' nem finge ser 'Usuário'. Você só responde uma vez como 'Assistente'."
        self.prompt_input = "Você consegue falar português?"

        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.output_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.input_label = tk.Label(root, text="Digite sua mensagem:")
        self.input_label.grid(row=1, column=0, padx=10, pady=5)

        self.input_entry = tk.Entry(root, width=30)
        self.input_entry.grid(row=1, column=1, padx=10, pady=5)

        self.send_button = tk.Button(root, text="Enviar", command=self.send_message)
        self.send_button.grid(row=2, column=0, columnspan=2, pady=10)

    def send_message(self):
        user_input = self.input_entry.get()
        
        # Limpar o campo de entrada
        self.input_entry.delete(0, tk.END)
        
        # Utilize threading para evitar travamentos
        thread = threading.Thread(target=self.generate_response, args=(user_input,))
        thread.start()

    def generate_response(self, user_input):
        # Gere a resposta do modelo LLM
        output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',
                               input={"prompt": f"{self.pre_prompt} {self.prompt_input} Assistant: {user_input}",
                                      "temperature": 0.1, "top_p": 0.9, "max_length": 128, "repetition_penalty": 1})

        # Exiba a resposta gerada na interface
        full_response = ""
        for item in output:
            full_response += item

        # Atualize a interface gráfica de maneira segura
        self.root.after(0, self.update_interface, user_input, full_response)

    def update_interface(self, user_input, full_response):
        self.output_text.insert(tk.END, f"Usuário: {user_input}\nAssistente: {full_response}\n\n")

if __name__ == "__main__":
    root = tk.Tk()
    chat_interface = ChatInterface(root)
    root.mainloop()
