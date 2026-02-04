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

4. Busca e instala el módulo "Inventario de Laboratorio"

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

### Configurar permisos de usuarios

1. Crea el grupo "Usuarios de Laboratorio" (opcional)
2. Asigna usuarios estudiantes a este grupo
3. Los administradores mantienen el grupo "Administración / Ajustes"

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

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia LGPL-3.0 - ver el archivo LICENSE para más detalles.

## 👨‍💻 Autor

[Tu Nombre] - [Tu Email/GitHub]

## 🙏 Agradecimientos

- Comunidad Odoo
- [Cualquier recurso o persona que quieras agradecer]
