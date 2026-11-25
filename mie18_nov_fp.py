'''
lista_prod=[
    {'nombre':'',
     'stock':'',
     'precio':'',
     'reponer':False}
]
'''

lista_productos=[]

nombre=''
stock=0
precio=0

def menu():
    print('========== MENÚ PRINCIPAL ==========')
    print('1. Agregar producto')
    print('2. Buscar producto')
    print('3. Eliminar producto')
    print('4. Actualizar reposición')
    print('5. Mostrar productos')
    print('6. Salir')
    print('=====================================')

def opt_menu():
    while True:
        try:
            opt=int(input('Ingrese una opción: '))
            if opt>=1 and opt<=6:
                return opt
            else:
                print('Error, debes ingresar una opción entre el 1 y 6.')
        except ValueError:
            print('Error, debes ingresar un número entero.')

def validar_nombre(nombre):
    return len(nombre.strip())>0

def validar_stock(stock):
    return stock>=0

def validar_precio(precio):
    return precio>0

def agregar_producto(lista_productos):
    nombre=input(('Ingrese el nombre del producto a agregar: ').strip()).lower()
    if not validar_nombre(nombre):
        print(f'Error, el campo "nombre" no puede estar vacío.')
        return
    else:
        try:
            stock=int(input(f'Ingrese el stock para el producto {nombre}: '))
            if not validar_stock(stock):
                print('Error, el stock debe ser mayor o igual a 0.')
                return
            else:
                try:
                    precio=float(input(f'Ingrese el precio unitario para el producto {nombre}: '))
                    if not validar_precio(precio):
                        print('Error, el precio debe ser un número mayor que 0.')
                    else:
                        producto={
                            'nombre':nombre.strip(),
                            'stock':stock,
                            'precio':precio,
                            'reponer':False
                            }
                        lista_productos.append(producto)
                        print(f'Producto "{producto['nombre']}" agregado con éxito.')
                except ValueError:
                    print('Error, el precio debe ser un número decimal válido.')
        except ValueError:
            print('Error, el stock debe ser un valor numérico entero.')

def buscar_producto(lista_productos, nombre_buscar):
    for i in range(len(lista_productos)):
        if lista_productos[i]['nombre']==nombre_buscar:
            return i
    return -1

def actualizar_reposicion(lista_productos):
    for producto in lista_productos:
        if producto['stock']<5:
            producto['reponer']=True
        else:
            producto['reponer']=False

def main():
    productos=[]

    while True:
        menu()
        opt=opt_menu()

        if opt==1:
            agregar_producto(productos)
        elif opt==2:
            nombre=input('Ingrese el nombre del producto a buscar: ')
            pos=buscar_producto(productos,nombre)
            if pos>-1:
                p=productos[pos]
                estado_txt='reponer' if p['reponer'] else 'Stock ok'
                print(f'\nProducto encontrado en la posición {pos}:')
                print(f'nombre: {p['nombre']} | Stock: {p['stock']} | Precio: {p['precio']}')
            else:
                print(f'El producto {nombre} no se encuentra registrado.')
        elif opt==3:
            nombre=input('Ingrese el nombre del producto a eliminar: ')
            pos=buscar_producto(productos,nombre)
            if pos!=-1:
                eliminado=productos.pop(pos)
            else:
                print(f'El producto {nombre} no se encuentra registrado.')
        elif opt==4:
            actualizar_reposicion(productos)
            print('Estado  de reposición actualziado correctamente.')
        elif opt==5:
            actualizar_reposicion(productos)
            print(f'\n=== LISTA DE PRODUCTOS ===')
            if len(productos)==0:
                print('No hay productos registrados.')
            else:
                valor_total=0.0
                for p in productos:
                    estado_txt='reponer' if p['reponer'] else 'stock ok'
                    print(f'Nombre: {p['nombre']}')
                    print(f'Stock: {p['stock']}')
                    print(f'Precio: {p['precio']}')
                    print(f'Estado: {p['estado_txt']}')
                    print('*********************************************')
                    valor_total+=p['stock']*p['precio']
                print(f'Valor total inventario: ${valor_total:.2f}')
        elif opt==6:
            print('Gracias por usar el sistema, vuelva pronto.')
            break
main()



