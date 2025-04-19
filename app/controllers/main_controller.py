class MainController:
    def __init__(self, model):
        self.model = model

    def load_data(self):
        return self.model.fetch_records()

    def render_view(self, data):
        from app.views.main_view import render_main_view
        render_main_view(data)