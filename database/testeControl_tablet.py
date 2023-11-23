from controller.tablet import AdicionarTablet, ListarTablet, BuscarTablet

if __name__=='__main__':
    print('Adicionando')   
    AdicionarTablet.post("Apple", "iPad Pro", "256GB", "iOS")
    AdicionarTablet.post("Samsung", "Galaxy Tab S7", "128GB", "Android")
    AdicionarTablet.post("Microsoft", "Surface Pro 7", "512GB", "Windows")
    AdicionarTablet.post("Samsung", "Galaxy Tab S7", "8 GB", "Android")
    AdicionarTablet.post("Apple", "iPad Air", "64 GB", "iOS")
    AdicionarTablet.post("Lenovo", "Tab P11", "6 GB", "Android")
    AdicionarTablet.post("Microsoft", "Surface Go 2", "4 GB", "Windows")
    AdicionarTablet.post("Huawei", "MatePad Pro", "6 GB", "Android")
        
    print("Listando")
    ListarTablet.get()
    
    print("Buscar")
    BuscarTablet.get(1)

    print('Apagando')
    # Apagar.get(4)
    # Listar.get()