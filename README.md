# 🧪 Lab Inventory Management - Odoo 17

Sistema de gestión de inventario para laboratorios educativos desarrollado como módulo para Odoo 17 Community Edition.

## 📋 Características

### Gestión de Reactivos Químicos
- ✅ Información detallada: fórmula química, CAS, pureza
- ✅ Propiedades físicas: densidad, punto de fusión/ebullición, estado de agregación
- ✅ Gestión de seguridad: pictogramas de peligrosidad
- ✅ Control de fechas: caducidad y apertura
- ✅ Clasificación por ubicación (muebles y armarios)

### Gestión de Equipos de Laboratorio
- ✅ Código de identificación y función del equipo
- ✅ Control de mantenimiento preventivo
- ✅ Historial completo de uso con tracking automático
- ✅ Registro de usuario, fecha y hora de cada uso
- ✅ Sistema de permisos diferenciados (usuarios vs administradores)

### Sistema de Historial de Uso
- ✅ Auto-completado de usuario, fecha y hora al crear registros
- ✅ Permisos configurables: usuarios solo pueden crear, administradores pueden editar
- ✅ Exportación de datos para reportes mensuales
- ✅ Trazabilidad completa del uso de equipos

## 🚀 Instalación

### Requisitos
- Odoo 17 Community Edition
- Python 3.10+
- Módulos base: `stock`, `product`

### Pasos de instalación

1. Clona el repositorio en tu directorio de addons:
```bash
cd /path/to/odoo/addons
git clone https://github.com/tu-usuario/lab-inventory-odoo.git lab_inventory
```

2. Reinicia el servicio de Odoo:
```bash
sudo systemctl restart odoo
```

3. Actualiza la lista de aplicaciones en Odoo:
   - Ve a **Aplicaciones** (modo desarrollador activado)
   - Clic en **Actualizar lista de aplicaciones**

4. Busca e instala el módulo "Inventario"

## ⚙️ Configuración

### Crear categorías de producto

1. Ve a **Inventario > Configuración > Categorías de producto**
2. Crea las siguientes categorías:
   - `Reactivos Químicos`
   - `Equipos de Laboratorio`

### Configurar ubicaciones de almacén

Estructura recomendada:
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

### Configuración de Campos Personalizados

### Campos para Reactivos Químicos

Ve a **Ajustes > Técnico > Estructura de la Base de Datos > Modelos** y busca `product.template`. Añade estos campos personalizados (con prefijo `x_`):

| Campo | Nombre técnico | Tipo | Descripción |
|-------|---------------|------|-------------|
| Fórmula química | `x_formula_quimica` | Char (Texto) | Fórmula molecular del reactivo |
| CAS | `x_CAS` | Char (Texto) | Número de registro CAS |
| Pureza | `x_pureza` | Char o Selection | Nivel de pureza (99%, 95%, etc.) |
| Estado de agregación | `x_estado_de_agregacion` | Selection | Sólido/Líquido/Gaseoso |
| Densidad | `x_densidad` | Float (Decimal) | Densidad en g/cm³ |
| Punto de fusión | `x_punto_de_fusion` | Float (Decimal) | Temperatura en °C |
| Punto de ebullición | `x_punto_de_ebullicion` | Float (Decimal) | Temperatura en °C |
| Pictogramas de peligrosidad | `x_pictograma_de_peligrosidad` | Char o Many2many | Símbolos de seguridad |
| Fecha de caducidad | `x_fecha_de_caducidad` | Date (Fecha) | Fecha de vencimiento |
| Fecha de apertura | `x_fecha_de_apertura` | Date (Fecha) | Fecha de primer uso |
|Advertencia de Seguridad| `x_advertencia_seguridad`|Char (Texto)|Advertencias de uso para el reactivo|

### Campos para Equipos de Laboratorio

En el mismo modelo `product.template`, añade:

| Campo | Nombre técnico | Tipo | Descripción |
|-------|---------------|------|-------------|
| Código del equipo | `x_codigo_equipo` | Char (Texto) | Identificador único |
| Función | `x_funcion` | Text (Texto largo) | Descripción del uso del equipo |
| Próximo mantenimiento | `x_proximo_mantenimiento` | Date (Fecha) | Fecha programada de mantenimiento |
| Observaciones | `x_observaciones` | Text (Texto largo) | Notas generales |

