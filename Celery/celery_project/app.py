from celery import Celery

app = Celery('celery_project', include=["celery_project.task"])
app.config_from_object("celery_project.celeryconfig")


