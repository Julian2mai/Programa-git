from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

def generar_recibo(productos, nombre_archivo="recibo.pdf"):
    doc = SimpleDocTemplate(nombre_archivo, pagesize=letter)
    elementos = []
    estilos = getSampleStyleSheet()
    estilo_titulo = estilos['Heading1']
    estilo_titulo.alignment = TA_CENTER
    estilo_normal = estilos['Normal']
    estilo_normal.alignment = TA_CENTER
    
    # Nombre de la tienda
    elementos.append(Paragraph("Tienda de Mairongo", estilo_titulo))
    elementos.append(Spacer(1, 12))
    
    # Título del recibo
    elementos.append(Paragraph("RECIBO", estilo_normal))
    elementos.append(Spacer(1, 12))
    
    # Tabla de productos
    datos_tabla = [["Producto", "Precio", "Cantidad", "Total"]]
    total_general = 0
    
    for producto in productos:
        nombre = producto['nombre']
        precio = producto['precio']
        cantidad = producto['cantidad']
        total = precio * cantidad
        total_general += total
        datos_tabla.append([nombre, f"{precio:.2f} ", str(cantidad), f"{total:.2f} "])
    
    tabla_productos = Table(datos_tabla)
    tabla_productos.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elementos.append(tabla_productos)
    elementos.append(Spacer(1, 12))
    
    # Total general
    elementos.append(Paragraph(f"Total General: {total_general:.2f} ", estilo_normal))
    elementos.append(Spacer(1, 24))
    
    # Firma
    elementos.append(Paragraph("Gracias por su compra", estilo_normal))
    elementos.append(Paragraph("Mairongo", estilo_normal))
    
    # Generar PDF
    doc.build(elementos)

def main():
    productos = []
    while True:
        nombre = input("Ingrese el nombre del producto : ")
        if nombre.lower() == 'fin':
            break
        
        while True:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                total = precio * cantidad
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el precio.")
        
        productos.append({
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
        })
    
    nombre_archivo = input("Ingrese el nombre del archivo PDF (por defecto 'recibo.pdf'): ")
    if not nombre_archivo:
        nombre_archivo = "Recibo.pdf"
    
    generar_recibo(productos, nombre_archivo)
    print(f"Recibo generado como {nombre_archivo}")

if __name__ == "__main__":
    main()