### Modelo de Historial de Uso

Crea un nuevo modelo `x_lab_equipment_usage` con estos campos:

| Campo | Nombre técnico | Tipo | Modelo relacionado |
|-------|---------------|------|-------------------|
| Equipo | `x_product_id` | Many2one | `product.template` |
| Usuario | `x_usuario_id` | Many2one | `res.users` |
| Fecha de uso | `x_fecha_uso` | Date | - |
| Hora | `x_hora_uso` | Char | - |
| Observaciones | `x_observaciones` | Text | - |

## 🤖 Configurar campos calculados automáticos (Historial de Uso)

Para que los campos de usuario, fecha y hora se completen automáticamente al crear un registro de uso, configura campos calculados:

### Configuración en el modelo `x_lab_equipment_usage`

Ve a **Ajustes > Técnico > Estructura de la Base de Datos > Modelos** y abre el modelo `x_lab_equipment_usage`.

#### Campo: Usuario automático (`x_usuario_id`)

1. Edita el campo `x_usuario_id`
2. En la sección **"Propiedades avanzadas"**:
   - **Dependencias**: `x_product_id`
   - **Calcular**:
```python
for record in self:
    if not record.x_usuario_id:
        record['x_usuario_id'] = self.env.user.id
```
3. Marca **"Almacenado"**: ✅
4. Guarda

#### Campo: Fecha automática (`x_fecha_uso`)

1. Edita el campo `x_fecha_uso`
2. En la sección **"Propiedades avanzadas"**:
   - **Dependencias**: `x_product_id`
   - **Calcular**:
```python
for record in self:
    if not record.x_fecha_uso:
        record['x_fecha_uso'] = datetime.date.today()
```
3. Marca **"Almacenado"**: ✅
4. Guarda

#### Campo: Hora automática (`x_hora_uso`)

1. Edita el campo `x_hora_uso`
2. En la sección **"Propiedades avanzadas"**:
   - **Dependencias**: `x_product_id`
   - **Calcular**:
```python
for record in self:
    if not record.x_hora_uso:
        record['x_hora_uso'] = datetime.datetime.now().strftime('%H:%M')
```
3. Marca **"Almacenado"**: ✅
4. Guarda

### ✅ Resultado

Ahora cuando un usuario cree un nuevo registro de uso:
- El campo **Usuario** se completará automáticamente con el usuario actual
- El campo **Fecha** se completará con la fecha actual
- El campo **Hora** se completará con la hora actual (formato 24h)

> **Nota**: Los campos aparecen como de solo lectura en la vista (con `readonly="1"`), pero los administradores pueden editarlos si es necesario accediendo directamente al registro.

Luego añade en `product.template`:

| Campo | Nombre técnico | Tipo | Configuración |
|-------|---------------|------|---------------|
| Historial de uso | `x_equipment_usage_ids` | One2many | Modelo: `x_lab_equipment_usage`<br>Campo: `x_product_id` |

### Campos Nativos de Odoo (ya disponibles)

No es necesario crear estos campos, ya están incluidos en Odoo:

- **Nombre**: Campo nativo del producto
- **Cantidad**: Gestionado automáticamente por Odoo
- **Proveedor/Marca**: Usa la pestaña "Compra" del producto
- **Localización**: Usa las ubicaciones de almacén jerárquicas

## 📝 Editar vistas directamente (sin Studio)

Puedes personalizar las vistas editándolas manualmente. Es un poco más técnico pero no es difícil:

### Método: Heredar la vista del formulario de producto

#### Paso 1: Inspecciona la vista del producto (opcional)

1. Ve a **Inventario > Productos**
2. Abre cualquier producto
3. Con el modo desarrollador activo, verás un **icono de bug 🐛** en la parte superior
4. Clic en él y selecciona **"Editar vista: Formulario"**
5. Verás el XML de la vista actual (solo para referencia)
6. ⚠️ **NO edites directamente esta vista** (es la original del sistema)

