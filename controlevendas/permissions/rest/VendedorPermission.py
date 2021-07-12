from rest_framework import permissions

class VendedorPermission(permissions.BasePermission):
	message = 'Você não possui permissão específica para acesso'

	def has_permission(self, request, view):
		if request.user.groups.filter(name="grupo_vendedor").exists():
			return True
		return False 