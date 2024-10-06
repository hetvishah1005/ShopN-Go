from django.urls import path  # Import the path function to define URL patterns
from . import views  # Import views from the current app

# Set a namespace for the URL patterns of this app
app_name = 'myapp'

# URL patterns for the myapp application
urlpatterns = [
    path('', views.index, name='index'),  # URL for the index view (home page)

    path('about/', views.about, name='about'),  # URL for the about page

    # URL pattern that includes year and month for the about view
    # Example: http://127.0.0.1:8000/about/2024/12/
    path('about/<int:year>/<int:month>/', views.about, name='about_with_date'),

    # URL pattern for viewing details of a specific type based on its ID
    # Example: http://127.0.0.1:8000/1/ (replace 1 with the actual type ID)
    path('<int:type_no>/', views.detail, name='detail'),

    # URL pattern for the sample Function-Based View (FBV)
    path('sample_fbv/', views.sample_fbv, name='sample_fbv'),

    # URL pattern for the sample Class-Based View (CBV)
    path('sample_cbv/', views.SampleCBV.as_view(), name='sample_cbv'),
]