#### Paso 2: Crea una vista heredada

1. Ve a **Ajustes > Técnico > Interfaz de Usuario > Vistas**
2. Clic en **"Crear"**
3. Completa los campos:
   - **Nombre de la vista**: `product.template.form.lab.custom`
   - **Modelo**: `product.template`
   - **Vista heredada**: Busca y selecciona `product.template.product.form`
   - **Modo**: `Extension` (Extensión)

#### Paso 3: Añade el código XML en Arquitectura

> ⚠️ **Importante**: Verifica los IDs de tus categorías antes de pegar el código. Para obtenerlos, abre cada categoría y mira la URL:
> - `http://127.0.0.1:8069/web#id=9&...` → El ID es **9**
> - Reactivos Químicos: ID **9**
> - Equipos de Laboratorio: ID **10**

Pega este código en el campo **"Arquitectura"**:

``` xml
<xpath expr="//notebook" position="inside">
    <!-- Pestaña para REACTIVOS QUÍMICOS -->
    <page string="Información Reactiva" attrs="{'invisible': [('categ_id', 'in', [9])]}">
        
        <!-- Banner de advertencia solo para reactivos -->
        <div class="alert alert-danger" role="alert" style="margin: 10px 0 20px 0; padding: 20px; border-left: 5px solid #721c24;" attrs="{'invisible': [('x_advertencia_seguridad', '=', False)]}">
            <div style="display: flex; align-items: center; gap: 15px;">
                <i class="fa fa-exclamation-triangle fa-3x" style="color: #721c24;"/>
                <div style="flex: 1;">
                    <h3 style="margin: 0 0 10px 0; color: #721c24;">
                        ADVERTENCIA DE SEGURIDAD
                    </h3>
                    <field name="x_advertencia_seguridad" nolabel="1" readonly="1"/>
                </div>
            </div>
        </div>
        
        <group>
            <group string="Identificación">
                <field name="x_formula_quimica"/>
                <field name="x_CAS"/>
                <field name="x_pureza"/>
                <field name="x_pictograma_de_peligrosidad"/>
            </group>
            <group string="Propiedades Físicas">
                <field name="x_estado_de_agregacion"/>
                <field name="x_densidad"/>
                <field name="x_punto_de_fusion"/>
                <field name="x_punto_de_ebullicion"/>
            </group>
            <group string="Fechas">
                <field name="x_fecha_de_caducidad"/>
                <field name="x_fecha_de_apertura"/>
            </group>
            <group string="Seguridad">
                <field name="x_advertencia_seguridad" placeholder="Ingrese advertencias de seguridad para este reactivo..."/>
            </group>
        </group>
    </page>
    
    <!-- Pestaña para EQUIPOS DE LABORATORIO -->
    <page string="Información Equipo" attrs="{'invisible': [('categ_id', 'in', [10])]}">
        <group>
            <group string="Identificación del Equipo">
                <field name="x_codigo_equipo"/>
                <field name="x_funcion"/>
            </group>
            <group string="Mantenimiento">
                <field name="x_proximo_mantenimiento"/>
                <field name="x_observaciones"/>
            </group>
        </group>
        
        <separator string="Historial de Uso del Equipo"/>
        <field name="x_equipment_usage_ids" nolabel="1" colspan="2">
            <tree string="Registros de Uso" editable="top">
                <field name="x_fecha_uso" string="Fecha" readonly="1" force_save="1"/>
                <field name="x_hora_uso" string="Hora" readonly="1" force_save="1"/>
                <field name="x_usuario_id" string="Usuario" readonly="1" force_save="1"/>
                <field name="x_observaciones" string="Observaciones"/>
            </tree>
        </field>
    </page>
</xpath>
```

#### Paso 4: Guarda y verifica

1. Clic en **"Guardar"**
2. Recarga la página (Ctrl + Shift + R)
3. Abre un producto y verifica:
   - Si es de categoría "Reactivos Químicos" → aparece pestaña "Información Reactiva"
   - Si es de categoría "Equipos de Laboratorio" → aparece pestaña "Información Equipo"

