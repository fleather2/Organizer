from django.urls import path
from . import views
from . import apps

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),

    path('ideas', views.ideas, name="ideas"),
    path('removeIdea/<slug:idea>', views.removeIdea),

    path('todos', views.todos),
    path('removeTodo/<slug:todo>', views.removeTodo),
    path('toggleTodoCompleted/<slug:todo>', views.toggleTodoCompleted),

    path('calendar', views.calendar),
]
