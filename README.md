# Inventory Manager — Acceptance Test Workshop

## Descripción
Aplicación de línea de comandos para gestionar un inventario de productos
(agregar, listar, actualizar cantidades, eliminar y limpiar el inventario),
probada con **Behave**

## Estructura del proyecto
```
inventory_manager/
├── inventory.py                     # Lógica principal
├── features/
│   ├── add_product.feature          # Feature 1
│   ├── list_products.feature        # Feature 2
│   ├── update_quantity.feature      # Feature 3
│   ├── remove_product.feature       # Feature 4
│   ├── clear_inventory.feature      # Feature 5
│   └── steps/
│       └── inventory_steps.py       # Definición de los pasos
└── README.md
```
## Funcionalidades (Features)

1. Agregar un producto al inventario.
2. Listar todos los productos.
3. Actualizar la cantidad de un producto.
4. Eliminar un producto del inventario.
5. **Vaciar completamente el inventario**.

## Cómo ejecutar

```bash
pip install behave
python3 inventory.py     # ejecuta la aplicación interactiva
behave                   # ejecuta las pruebas de aceptación
```