from app.controllers.main_controller import MainController

def main():
    controller = MainController()
    controller.load_data()
    controller.render_view()

if __name__ == "__main__":
    main()