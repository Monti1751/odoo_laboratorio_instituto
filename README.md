# 🧪 Lab Inventory Management - Odoo 17

Sistema de gestión de inventario para laboratorios educativos desarrollado como módulo personalizado para Odoo 17 Community Edition.

---

## 📦 Módulos incluidos

Este repositorio contiene **dos módulos** que trabajan juntos:

### `lab_setup` — Configuración de Laboratorio
Configura automáticamente toda la estructura del laboratorio al instalarse:
- ✅ Crea las categorías de producto: **Reactivos Químicos** y **Equipos de Laboratorio**
- ✅ Crea la jerarquía de ubicaciones del almacén (Mueble 1/2, Armarios A/B, Área de Equipos)
- ✅ Añade campos personalizados al formulario de producto (fórmula química, CAS, pureza, densidad, etc.)
- ✅ Crea el modelo de **historial de uso de equipos** con auto-completado de usuario, fecha y hora
- ✅ Añade pestañas condicionales en el formulario de producto según su categoría

### `lab_consumo` — Consumo de Reactivos
Gestiona el registro de consumo de reactivos de laboratorio:
- ✅ Registro de consumo por reactivo, cantidad y alumno
- ✅ Descuento automático de stock mediante movimientos de inventario
- ✅ Estados: Borrador → Consumido
- ✅ Validación de stock disponible antes de consumir

---

## 🚀 Instalación

### Requisitos
- Odoo 17 Community Edition
- Python 3.10+
- Módulos base de Odoo: `stock`, `product`

### Pasos

1. **Copia los módulos** al directorio `custom_addons` de tu instancia Odoo:
```bash
cd /opt/odoo/custom_addons
git clone https://github.com/Monti1751/odoo_laboratorio_instituto.git
```
Esto dejará disponibles las carpetas `lab_setup` y `lab_consumo` dentro de `Lab_Consumo/opt/odoo/custom_addons/`.

2. **Configura permisos** (Linux):
```bash
sudo chown -R odoo:odoo lab_setup lab_consumo
```

3. **Reinicia el servidor Odoo**:
```bash
sudo systemctl restart odoo
```

4. **Activa el modo desarrollador** en Odoo:
   - Ve a **Ajustes → Activar modo desarrollador**

5. **Actualiza la lista de módulos**:
   - Ve a **Aplicaciones → Actualizar lista de aplicaciones**

6. **Instala los módulos** en este orden:
   1. Busca **"Configuración de Laboratorio"** (`lab_setup`) → Instalar
   2. Busca **"Consumo de Reactivos de Laboratorio"** (`lab_consumo`) → Instalar

> **Nota:** Instala `lab_setup` primero, ya que crea las categorías y ubicaciones que usarás al trabajar con `lab_consumo`.

---

## ✅ Qué se configura automáticamente al instalar `lab_setup`

### Categorías de producto
| Categoría | Descripción |
|---|---|
| Reactivos Químicos | Para productos químicos del laboratorio |
| Equipos de Laboratorio | Para instrumentos y equipos |

### Ubicaciones de almacén
```
Laboratorio Principal
├── Mueble 1
│   ├── Armario A
│   └── Armario B
├── Mueble 2
│   ├── Armario A
│   └── Armario B
└── Área de Equipos
```

### Campos personalizados en productos

**Reactivos Químicos** (pestaña "Información Reactiva"):

| Campo | Tipo | Descripción |
|---|---|---|
| Fórmula química | Texto | Fórmula molecular (ej: H₂SO₄) |
| CAS | Texto | Número de registro CAS |
| Pureza | Texto | Nivel de pureza (ej: 99%) |
| Estado de agregación | Selección | Sólido / Líquido / Gaseoso |
| Densidad | Decimal | En g/cm³ |
| Punto de fusión | Decimal | En °C |
| Punto de ebullición | Decimal | En °C |
| Pictogramas de peligrosidad | Texto | Símbolos GHS |
| Fecha de caducidad | Fecha | Vencimiento del reactivo |
| Fecha de apertura | Fecha | Primer uso |
| Advertencia de seguridad | Texto largo | Se muestra como banner rojo |

