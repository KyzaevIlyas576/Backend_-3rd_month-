import flet as ft

def main_page(page: ft.Page):
    page.title = "Счётчик"

    count = 0
    
    text_hello = ft.Text("Нажато: 0 раз", size=20)

    def increment(e):
        nonlocal count  # даёт доступ к переменной выше
        
        count += 1
        text_hello.value = f"Нажато: {count} раз"
        page.update()

    btn = ft.ElevatedButton("Нажми меня", on_click = increment)

    page.add(
        ft.Column(
            controls=[
                text_hello,
                btn
            ],
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        )
    )


ft.app(main_page, view=ft.AppView.WEB_BROWSER)
