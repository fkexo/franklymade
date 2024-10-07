class MyAppRouter:
    """
    A router to control database operations on models in different apps.
    Directs queries to either the local database or the remote one.
    """

    def db_for_read(self, model, **hints):
        """Direct read operations."""
        if model._meta.app_label == 'api':
            return 'remote'  # Reads from remote database for the 'api' app
        return 'default'  # Reads from the local database for everything else

    def db_for_write(self, model, **hints):
        """Direct write operations."""
        if model._meta.app_label == 'api':
            return 'remote'  # Writes to remote database for the 'api' app
        return 'default'  # Writes to local database for everything else

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if a model is in both databases."""
        if obj1._meta.app_label == 'api' and obj2._meta.app_label == 'api':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that models only appear in the appropriate database."""
        if app_label == 'api':
            return db == 'remote'  # Migrate 'api' models to the remote database
        return db == 'default'  # Migrate other apps to the local database
