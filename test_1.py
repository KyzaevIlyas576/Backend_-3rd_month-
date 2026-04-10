# задания 3-4
import flet as ft
import datetime as dtt

def main_page(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    greeting_history = []

    greeting_text = ft.Text('История заполнения:')

    def text_name(e):
        name = text_input.value.strip()
        time_now = dtt.datetime.now().hour


        if name:
            text_hello.value = f"{'Доброе утро' if 0 <= time_now <= 11 else 'Добрый вечер'}, {name}!"
            text_hello.color = ft.Colors.BLUE
            text_input.value = ""
            greeting_history.append((name, time_now))
            # greeting_text.value = f'История приветствия: \n' + "\n".join(greeting_history)
            greeting_history.append((name, hour))
            greeting_history[:] = greeting_history[-5:]     # обрезаем историю
        

        else:
            text_hello.value = "Введите корректное имя!" 
            text_hello.color = ft.Colors.RED_900

        page.update()



    def thememode(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        
        page.update()


    text_hello = ft.Text('Как тебя зовут?', size=20)
    text_input = ft.TextField(label='Ваше имя', on_submit=text_name, expand=False)
    btn = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=text_name)


    theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)


    def update_history(data):
        greeting_text.value = f'История приветствия: \n' + "\n".join([f"{name} ({hour}:00)" for name, hour in data])
        # 'История приветствия: <новая строка>' + "<новая строка> (+ имя и <час:00>) за каждые имя и час в data"


    def show_morning(e):
        morning = [(name, hour) for name, hour in greeting_history if hour < 12]
        update_history(morning)
        page.update()


    def show_evening(e):
        evening = [(name, hour) for name, hour in greeting_history if hour >= 12]
        update_history(evening)
        page.update()
        

    def show_all(e):
        update_history(greeting_history)
        page.update()
    

    def clear_history(e):
        greeting_history.clear()
        greeting_text.value = "История приветствия:"
        page.update()

    
    morning_button = ft.ElevatedButton('утренние', icon=ft.Icons.SUNNY, on_click=show_morning)
    evening_button = ft.ElevatedButton('вечерние', icon=ft.Icons.NIGHT_SHELTER, on_click=show_evening)
    all_button = ft.ElevatedButton('все', icon=ft.Icons.VISIBILITY, on_click=show_all)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    

    main_object = ft.Row(
        controls=[text_input, btn, clear_button],
        alignment=ft.MainAxisAlignment.CENTER
        ) 

    page.add(text_hello, main_object, theme_btn, ft.Row([morning_button, evening_button, all_button], alignment=ft.MainAxisAlignment.CENTER), greeting_text)


ft.app(main_page, view=ft.AppView.WEB_BROWSER)
