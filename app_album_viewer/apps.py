from django.apps import AppConfig


class AlbumViewerConfig(AppConfig):
    # Specifies the default auto field type for the models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    # Specifies the name of the app
    name = 'app_album_viewer'
