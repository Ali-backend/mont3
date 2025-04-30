import flet as ft


def main(page: ft.Page)
    page.title = "Расходы"
    Title = ft.Text("Ваши расходы", size=30)
    products=[]
    Expenses = ft.Text("Общая сумма расходов: ")
    total_cost = ft.Text("0")


    def save(e):
        name = first_input.value
        cost = second_input.value
        if not cost.isdigit():
            print("Введите  число")
        elif int(cost) < 1:
            print("Число должно быть положительным")
        cost = int(cost)
        total = int(total_cost.value) + cost
        total_cost.value = total
        products.append(f"{name}: {cost}")
        list_area.controls = [ft.Text(value=product)for product in products]

        page.update()


        
#    def on_change(event):
 #       print(input.value)
  #      if input.value.lower() in friends_list:
  #          print(f"Друг {input.value} найден")

    first_input = ft.TextField(label="Введите название товара", )
    second_input = ft.TextField(label="Введите сумму товара", )
    
    button = ft.ElevatedButton("Сохронить", on_click=save)

    list_area = ft.Colunn
    page.add(Title, 
            first_input,
            second_input, 
            button,
            list_area,
            ft.Row([Expenses, total_cost])
    
    )

ft.app(main)