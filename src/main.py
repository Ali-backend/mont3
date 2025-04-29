import flet as ft

#"""friends - [
 #   {"name": "Билли", "age": 18},
 #   {"name": "Стив", "age": 15}
#]"""


def main(page: ft.Page):
    page.title = "Расходы"
    Title = ft.Text("Ваши расходы", size=30, italic=True)
    products = []
    Expenses = ft.Text("Общая сумма расходов:", size=30)
    total_cost = ft.Text("0", size=30)

    def save(e)
        name = first_input.value
        cost = second_input.value
        if not cost.isdigit():
            print("Введите число")
        elif int(cost) < 1:
            print("Число должно быть роложительным")    
        cost = int(cost)
        total = int(total_cost.value) + cost
        total_cost.value = total
        list_area.controls.append(
            ft.Row(
                controls=[
                    ft.Text(name),
                    ft.Text(cost, color=get_color(cost)),
                    ft.IconButton(ft.Icons.EDIT, icon_color=ft.colors.PINK),
                    ft.IconButton(ft.Icons.DELETE, icon_color=ft.colors.PINK)
                ]
            )
        )

        page.update()
        

 #   def on_change(event):
 #       print(input.value)
 #       if input.value.lower() in friends_list:
  #          print(f"Друг {input.value} найден")

    
    first_input = ft.TextField(label="Введите  названние товара", )
    second_input = ft.TextField(label="Введите сумму товара", )

    button = ft.ElevatedButton("Сохронять", on_click=save)

    list_area = ft.Colunn.expand=(True, scroll="always")
    page.add(Title,
             ft.Row([first_input, 
             second_input, 
             button]), 
             ft.Row([Expenses, total_cost])
             list_area

    )


ft.app(main)
