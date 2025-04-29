import flet as ft


def main(page: ft.Page):
    page.title = "My first app"
    friends_list=["маша","саша","даша"]

    def on_change(event):
        print(input.value)
        if input.value.lower() in friends_list:
            print(f"Друг {input.value} найден")

    input = ft.TextField(label="Введите текст", on_change-on_change)
    
    page.add(input

    )


ft.app(main)
