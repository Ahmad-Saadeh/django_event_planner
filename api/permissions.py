from rest_framework.permissions import BasePermission

class IsEventOwner(BasePermission):
	message = "You must be the owner of this booking"

	def has_object_permission(self, request, view, obj):
		if obj.booker == request.user:
			return True
		else:
			return False
