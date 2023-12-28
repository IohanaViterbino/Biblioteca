from controller.tablet import TabletController

if __name__=='__main__':
    print('Adicionando')   
    TabletController.post("Apple", "iPad Pro", "256GB", "iOS")
    TabletController.post("Samsung", "Galaxy Tab S7", "128GB", "Android")
    TabletController.post("Microsoft", "Surface Pro 7", "512GB", "Windows")
    TabletController.post("Samsung", "Galaxy Tab S7", "8 GB", "Android")
    TabletController.post("Apple", "iPad Air", "64 GB", "iOS")
    TabletController.post("Lenovo", "Tab P11", "6 GB", "Android")
    TabletController.post("Microsoft", "Surface Go 2", "4 GB", "Windows")
    TabletController.post("Huawei", "MatePad Pro", "6 GB", "Android")
        
    print("Listando")
    for tb in TabletController.get_tablets():
        print(tb)
    
    print("Buscar")
    print(TabletController.get_tablet(1))

    print('Apagando')
    # TabletController.excluirTablet(4)