import flet as ft
from db.connection import initialize_database
from ui.login_pages import login_page, registration_page, registration_success_page
from ui.home import home_page
from ui.onboarding_pages import show_loading

def main(page: ft.Page):
    page.title = "Plateful App"
    page.window_resizable = False  # Disable resizing
    page.window_width = 390  # Mobile width
    page.window_height = 844  # Mobile height
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.ORANGE_800,
            secondary=ft.Colors.RED_600,
            background=ft.Colors.WHITE,
            on_primary=ft.Colors.BLACK,
        )
    )

    # print("AB")
    # Initialize the database (creates tables if not already created)
    try:
        initialize_database()
    except Exception as e:
        print(f"Database initialization error: {e}")

    # print("A")
    # Function to navigate to different views
    def navigate_to(page, view):
        page.clean()
        if view == "welcome":
            page.add(show_loading(page, navigate_to))  # Add the returned content
        elif view == "login":
            page.add(login_page(page, navigate_to))
        elif view == "register":
            page.add(registration_page(page, navigate_to))
        elif view == "registration-success":
            page.add(registration_success_page(page, navigate_to))
        elif view == "home":
            page.add(home_page(page))
        page.update()

    # Start with the login view
    navigate_to(page, "login")

# print("AC")
ft.app(target=main, view=ft.AppView.FLET_APP_WEB)