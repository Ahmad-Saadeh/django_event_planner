from django.urls import path
from .views import Login, Logout, Signup, home,event_list, create_event, event_detail, event_update, dashboard, my_list,booking
from api.views import ListView,ListEventsView,Register, UpdateView, EventCreateView, BookEventList, Book, EventUsers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
#from events import views
urlpatterns = [
	path('', home, name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
	path('list/', event_list, name='event-list'),
	path('create/', create_event, name='create-event'),
	path('detail/<int:event_id>',event_detail, name='event-detail'),
	path('update/<int:event_id>', event_update, name='event-update'),
	path('dashboard/', dashboard, name='dashboard'),
	path('my_list/', my_list,name='my-list'),
	path('booking/<int:event_id>', booking,name='event-book'),


# API paths
	path('api/list/', ListView.as_view(), name='api-list'),
	path('api/organizer-events/', ListEventsView.as_view(), name='api-event-list'),
	path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('api/register/', Register.as_view(), name="register"),
    path('api/update/<int:object_id>', UpdateView.as_view(), name='api-update'),
    path('api/create/', EventCreateView.as_view(), name='api-create'),
    path('api/booked-events/', BookEventList.as_view(), name='api-event-book'),
    path('api/book/', Book.as_view(), name='book'),
    path('api/events/<int:event_id>/bookings/', EventUsers.as_view(), name='users')


]
