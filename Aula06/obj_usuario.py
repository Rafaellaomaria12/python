from classe_usuario import usuario

admin = usuario("admin","P@$$w0rd","Administrador")
admin.login("admin","P@$$w0rd")
admin.alterar_senha("admin","123")
admin.login("admin","123")