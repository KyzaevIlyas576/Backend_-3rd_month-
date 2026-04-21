import flet as ft 

def main_page(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_history = []

    text_hello = ft.Text('Как тебя зовут?', size=20)
    text_input = ft.TextField(label='Ваше имя')
    greeting_text = ft.Column()

    def update_history_view():
        greeting_text.controls.clear()
        for name in greeting_history:
            greeting_text.controls.append(ft.Text(f"Привет, {name}!"))

    def text_name(e):
        name = text_input.value.strip()

        if not name:
            text_hello.value = "Введите корректное имя!"
            text_hello.color = ft.Colors.RED_900

        # 2) Если пользователь вводит имя, которое уже есть в списке greeting_history, приложение не должно добавлять его второй раз.
        # Вместо этого оно должно вывести сообщение: "Это имя уже в истории!" (красным цветом). Если имени нет — добавляем как обычно.
        elif name in greeting_history:
            text_hello.value = "Это имя уже в истории!"
            text_hello.color = ft.Colors.RED_900

        # 3) Запретить добавлять имена, состоящие только из цифр (метод .isdigit()). Если ввели только цифры — писать: "Имя не может состоять из цифр!".
        elif name.isdigit():
            text_hello.value = "Имя не может состоять только из цифр!"
            text_hello.color = ft.Colors.RED_900

        # 5) Валидация: Запретить добавлять в список имена короче 2-х символов.
        elif len(name) < 2:
            text_hello.value = "Имя не должно быть короче 2 символов!"
            text_hello.color = ft.Colors.RED_900

        else:
            text_hello.value = f"Привет! {name}"
            text_hello.color = ft.Colors.BLUE
            
            # greeting_history.append(name) - без бонуса
            # Бонусное задание: Сделать так, чтобы новое имя добавлялось не в конец списка (вниз), а в начало (вверх)
            greeting_history.insert(0, name)


            # 1) В списке истории должно храниться не более 5 последних имен. Если добавляется 6-е, самое старое (первое) должно удаляться из списка.
            if len(greeting_history) > 5:
                greeting_history.pop()
                # greeting_history.pop(0) - без бонуса

            update_history_view()
            text_input.value = ""

        page.update()

    def thememode(e):
        page.theme_mode = (
            ft.ThemeMode.DARK 
            if page.theme_mode == ft.ThemeMode.LIGHT 
            else ft.ThemeMode.LIGHT
        )
        page.update()

    def clear_history(e):
        greeting_history.clear()
        update_history_view()
        page.update()

    btn = ft.ElevatedButton('Send', on_click=text_name)
    theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)


    # 4) Интерфейс: Использовать Column для всей страницы и Row для кнопок.
    # Разместить кнопку переключения темы и кнопку очистки в одном ряду в верхней части экрана.
    top_row = ft.Row(
        controls=[theme_btn, clear_button],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    main_row = ft.Row(
        controls=[text_input, btn],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(ft.Column(controls=[top_row, text_hello, main_row, greeting_text]))

ft.app(main_page)