from tkinter import *
import Cryptic as cf  # Импорт модуля для шифрования


class EncryptionApp:
    def __init__(self, title="Программа шифрования", size='450x300'):
        self.root = Tk()  # Создание основного окна
        self.root.title(title)
        self.root.geometry(size)
        self.root.resizable(True, True)

        # Секция для шифрования (размещение и скрытие): поле ввода текста и поле ввода ключа, кнопка "Зашифровать")
        self.lbl_text = Label(self.root, text="Текст:")
        self.lbl_text.grid(column=0, row=1)
        self.lbl_text.grid_forget()
        self.text_input = Entry(self.root, width=30)
        self.text_input.grid(column=0, row=2)
        self.text_input.grid_forget()
        self.lbl_key = Label(self.root, text="Ключ:")
        self.lbl_key.grid(column=0, row=3)
        self.lbl_key.grid_forget()
        self.key_input = Entry(self.root, width=30)
        self.key_input.grid(column=0, row=4)
        self.key_input.grid_forget()
        self.btn_encrypt = Button(self.root, text="Зашифровать", command=self.btn_encrypt_clicked)
        self.btn_encrypt.grid(column=0, row=7)
        self.btn_encrypt.grid_forget()

        # Кнопка "Расшифровать" (размещение и скрытие)
        self.btn_decrypt = Button(self.root, text="Расшифровать", command=self.btn_decrypt_clicked)
        self.btn_decrypt.grid(column=0, row=7)
        self.btn_decrypt.grid_forget()

        # Секция для расшифровки (размещение и скрытие): поле ввода зашифрованного текста, и поле ввода ключа
        self.lbl_encrypted_text = Label(self.root, text="Зашифрованный текст:")
        self.lbl_encrypted_text.grid(column=0, row=8)
        self.lbl_encrypted_text.grid_forget()
        self.encrypted_text_input = Entry(self.root, width=30)
        self.encrypted_text_input.grid(column=0, row=9)
        self.encrypted_text_input.grid_forget()

        self.btn_encr_page = Button(self.root, text="Страница Зашифровки",
                                    command=self.btn_encr_page_clicked)
        self.btn_encr_page.grid(column=0, row=0, padx=20, pady=20)
        self.btn_decryption_page = Button(self.root, text="Страница Расшифровки",
                                          command=self.btn_decryption_page_clicked)
        self.btn_decryption_page.grid(column=1, row=0, padx=20, pady=20)

        self.current_mode = 'None'  # Изначально установлен режим "None"
        self.root.mainloop()  # Запуск главного цикла приложения

    # Обработчик нажатия кнопки "Зашифровать"
    def btn_encrypt_clicked(self):
        t = self.text_input.get()  # Получение текста из поля ввода
        s = self.key_input.get()  # Получение ключа из поля ввода
        etext = cf.encrypt_text(t, s)  # Шифрование текста
        self.lbl_encrypted_text.grid()  # Отображение надписи "Зашифрованный текст:"
        self.encrypted_text_input.delete(0, END)  # Очистка поля ввода зашифрованного текста
        self.encrypted_text_input.insert(0, etext)  # Вставка зашифрованного текста в поле ввода
        self.encrypted_text_input.grid()  # Отображение поля ввода зашифрованного текста

    # Обработчик нажатия кнопки "Расшифровать"
    def btn_decrypt_clicked(self):
        t = self.encrypted_text_input.get()  # Получение зашифрованного текста из поля ввода
        s = self.key_input.get()  # Получение ключа из поля ввода
        decrypt_text = cf.decrypt_text(t, s)  # Расшифровка текста
        self.lbl_text.grid()  # Отображение надписи "Текст:"
        self.text_input.delete(0, END)  # Очистка поля ввода текста
        self.text_input.insert(0, decrypt_text)  # Вставка расшифрованного текста в поле ввода
        self.text_input.grid()  # Отображение поля ввода текста

    # Функция смены режима отображения (Страница Зашифровки/Страница Расшифровки)
    def change_mode(self, new_mode):
        if self.current_mode == new_mode:
            return
        self.current_mode = new_mode
        if new_mode == 'encrypt':
            # Отображение элементов для шифрования и скрытие элементов для расшифрования
            self.lbl_text.grid(row=1)
            self.text_input.grid(row=2)
            self.lbl_text.grid()
            self.text_input.grid()
            self.lbl_key.grid()
            self.key_input.grid()
            self.btn_encrypt.grid()
            self.lbl_encrypted_text.grid(row=8)
            self.encrypted_text_input.grid(row=9)
            self.lbl_encrypted_text.grid_forget()
            self.encrypted_text_input.grid_forget()
            self.btn_decrypt.grid_forget()
        elif new_mode == 'decrypt':
            # Отображение элементов для расшифрования и скрытие элементов для шифрования
            self.lbl_encrypted_text.grid(row=1)
            self.encrypted_text_input.grid(row=2)
            self.lbl_key.grid()
            self.key_input.grid()
            self.lbl_text.grid(row=8)
            self.text_input.grid(row=9)
            self.lbl_text.grid_forget()
            self.text_input.grid_forget()
            self.btn_encrypt.grid_forget()
            self.btn_decrypt.grid()

    # Обработчик нажатия кнопки "Страница Зашифровки"
    def btn_encr_page_clicked(self):
        self.change_mode('encrypt')  # Переключение на режим шифрования

    # Обработчик нажатия кнопки "Страница Расшифровки"
    def btn_decryption_page_clicked(self):
        self.change_mode('decrypt')  # Переключение на режим расшифрования


EncryptionApp()