**Equipos de Laboratorio** (pestaña "Información Equipo"):

| Campo | Tipo | Descripción |
|---|---|---|
| Código del equipo | Texto | Identificador único |
| Función | Texto largo | Descripción del uso |
| Próximo mantenimiento | Fecha | Mantenimiento programado |
| Observaciones | Texto largo | Notas generales |
| Historial de uso | Tabla | Registro automático de usos |

### Historial de uso de equipos
Cuando un usuario añade una fila al historial de uso de un equipo, los siguientes campos se completan automáticamente:
- **Usuario** → usuario de Odoo que crea el registro
- **Fecha** → fecha actual
- **Hora** → hora actual (formato 24h)

**Permisos:**
- Usuarios normales: pueden crear y ver registros, pero no eliminarlos
- Administradores: control total

---

## 📖 Uso

### Gestionar Reactivos
1. Ve a **Inventario → Productos → Crear**
2. Asigna la categoría **Reactivos Químicos**
3. La pestaña **"Información Reactiva"** aparecerá automáticamente
4. Completa los campos de identificación, propiedades físicas y seguridad

### Gestionar Equipos
1. Ve a **Inventario → Productos → Crear**
2. Asigna la categoría **Equipos de Laboratorio**
3. La pestaña **"Información Equipo"** aparecerá automáticamente
4. Completa código, función y mantenimiento
5. Usa la tabla **"Historial de Uso"** para registrar cada uso del equipo

### Registrar consumo de reactivos
1. Ve a **Laboratorio → Consumo → Crear**
2. Selecciona el reactivo, la cantidad y el alumno
3. Haz clic en **"Consumir"** para descontar el stock automáticamente

---

## ⚙️ Configuración manual (opcional)

Si prefieres configurar el sistema manualmente en lugar de usar `lab_setup`, puedes hacerlo desde la interfaz de Odoo:

### Crear categorías de producto
1. Ve a **Inventario → Configuración → Categorías de producto**
2. Crea manualmente: `Reactivos Químicos` y `Equipos de Laboratorio`

### Configurar ubicaciones de almacén
1. Ve a **Inventario → Configuración → Ubicaciones**
2. Crea la jerarquía indicada arriba de forma manual

### Añadir campos personalizados
1. Ve a **Ajustes → Técnico → Estructura de la Base de Datos → Modelos**
2. Busca `product.template` y añade los campos con prefijo `x_` indicados en las tablas anteriores

### Crear la vista heredada
1. Ve a **Ajustes → Técnico → Interfaz de Usuario → Vistas**
2. Crea una vista con modelo `product.template`, heredando de `product.template.product.form`
3. Añade las pestañas condicionales en XML

> **Recomendación:** Usa el módulo `lab_setup` para evitar toda esta configuración manual.

---

## 🗂️ Estructura del repositorio

```
odoo_laboratorio_instituto/
└── Lab_Consumo/
    └── opt/
        └── odoo/
            └── custom_addons/
                ├── lab_setup/              ← Módulo de configuración
                │   ├── __manifest__.py
                │   ├── models/
                │   │   ├── lab_equipment_usage.py
                │   │   └── product_template.py
                │   ├── data/
                │   │   ├── product_category_data.xml
                │   │   └── stock_location_data.xml
                │   ├── views/
                │   │   └── product_template_views.xml
                │   └── security/
                │       └── ir.model.access.csv
                └── lab_consumo/            ← Módulo de consumo
                    ├── __manifest__.py
                    ├── models/
                    │   └── consumo_reactivo.py
                    ├── views/
                    │   └── consumo_reactivo_views.xml
                    └── security/
                        └── ir.model.access.csv
```

---

## 📝 Licencia

Este proyecto está bajo la Licencia LGPL-3.0.

## 👨‍💻 Autores

- [Fran Montesinos](https://github.com/Monti1751)
- [Ashley Barrionuevo](https://github.com/Ashley2411)
- [Miguel Duque](https://github.com/El-Mig)
- [David Cruces](https://github.com/davcruman)
