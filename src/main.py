import flet as ft
from database import Database

def main(page: ft.Page):
    page.title = "Список фильмов"
    page.window.width = 1024

    database = Database("movies.db")
    database.create_tables()

   
    title_input = ft.TextField(label="Название фильма")
    
    genre_input = ft.TextField(label="Жанр")
    year_input = ft.TextField(label="Год выхода")

    movie_list_area = ft.Column(expand=True, scroll="always")

  
    def build_rows():
        rows = []
        for movie in database.get_all_movies():
            rows.append(
                ft.Row(
                    controls=[
                        ft.Text(value=movie[1], size=20),  
                        ft.Text(value=movie[2], size=20), 
                        ft.Text(value=movie[3], size=20), 
                    
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINED,
                            icon_color=ft.Colors.RED,
                            icon_size=20,
                            on_click=delete_movie,
                            data=movie[0],  
                        ),
                    ]
                )
            )
        return rows

   
    def add_movie(e):
        database.add_movie(title_input.value, genre_input.value, year_input.value)
        movie_list_area.controls = build_rows()
        title_input.value = ""
        genre_input.value = ""
        year_input.value = ""
        title_input.focus()
        page.update()

    
    def delete_movie(e):
        movie_id = e.control.data
        database.delete_movie(movie_id)
        movie_list_area.controls = build_rows()
        page.update()

   
    add_button = ft.ElevatedButton(
        text="Добавить",
        on_click=add_movie,
        color=ft.Colors.PINK,
        bgcolor=ft.Colors.AMBER,
    )

  
    input_area = ft.Row(controls=[title_input, genre_input, year_input, add_button])

 
    page.add(
        ft.Text(value="Список фильмов", size=30, weight=ft.FontWeight.BOLD),
        input_area,
        movie_list_area,
    )

    movie_list_area.controls = build_rows()
    page.update()

ft.app(target=main)