### 🔧 Ajustar IDs de categorías

Si tus categorías tienen IDs diferentes (no son 9 y 10), modifica estas líneas en el XML:

- `attrs="{'invisible': [('categ_id', 'in', [10])]}"` → Cambia **10** por el ID de "Equipos de Laboratorio"
- `attrs="{'invisible': [('categ_id', 'in', [9])]}"` → Cambia **9** por el ID de "Reactivos Químicos"

### ✅ Resultado

Las pestañas personalizadas aparecerán automáticamente según la categoría asignada al producto, mostrando solo los campos relevantes para cada tipo.

### Configurar permisos de usuarios

1. Crea el grupo "Usuarios de Laboratorio" (opcional)
2. Asigna usuarios estudiantes a este grupo
3. Los administradores mantienen el grupo "Administración / Ajustes"

## 🚀 Instalación del Módulo `lab_consumo`

Para instalar este módulo en una instancia de Odoo (Local o Servidor), sigue estos pasos:

### 1. Descargar el código
Accede a la terminal de tu servidor Odoo y navega hasta tu carpeta de `custom_addons`. Luego, clona el repositorio:
https://github.com/El-Mig
```bash
cd /opt/odoo/custom_addons
git clone [https://github.com/Monti1751/odoo_laboratorio_instituto.git](https://github.com/Monti1751/odoo_laboratorio_instituto.git) lab_consumo
```
### 2. Configurar permisos
Asegúrate de que Odoo tenga permisos para leer la nueva carpeta:
```
sudo chown -R odoo:odoo lab_consumo
```
### 3. Reiniciar el servicio
Para que Odoo detecte los nuevos archivos Python, debes reiniciar el servidor:
```
sudo systemctl restart odoo
```
### 4. Activar el módulo en la interfaz de Odoo

1. Entra en Odoo con tu usuario administrador.

2. Activa el Modo Desarrollador (Ajustes > Activar modo desarrollador).

3. Ve al menú Aplicaciones.

4. En la barra superior, haz clic en Actualizar lista de aplicaciones y confirma en el botón "Actualizar".

5. Quita el filtro de "Aplicaciones" de la barra de búsqueda, busca lab_consumo e instálalo.

### 🛠️ Requisitos previos
Para que el módulo funcione correctamente, asegúrate de tener instalados los siguientes módulos oficiales:

- Inventario (stock): Necesario para gestionar los movimientos de los reactivos.
- Contactos (base): Para asociar alumnos a los consumos.
   
## 📖 Uso

### Gestionar Reactivos

1. Crea un nuevo producto
2. Asigna la categoría "Reactivos Químicos"
3. La pestaña "Información Reactiva" aparecerá automáticamente
4. Completa los campos: fórmula química, CAS, pureza, etc.

### Gestionar Equipos

1. Crea un nuevo producto
2. Asigna la categoría "Equipos de Laboratorio"
3. Completa código, función y próximo mantenimiento
4. El historial de uso se registra automáticamente

### Registrar uso de equipos

Los estudiantes pueden:
- Crear nuevos registros de uso (usuario, fecha y hora se autocompletan)
- Añadir observaciones sobre el uso

Los administradores pueden:
- Editar cualquier registro existente
- Modificar fecha, hora o usuario si es necesario

## 🗂️ Estructura del proyecto
```
lab_inventory/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── product_template.py
├── views/
│   └── product_template_views.xml
├── security/
│   └── ir.model.access.csv
└── README.md
```

## 📝 Licencia

Este proyecto está bajo la Licencia LGPL-3.0 - ver el archivo LICENSE para más detalles.

## 👨‍💻 Autor

[Fran Montesinos] - [Monti1751](https://github.com/Monti1751)

[Ashley Barrionuevo] - [Ashley2411](https://github.com/Ashley2411)

[Miguel Duque] - [El-Mig](https://github.com/El-Mig)

[David Cruces] - [davcruman](https://github.com/davcruman)

## 🙏 Agradecimientos

- Comunidad Odoo
- [Cualquier recurso o persona que quieras agradecer]
