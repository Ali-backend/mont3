import flet as ft


def main(page: ft.Page)
    page.title = "My first app"
    friends=[]

    def save(e):
        friend = {"name": first_input.value, "age": second_input.value}
        friends.append(friend)
        print(friend)

#    def on_change(event):
 #       print(input.value)
  #      if input.value.lower() in friends_list:
  #          print(f"Друг {input.value} найден")

    first_input = ft.TextField(label="Введите имя", )
    second_input = ft.TextField(label="Введите возрост", )
    
    button = ft.ElevatedButton("Добавить", on_click=save)
    page.add(first_input,second_input, button
    
    )

ft.app(main)