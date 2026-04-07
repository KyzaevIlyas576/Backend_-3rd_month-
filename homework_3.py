import flet as ft 

def main_page(page: ft.Page):
    page.title = 'ДЗ №3'
    page.theme_mode = ft.ThemeMode.LIGHT

    def text_age(e):  # e - event | "_" 
        text_hello.value = "Укажите свой возраст"
        age = text_input.value.strip()
        text_hello.value = None


        if age.isdigit():
            if 18 <= int(age) < 100:
                text_hello.value = "Доступ разрешён"
                text_hello.color = ft.Colors.GREEN_900
            elif int(age) < 18:
                text_hello.value = "Доступ запрещён"
                text_hello.color = ft.Colors.RED_900
            elif int(age) >= 100:
                text_hello.value = "Как можно было дожить до 100?"
                text_hello.color = ft.Colors.BLACK_87
        else:
            text_hello.value = "Введите корректный возраст" 
            text_hello.color = ft.Colors.YELLOW_900

        page.update()

    text_hello = ft.Text('Привет', color=ft.Colors.BLUE_900)
    text_input = ft.TextField(label='Укажите свой возраст')
    btn = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=text_age)

    page.add(text_hello, text_input, btn)


ft.app(main_page, view=ft.AppView.WEB_BROWSER)
