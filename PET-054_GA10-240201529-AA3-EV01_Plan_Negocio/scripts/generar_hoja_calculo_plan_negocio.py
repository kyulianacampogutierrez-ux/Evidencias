#!/usr/bin/env python3
# ==============================================================================
# GENERADOR DE HOJA DE CÁLCULO PROFESIONAL PLAN DE NEGOCIO Y ESTADOS FINANCIEROS
# Evidencia: GA10-240201529-AA3-EV01 - Plan de negocio
# Competencia: 240201529 - Gestionar procesos propios de la cultura emprendedora
# Actividad: GA10-240201529-AA3 - Establecer el modelo de negocio del emprendimiento
# Emprendimiento: Pizzería Gourmet Bella Italia Popayán
# Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | CTPI Popayán - Regional Cauca
# ==============================================================================

import os
import subprocess
import shutil

BASE_DIR = '/home/danilo/Escritorio/Karen/SENA/CDE/Evidencias/PET-054_GA10-240201529-AA3-EV01_Plan_Negocio'
HOJA_DIR = os.path.join(BASE_DIR, 'hoja_calculo')
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
ENTREGA_DIR = '/home/danilo/Escritorio/Karen/SENA/ENTREGA_ZAJUNA_GA10-240201529-AA3-EV01'
ENTREGA_HOJA_DIR = os.path.join(ENTREGA_DIR, 'hoja_calculo')

os.makedirs(HOJA_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(ENTREGA_HOJA_DIR, exist_ok=True)

xml_file_path = os.path.join(HOJA_DIR, 'GA10-240201529-AA3-EV01_Plan_Negocio.xml')

# Helper to escape XML
def xe(text):
    if text is None:
        return ""
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

with open(xml_file_path, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<?mso-application progid="Excel.Sheet"?>\n')
    f.write('<Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet"\n')
    f.write(' xmlns:o="urn:schemas-microsoft-com:office:office"\n')
    f.write(' xmlns:x="urn:schemas-microsoft-com:office:excel"\n')
    f.write(' xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet"\n')
    f.write(' xmlns:html="http://www.w3.org/TR/REC-html40">\n')
    
    # Document Properties
    f.write(' <DocumentProperties xmlns="urn:schemas-microsoft-com:office:office">\n')
    f.write('  <Title>Plan de Negocio y Estados Financieros - Pizzería Bella Italia Popayán</Title>\n')
    f.write('  <Subject>Evidencia GA10-240201529-AA3-EV01</Subject>\n')
    f.write('  <Author>Karen Yuliana Campo</Author>\n')
    f.write('  <Company>SENA CTPI Popayán - Regional Cauca</Company>\n')
    f.write(' </DocumentProperties>\n')
    
    # Styles
    f.write(' <Styles>\n')
    f.write('  <Style ss:ID="Default" ss:Name="Normal">\n')
    f.write('   <Alignment ss:Vertical="Center"/>\n')
    f.write('   <Borders/>\n')
    f.write('   <Font ss:FontName="Calibri" ss:Size="10" ss:Color="#0F172A"/>\n')
    f.write('   <Interior ss:Color="#FFFFFF" ss:Pattern="Solid"/>\n')
    f.write('   <NumberFormat/>\n')
    f.write('   <Protection/>\n')
    f.write('  </Style>\n')
    
    # Header Styles
    f.write('  <Style ss:ID="TituloPrincipal">\n')
    f.write('   <Alignment ss:Horizontal="Center" ss:Vertical="Center" ss:WrapText="1"/>\n')
    f.write('   <Font ss:FontName="Calibri" ss:Size="14" ss:Bold="1" ss:Color="#FFFFFF"/>\n')
    f.write('   <Interior ss:Color="#047857" ss:Pattern="Solid"/>\n')
    f.write('  </Style>\n')
    
    f.write('  <Style ss:ID="SubtituloVerde">\n')
    f.write('   <Alignment ss:Horizontal="Center" ss:Vertical="Center"/>\n')
    f.write('   <Font ss:FontName="Calibri" ss:Size="11" ss:Bold="1" ss:Color="#065F46"/>\n')
    f.write('   <Interior ss:Color="#D1FAE5" ss:Pattern="Solid"/>\n')
    f.write('   <Borders>\n')
    f.write('    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#10B981"/>\n')
    f.write('    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#10B981"/>\n')
    f.write('    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#10B981"/>\n')
    f.write('    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#10B981"/>\n')
    f.write('   </Borders>\n')
    f.write('  </Style>\n')

    f.write('  <Style ss:ID="EncabezadoTabla">\n')
    f.write('   <Alignment ss:Horizontal="Center" ss:Vertical="Center" ss:WrapText="1"/>\n')
    f.write('   <Font ss:FontName="Calibri" ss:Size="10" ss:Bold="1" ss:Color="#FFFFFF"/>\n')
    f.write('   <Interior ss:Color="#0F766E" ss:Pattern="Solid"/>\n')
    f.write('   <Borders>\n')
    f.write('    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#042F2E"/>\n')
    f.write('    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#14B8A6"/>\n')
    f.write('    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#042F2E"/>\n')
    f.write('    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#042F2E"/>\n')
    f.write('   </Borders>\n')
    f.write('  </Style>\n')

    f.write('  <Style ss:ID="EncabezadoAzul">\n')
    f.write('   <Alignment ss:Horizontal="Center" ss:Vertical="Center" ss:WrapText="1"/>\n')
    f.write('   <Font ss:FontName="Calibri" ss:Size="10" ss:Bold="1" ss:Color="#FFFFFF"/>\n')
    f.write('   <Interior ss:Color="#1E40AF" ss:Pattern="Solid"/>\n')
    f.write('   <Borders>\n')
    f.write('    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#1E3A8A"/>\n')
    f.write('    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#3B82F6"/>\n')
    f.write('    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#1E3A8A"/>\n')
    f.write('    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#1E3A8A"/>\n')
    f.write('   </Borders>\n')
    f.write('  </Style>\n')

    f.write('  <Style ss:ID="FilaDatoTexto">\n')
    f.write('   <Alignment ss:Horizontal="Left" ss:Vertical="Center"/>\n')
    f.write('   <Font ss:FontName="Calibri" ss:Size="9.5" ss:Color="#0F172A"/>\n')
    f.write('   <Interior ss:Color="#FFFFFF" ss:Pattern="Solid"/>\n')
    f.write('   <Borders>\n')
    f.write('    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('   </Borders>\n')
    f.write('  </Style>\n')

    f.write('  <Style ss:ID="FilaDatoCentro">\n')
    f.write('   <Alignment ss:Horizontal="Center" ss:Vertical="Center"/>\n')
    f.write('   <Font ss:FontName="Calibri" ss:Size="9.5" ss:Color="#0F172A"/>\n')
    f.write('   <Interior ss:Color="#FFFFFF" ss:Pattern="Solid"/>\n')
    f.write('   <Borders>\n')
    f.write('    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('   </Borders>\n')
    f.write('  </Style>\n')

    f.write('  <Style ss:ID="FilaDatoMoneda">\n')
    f.write('   <Alignment ss:Horizontal="Right" ss:Vertical="Center"/>\n')
    f.write('   <Font ss:FontName="Calibri" ss:Size="9.5" ss:Color="#0F172A"/>\n')
    f.write('   <Interior ss:Color="#FFFFFF" ss:Pattern="Solid"/>\n')
    f.write('   <NumberFormat ss:Format="$#,##0"/>\n')
    f.write('   <Borders>\n')
    f.write('    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('   </Borders>\n')
    f.write('  </Style>\n')

    f.write('  <Style ss:ID="FilaDatoPorc">\n')
    f.write('   <Alignment ss:Horizontal="Right" ss:Vertical="Center"/>\n')
    f.write('   <Font ss:FontName="Calibri" ss:Size="9.5" ss:Color="#0F172A"/>\n')
    f.write('   <Interior ss:Color="#FFFFFF" ss:Pattern="Solid"/>\n')
    f.write('   <NumberFormat ss:Format="0.0%"/>\n')
    f.write('   <Borders>\n')
    f.write('    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('   </Borders>\n')
    f.write('  </Style>\n')

    f.write('  <Style ss:ID="FilaTotal">\n')
    f.write('   <Alignment ss:Horizontal="Right" ss:Vertical="Center"/>\n')
    f.write('   <Font ss:FontName="Calibri" ss:Size="10" ss:Bold="1" ss:Color="#0F172A"/>\n')
    f.write('   <Interior ss:Color="#F1F5F9" ss:Pattern="Solid"/>\n')
    f.write('   <NumberFormat ss:Format="$#,##0"/>\n')
    f.write('   <Borders>\n')
    f.write('    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#94A3B8"/>\n')
    f.write('    <Border ss:Position="Bottom" ss:LineStyle="Double" ss:Weight="3" ss:Color="#0F172A"/>\n')
    f.write('    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#CBD5E1"/>\n')
    f.write('   </Borders>\n')
    f.write('  </Style>\n')

    f.write('  <Style ss:ID="CardHeader">\n')
    f.write('   <Alignment ss:Horizontal="Center" ss:Vertical="Center"/>\n')
    f.write('   <Font ss:FontName="Calibri" ss:Size="11" ss:Bold="1" ss:Color="#FFFFFF"/>\n')
    f.write('   <Interior ss:Color="#047857" ss:Pattern="Solid"/>\n')
    f.write('  </Style>\n')

    f.write('  <Style ss:ID="CardValue">\n')
    f.write('   <Alignment ss:Horizontal="Center" ss:Vertical="Center"/>\n')
    f.write('   <Font ss:FontName="Calibri" ss:Size="14" ss:Bold="1" ss:Color="#065F46"/>\n')
    f.write('   <Interior ss:Color="#DCFCE7" ss:Pattern="Solid"/>\n')
    f.write('   <Borders>\n')
    f.write('    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="2" ss:Color="#10B981"/>\n')
    f.write('    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#10B981"/>\n')
    f.write('    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#10B981"/>\n')
    f.write('    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#10B981"/>\n')
    f.write('   </Borders>\n')
    f.write('  </Style>\n')

    f.write(' </Styles>\n')

    # ==============================================================================
    # HOJA 1: PORTADA Y GENERALIDADES
    # ==============================================================================
    f.write(' <Worksheet ss:Name="01_Portada_Generalidades">\n')
    f.write('  <Table ss:DefaultColumnWidth="100">\n')
    f.write('   <Column ss:Width="30"/>\n')
    f.write('   <Column ss:Width="200"/>\n')
    f.write('   <Column ss:Width="320"/>\n')
    f.write('   <Column ss:Width="160"/>\n')
    f.write('   <Column ss:Width="160"/>\n')
    
    # Filas de Portada
    f.write('   <Row ss:Height="25">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="3" ss:StyleID="TituloPrincipal"><Data ss:Type="String">SERVICIO NACIONAL DE APRENDIZAJE - SENA | REGIONAL CAUCA</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="20">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="3" ss:StyleID="SubtituloVerde"><Data ss:Type="String">CENTRO DE TELEINFORMÁTICA Y PRODUCCIÓN INDUSTRIAL (CTPI) - FICHA 3186681</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="15"/>\n')
    
    info_portada = [
        ("PROGRAMA DE FORMACIÓN", "Tecnólogo en Análisis y Desarrollo de Software (ADSO)"),
        ("COMPETENCIA", "240201529 - Gestionar procesos propios de la cultura emprendedora y empresarial"),
        ("ACTIVIDAD DE APRENDIZAJE", "GA10-240201529-AA3: Establecer el modelo de negocio del emprendimiento a partir de las necesidades"),
        ("EVIDENCIA DE APRENDIZAJE", "GA10-240201529-AA3-EV01: Plan de negocio (Estados Financieros Proyectados)"),
        ("APRENDIZ", "Karen Yuliana Campo - C.C. 1.061.789.012"),
        ("EMPRENDIMIENTO", "Pizzería Gourmet Bella Italia Popayán"),
        ("UBICACIÓN DEL PROYECTO", "Calle 4 # 7-45, Centro Histórico, Popayán, Cauca"),
        ("MODELO DE FINANCIACIÓN", "Fondo Emprender SENA ($80M) + Recursos Propios ($30M) + Microcrédito ($10M)"),
        ("FECHA DE PRESENTACIÓN", "Noviembre 2026")
    ]
    for campo, valor in info_portada:
        f.write('   <Row ss:Height="20">\n')
        f.write(f'    <Cell ss:Index="2" ss:StyleID="EncabezadoAzul"><Data ss:Type="String">{xe(campo)}</Data></Cell>\n')
        f.write(f'    <Cell ss:MergeAcross="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(valor)}</Data></Cell>\n')
        f.write('   </Row>\n')
        
    f.write('   <Row ss:Height="20"/>\n')
    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="3" ss:StyleID="SubtituloVerde"><Data ss:Type="String">RESUMEN EJECUTIVO Y PARÁMETROS MACROECONÓMICOS DEL PROYECTO</Data></Cell>\n')
    f.write('   </Row>\n')

    resumen_kpi = [
        ("Capital Total Inicial Requerido", "$ 120.000.000 COP", "100.0%", "Inversión en activos, adecuaciones y capital de trabajo"),
        ("Aporte Fondo Emprender SENA", "$ 80.000.000 COP", "66.7%", "Capital no reembolsable condonable (4 empleos verificables)"),
        ("Aporte Propio Karen Campo", "$ 30.000.000 COP", "25.0%", "Ahorros y capital líquido familiar"),
        ("Microcrédito Bancario de Fomento", "$ 10.000.000 COP", "8.3%", "Banco Agrario / Línea Joven Emprendedor 24 meses"),
        ("Ventas Proyectadas Año 1", "$ 310.500.000 COP", "-", "6.760 pizzas + acompañamientos + catering + mayorista"),
        ("Costo Total de Ventas (CMV)", "$ 94.200.000 COP", "30.3%", "Materia prima gourmet, harinas italianas y quesos caucanos"),
        ("Margen de Contribución Total", "$ 216.300.000 COP", "69.7%", "Margen bruto operativo para absorción de costos fijos"),
        ("Gastos de Personal Anual (4 Empleos)", "$ 131.864.952 COP", "42.5%", "100% formalidad laboral: cesantías, primas, pensión, ARL"),
        ("Utilidad Neta Proyectada Año 1", "$ 14.767.238 COP", "4.8%", "Utilidad neta después de impuestos régimen SIMPLE (20%)"),
        ("Punto de Equilibrio en Ventas", "$ 283.846.416 COP", "91.4%", "Ventas mínimas para no incurrir en pérdidas operacionales"),
        ("Punto de Equilibrio en Unidades", "7.096 Unidades/año", "-", "591 unidades/mes = 19.7 unidades diarias"),
        ("Retorno sobre la Inversión (ROI)", "12.31% anual", "-", "Rentabilidad sobre capital total invertido"),
        ("Periodo de Recuperación (Payback)", "2.8 años", "-", "Retorno neto mediante flujo de caja libre")
    ]
    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="EncabezadoTabla"><Data ss:Type="String">CONCEPTO / INDICADOR</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">VALOR PROYECTADO</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">PARTICIPACIÓN</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">OBSERVACIÓN TÉCNICA</Data></Cell>\n')
    f.write('   </Row>\n')
    for conc, val, part, obs in resumen_kpi:
        f.write('   <Row ss:Height="20">\n')
        f.write(f'    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(conc)}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoCentro"><Data ss:Type="String">{xe(val)}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoCentro"><Data ss:Type="String">{xe(part)}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(obs)}</Data></Cell>\n')
        f.write('   </Row>\n')
        
    f.write('  </Table>\n')
    f.write(' </Worksheet>\n')

    # ==============================================================================
    # HOJA 2: PRESUPUESTO DE VENTAS, SERVICIOS Y VENTAS AL POR MAYOR (PASO 1 GUÍA 10)
    # ==============================================================================
    f.write(' <Worksheet ss:Name="02_Presupuesto_Ventas">\n')
    f.write('  <Table ss:DefaultColumnWidth="90">\n')
    f.write('   <Column ss:Width="30"/>\n')
    f.write('   <Column ss:Width="220"/>\n')
    f.write('   <Column ss:Width="100"/>\n')
    f.write('   <Column ss:Width="110"/>\n')
    f.write('   <Column ss:Width="110"/>\n')
    f.write('   <Column ss:Width="110"/>\n')
    f.write('   <Column ss:Width="90"/>\n')
    f.write('   <Column ss:Width="130"/>\n')
    f.write('   <Column ss:Width="130"/>\n')
    f.write('   <Column ss:Width="130"/>\n')
    
    f.write('   <Row ss:Height="25">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="8" ss:StyleID="TituloPrincipal"><Data ss:Type="String">PASO 1: PRESUPUESTO DE VENTAS, SERVICIOS Y VENTAS AL POR MAYOR (AÑO 1)</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="18">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="8" ss:StyleID="SubtituloVerde"><Data ss:Type="String">Proyección de ingresos, costeo de materias primas, servicios de catering y ventas al por mayor B2B</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="10"/>\n')

    f.write('   <Row ss:Height="24">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="EncabezadoTabla"><Data ss:Type="String">LÍNEA DE PRODUCTO / SERVICIO</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">UNIDADES AÑO 1</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">PRECIO UNITARIO (PVP)</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">COSTO VAR. UNITARIO</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">MARGEN CONTRIB. UNIT.</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">% MARGEN</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">INGRESOS TOTALES</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">COSTO VARIABLE TOTAL</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">MARGEN TOTAL</Data></Cell>\n')
    f.write('   </Row>\n')

    # Lineas de producto
    productos = [
        ("Pizza Tradicional Gourmet (35cm)", 3200, 38000, 11400),
        ("Pizza Especial Gourmet / Trufada", 2100, 48000, 14880),
        ("Acompañamientos (Focaccias / Dips)", 1800, 14000, 4200),
        ("Bebidas Artesanales e Italianas", 3500, 8500, 2550),
        ("Servicio Catering & Horno Móvil (Eventos)", 18, 1200000, 440000),
        ("Ventas Mayoristas B2B (Bases Precocidas)", 2100, 5500, 2100)
    ]
    
    total_ing = 0
    total_cost = 0
    total_marg = 0

    for idx, (nom, cant, pvp, c_unit) in enumerate(productos, start=5):
        m_unit = pvp - c_unit
        pct_m = m_unit / pvp
        ing_tot = cant * pvp
        cost_tot = cant * c_unit
        marg_tot = ing_tot - cost_tot
        
        total_ing += ing_tot
        total_cost += cost_tot
        total_marg += marg_tot
        
        f.write('   <Row ss:Height="20">\n')
        f.write(f'    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(nom)}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoCentro"><Data ss:Type="Number">{cant}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{pvp}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{c_unit}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda" ss:Formula="=RC[-2]-RC[-1]"><Data ss:Type="Number">{m_unit}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoPorc" ss:Formula="=RC[-1]/RC[-3]"><Data ss:Type="Number">{round(pct_m, 4)}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda" ss:Formula="=RC[-5]*RC[-4]"><Data ss:Type="Number">{ing_tot}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda" ss:Formula="=RC[-6]*RC[-4]"><Data ss:Type="Number">{cost_tot}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda" ss:Formula="=RC[-2]-RC[-1]"><Data ss:Type="Number">{marg_tot}</Data></Cell>\n')
        f.write('   </Row>\n')

    # Fila de Totales
    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="FilaTotal"><Data ss:Type="String">TOTAL CONSOLIDADO AÑO 1</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-6]C:R[-1]C)"><Data ss:Type="Number">12718</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal"><Data ss:Type="String">-</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal"><Data ss:Type="String">-</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal"><Data ss:Type="String">-</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=RC[3]/RC[1]"><Data ss:Type="Number">{round(total_marg/total_ing, 4)}</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-6]C:R[-1]C)"><Data ss:Type="Number">{total_ing}</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-6]C:R[-1]C)"><Data ss:Type="Number">{total_cost}</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-6]C:R[-1]C)"><Data ss:Type="Number">{total_marg}</Data></Cell>\n')
    f.write('   </Row>\n')
    
    # Análisis Detallado Guía 10
    f.write('   <Row ss:Height="20"/>\n')
    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="8" ss:StyleID="SubtituloVerde"><Data ss:Type="String">ANÁLISIS ESPECÍFICO EXIGIDO POR GUÍA DE APRENDIZAJE 10 (PÁG. 26)</Data></Cell>\n')
    f.write('   </Row>\n')
    
    analisis_guia = [
        ("PREGUNTA 1: ¿Cuál sería el valor de un servicio prestado?", 
         "En Bella Italia, el servicio no es solo venta en mostrador sino el 'Servicio de Estación Móvil y Catering para Eventos Sociales y Empresariales'. Cada servicio se cotiza en un paquete base de $1.200.000 COP para 30 comensales (15 pizzas familiares gourmet horneadas al instante con horno portátil refractario a gas/leña). Costo de materia prima e insumos: $380.000 COP + Transporte y logística: $60.000 COP = Costo variable total $440.000 COP. Margen de contribución: $760.000 COP (63.3%). Proyección: 18 eventos/año generando $21.600.000 COP de facturación de alto margen."),
        ("PREGUNTA 2: ¿Qué pasa si se vende al por mayor?", 
         "Bella Italia implementa una línea mayorista B2B de bases de pizza precocidas en horno de leña ultracongeladas al vacío para hoteles, cafés y restaurantes aliados de Popayán. Mientras una pizza terminada al detal tiene un PVP de $38.000, la base precocida mayorista se vende a $5.500 COP por unidad en paquetes de 50 unidades (descuento del 31.25% sobre valor base al público). Costo variable unitario: $2.100 COP (harina de fuerza, levadura, agua filtrada, aceite oliva virgen y termoencogible). Margen unitario: $3.400 COP (61.8%)."),
        ("IMPACTO FINANCIERO DE LA VENTA MAYORISTA", 
         "A) Maximiza la capacidad ociosa del horno y amasadora en horas de la mañana (9:00 am - 2:00 pm). B) Genera flujo de caja predecible y pedidos institucionales semanales. C) No requiere personal de servicio a la mesa ni vajilla. D) Aunque el margen porcentual es menor (61.8% vs 70.0%), aporta $7.140.000 COP directos de margen de contribución para absorber los costos fijos de nómina y arriendo."),
        ("ESTRUCTURA DE COSTOS FIJOS VS VARIABLES", 
         "Costos Variables: Materia prima directa (harina, queso mozzarella caucano, salsa pomodoro, embutidos, albahaca), empaques ecológicos biodegradables kraft, comisiones de pasarela POS digital Wompi (2.89%). Total: $94.200.000 COP anuales. Costos Fijos: Arriendo de sede ($30M), Nómina formal ($131.86M), Servicios públicos y leña certificada ($14.4M), Depreciaciones ($10.35M), Pauta digital ($3.6M) y Asesoría contable ($4.2M). Total Costos Fijos: $197.840.952 COP.")
    ]
    for preg, resp in analisis_guia:
        f.write('   <Row ss:Height="22">\n')
        f.write(f'    <Cell ss:Index="2" ss:MergeAcross="8" ss:StyleID="EncabezadoAzul"><Data ss:Type="String">{xe(preg)}</Data></Cell>\n')
        f.write('   </Row>\n')
        f.write('   <Row ss:Height="45">\n')
        f.write(f'    <Cell ss:Index="2" ss:MergeAcross="8" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(resp)}</Data></Cell>\n')
        f.write('   </Row>\n')
        
    f.write('  </Table>\n')
    f.write(' </Worksheet>\n')

    # ==============================================================================
    # HOJA 3: PRESUPUESTO DE PERSONAL Y PRESTACIONES DE LEY (PASO 2 GUÍA 10)
    # ==============================================================================
    f.write(' <Worksheet ss:Name="03_Presupuesto_Personal">\n')
    f.write('  <Table ss:DefaultColumnWidth="95">\n')
    f.write('   <Column ss:Width="30"/>\n')
    f.write('   <Column ss:Width="160"/>\n')
    f.write('   <Column ss:Width="60"/>\n')
    f.write('   <Column ss:Width="95"/>\n')
    f.write('   <Column ss:Width="85"/>\n')
    f.write('   <Column ss:Width="90"/>\n')
    f.write('   <Column ss:Width="80"/>\n')
    f.write('   <Column ss:Width="90"/>\n')
    f.write('   <Column ss:Width="80"/>\n')
    f.write('   <Column ss:Width="90"/>\n')
    f.write('   <Column ss:Width="70"/>\n')
    f.write('   <Column ss:Width="85"/>\n')
    f.write('   <Column ss:Width="110"/>\n')
    f.write('   <Column ss:Width="120"/>\n')

    f.write('   <Row ss:Height="25">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="12" ss:StyleID="TituloPrincipal"><Data ss:Type="String">PASO 2: PRESUPUESTO DE PERSONAL Y LIQUIDACIÓN PRESTACIONAL DE LEY (AÑO 1)</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="18">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="12" ss:StyleID="SubtituloVerde"><Data ss:Type="String">Estructura de nómina formal para 4 colaboradores directos (Fondo Emprender SENA / Código Sustantivo del Trabajo)</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="10"/>\n')

    f.write('   <Row ss:Height="25">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="EncabezadoTabla"><Data ss:Type="String">CARGO / ROL</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">CANT.</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">SUELDO BÁSICO</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">AUX. TRANSP.</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">CESANTÍAS (8.33%)</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">INT. CES. (1%)</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">PRIMA (8.33%)</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">VACAC. (4.17%)</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">PENSIÓN (12%)</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">ARL (1.044%)</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">CAJA COMP. (4%)</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">COSTO MENSUAL</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">COSTO ANUAL TOTAL</Data></Cell>\n')
    f.write('   </Row>\n')

    # Empleados: Cargo, cant, basico, aux_transp
    empleados = [
        ("Maestro Pizzero Chef", 1, 1900000, 162000),
        ("Auxiliar Cocina y Ensamble", 1, 1423500, 162000),
        ("Domiciliario Repartidor", 1, 1423500, 162000),
        ("Administradora / Líder ADSO", 1, 2200000, 0) # Supera 2 SMLMV
    ]

    tot_bas = 0
    tot_aux = 0
    tot_ces = 0
    tot_int = 0
    tot_pri = 0
    tot_vac = 0
    tot_pen = 0
    tot_arl = 0
    tot_caj = 0
    tot_mes = 0
    tot_ano = 0

    for cargo, cant, bas, aux in empleados:
        base_prest = bas + aux
        ces = round(base_prest * 0.08333)
        int_ces = round(ces * 0.12 / 12)
        pri = round(base_prest * 0.08333)
        vac = round(bas * 0.04167)
        pen = round(bas * 0.12)
        arl = round(bas * 0.01044)
        caj = round(bas * 0.04)
        
        c_mensual = bas + aux + ces + int_ces + pri + vac + pen + arl + caj
        c_anual = c_mensual * 12
        
        tot_bas += bas
        tot_aux += aux
        tot_ces += ces
        tot_int += int_ces
        tot_pri += pri
        tot_vac += vac
        tot_pen += pen
        tot_arl += arl
        tot_caj += caj
        tot_mes += c_mensual
        tot_ano += c_anual

        f.write('   <Row ss:Height="20">\n')
        f.write(f'    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(cargo)}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoCentro"><Data ss:Type="Number">{cant}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{bas}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{aux}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{ces}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{int_ces}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{pri}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{vac}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{pen}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{arl}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{caj}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda" ss:Formula="=SUM(RC[-9]:RC[-1])"><Data ss:Type="Number">{c_mensual}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda" ss:Formula="=RC[-1]*12"><Data ss:Type="Number">{c_anual}</Data></Cell>\n')
        f.write('   </Row>\n')

    # Total Personal
    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="FilaTotal"><Data ss:Type="String">TOTALES NÓMINA (4 EMPLEOS)</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal"><Data ss:Type="Number">4</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-4]C:R[-1]C)"><Data ss:Type="Number">{tot_bas}</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-4]C:R[-1]C)"><Data ss:Type="Number">{tot_aux}</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-4]C:R[-1]C)"><Data ss:Type="Number">{tot_ces}</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-4]C:R[-1]C)"><Data ss:Type="Number">{tot_int}</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-4]C:R[-1]C)"><Data ss:Type="Number">{tot_pri}</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-4]C:R[-1]C)"><Data ss:Type="Number">{tot_vac}</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-4]C:R[-1]C)"><Data ss:Type="Number">{tot_pen}</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-4]C:R[-1]C)"><Data ss:Type="Number">{tot_arl}</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-4]C:R[-1]C)"><Data ss:Type="Number">{tot_caj}</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-4]C:R[-1]C)"><Data ss:Type="Number">{tot_mes}</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-4]C:R[-1]C)"><Data ss:Type="Number">{tot_ano}</Data></Cell>\n')
    f.write('   </Row>\n')
    
    # Dotación y Observaciones
    f.write('   <Row ss:Height="20"/>\n')
    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="12" ss:StyleID="SubtituloVerde"><Data ss:Type="String">GASTOS ADICIONALES DE PERSONAL Y CUMPLIMIENTO CON FONDO EMPRENDER SENA</Data></Cell>\n')
    f.write('   </Row>\n')
    
    obs_personal = [
        ("Dotaciones y Ropa de Trabajo (Art. 230 CST)", "$ 2.400.000 COP / año", "3 entregas al año para los 3 cargos operativos (filipinas ignífugas, delantales de cuero, cofias y calzado antideslizante dieléctrico)."),
        ("Exoneración de Aportes a Salud (Ley 1607 / Art. 114-1 E.T.)", "0% aporte empleador", "Las microempresas están exoneradas del 8.5% de salud sobre trabajadores que devenguen menos de 10 SMLMV."),
        ("Compromiso de Condonación Fondo Emprender SENA", "4 Empleos Directos Verificados", "La generación de estos 4 empleos formales en Popayán es el indicador principal para que los $80.000.000 COP sean condonados 100% por el SENA."),
        ("Presupuesto Anual Total de Nómina y Bienestar", "$ 131.864.952 COP", "Consolida nómina básica ($83.3M), auxilio transporte ($5.8M), prestaciones ($26.4M), parafiscales ($14.0M) y dotaciones ($2.4M).")
    ]
    for c1, c2, c3 in obs_personal:
        f.write('   <Row ss:Height="20">\n')
        f.write(f'    <Cell ss:Index="2" ss:MergeAcross="2" ss:StyleID="EncabezadoAzul"><Data ss:Type="String">{xe(c1)}</Data></Cell>\n')
        f.write(f'    <Cell ss:MergeAcross="2" ss:StyleID="FilaDatoCentro"><Data ss:Type="String">{xe(c2)}</Data></Cell>\n')
        f.write(f'    <Cell ss:MergeAcross="7" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(c3)}</Data></Cell>\n')
        f.write('   </Row>\n')
        
    f.write('  </Table>\n')
    f.write(' </Worksheet>\n')

    # ==============================================================================
    # HOJA 4: ESTIMACIÓN DE ACTIVOS FIJOS Y DEPRECIACIÓN (PASO 3 GUÍA 10)
    # ==============================================================================
    f.write(' <Worksheet ss:Name="04_Activos_Fijos_Depreciacion">\n')
    f.write('  <Table ss:DefaultColumnWidth="95">\n')
    f.write('   <Column ss:Width="30"/>\n')
    f.write('   <Column ss:Width="160"/>\n')
    f.write('   <Column ss:Width="220"/>\n')
    f.write('   <Column ss:Width="50"/>\n')
    f.write('   <Column ss:Width="110"/>\n')
    f.write('   <Column ss:Width="120"/>\n')
    f.write('   <Column ss:Width="80"/>\n')
    f.write('   <Column ss:Width="90"/>\n')
    f.write('   <Column ss:Width="110"/>\n')
    f.write('   <Column ss:Width="110"/>\n')

    f.write('   <Row ss:Height="25">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="8" ss:StyleID="TituloPrincipal"><Data ss:Type="String">PASO 3: ESTIMACIÓN DE ACTIVOS FIJOS Y PLAN DE DEPRECIACIÓN ANUAL</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="18">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="8" ss:StyleID="SubtituloVerde"><Data ss:Type="String">Cuantificación de infraestructura operativa, tecnología y depreciación por línea recta (NIC 16)</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="10"/>\n')

    f.write('   <Row ss:Height="24">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="EncabezadoTabla"><Data ss:Type="String">CATEGORÍA</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">DESCRIPCIÓN DEL ACTIVO</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">CANT.</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">VALOR UNITARIO</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">VALOR TOTAL</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">VIDA ÚTIL</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">% DEPREC.</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">DEPREC. ANUAL</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">DEPREC. MENSUAL</Data></Cell>\n')
    f.write('   </Row>\n')

    activos = [
        ("Maquinaria y Equipo", "Horno Napolitano Refractario de Leña/Gas Híbrido", 1, 24000000, 10),
        ("Maquinaria y Equipo", "Amasadora Espiral Industrial 25 Kg Dos Velocidades", 1, 8500000, 10),
        ("Maquinaria y Equipo", "Mesa Refrigerada Pizza 3 Puertas con Vitrina GN", 1, 9200000, 10),
        ("Maquinaria y Equipo", "Refrigerador Vertical Acero Inox 2 Cuerpos", 1, 6500000, 10),
        ("Maquinaria y Equipo", "Rebanadora de Jamones y Laminadora de Masa", 1, 3800000, 10),
        ("Maquinaria y Equipo", "Campana Extractora y Sistema de Filtración Humos", 1, 4500000, 10),
        ("Cómputo y TI", "Servidor Local POS Touch All-in-One + Cajón Dinero", 1, 4200000, 5),
        ("Cómputo y TI", "Tabletas Android Rugerizadas Comanderas Meseros", 2, 900000, 5),
        ("Cómputo y TI", "Impresoras Térmicas Red Comandas Cocina y Factura", 2, 600000, 5),
        ("Cómputo y TI", "Router MikroTik Balanceador Dual-WAN + WiFi Clientes", 1, 800000, 5),
        ("Muebles y Enseres", "Juego de 8 Mesas y 32 Sillas Madera Estilo Trattoria", 1, 8000000, 10),
        ("Muebles y Enseres", "Barra de Despacho y Vitrina Mostrador Clientes", 1, 2500000, 10),
        ("Muebles y Enseres", "Estanterías Acero Inox para Fermentación y Almacén", 2, 1000000, 10),
        ("Muebles y Enseres", "Menaje Completo (Platos pizza, cubiertos, palas leña)", 1, 3500000, 10),
        ("Transporte y Logística", "Motocicleta 125cc con Baúl Térmico Calefactado 70°C", 1, 7500000, 5),
    ]

    tot_val_act = 0
    tot_dep_ano = 0
    tot_dep_mes = 0

    for cat, desc, cant, v_unit, vu in activos:
        v_tot = cant * v_unit
        pct_dep = 1.0 / vu
        d_ano = round(v_tot * pct_dep)
        d_mes = round(d_ano / 12)
        
        tot_val_act += v_tot
        tot_dep_ano += d_ano
        tot_dep_mes += d_mes

        f.write('   <Row ss:Height="20">\n')
        f.write(f'    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(cat)}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(desc)}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoCentro"><Data ss:Type="Number">{cant}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{v_unit}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda" ss:Formula="=RC[-2]*RC[-1]"><Data ss:Type="Number">{v_tot}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoCentro"><Data ss:Type="String">{vu} años</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoPorc"><Data ss:Type="Number">{pct_dep}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda" ss:Formula="=RC[-3]*RC[-1]"><Data ss:Type="Number">{d_ano}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda" ss:Formula="=RC[-1]/12"><Data ss:Type="Number">{d_mes}</Data></Cell>\n')
        f.write('   </Row>\n')

    # Total Activos
    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="3" ss:StyleID="FilaTotal"><Data ss:Type="String">SUBTOTAL ACTIVOS DEPRECIABLES</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-15]C:R[-1]C)"><Data ss:Type="Number">{tot_val_act}</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal"><Data ss:Type="String">-</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal"><Data ss:Type="String">-</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-15]C:R[-1]C)"><Data ss:Type="Number">{tot_dep_ano}</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-15]C:R[-1]C)"><Data ss:Type="Number">{tot_dep_mes}</Data></Cell>\n')
    f.write('   </Row>\n')
    
    # Adecuaciones Locativas (No depreciables directamente sino diferidas/amortizables en contrato de arriendo)
    f.write('   <Row ss:Height="20">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">Adecuaciones Locativas</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaDatoTexto"><Data ss:Type="String">Ductería chimenea, redes trifásicas, gas y enchapes sanitarios</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaDatoCentro"><Data ss:Type="Number">1</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">18500000</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">18500000</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaDatoCentro"><Data ss:Type="String">Amort. 5 años</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaDatoPorc"><Data ss:Type="Number">0.20</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">3700000</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">308333</Data></Cell>\n')
    f.write('   </Row>\n')
    
    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="3" ss:StyleID="FilaTotal"><Data ss:Type="String">TOTAL INVERSIÓN EN PLANTA Y EQUIPO + ADECUACIONES</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal"><Data ss:Type="Number">{tot_val_act + 18500000}</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal"><Data ss:Type="String">-</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal"><Data ss:Type="String">-</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal"><Data ss:Type="Number">{tot_dep_ano + 3700000}</Data></Cell>\n')
    f.write(f'    <Cell ss:StyleID="FilaTotal"><Data ss:Type="Number">{tot_dep_mes + 308333}</Data></Cell>\n')
    f.write('   </Row>\n')

    f.write('  </Table>\n')
    f.write(' </Worksheet>\n')

    # ==============================================================================
    # HOJA 5: CAPITAL INICIAL Y FUENTES DE FINANCIACIÓN (PASO 4 GUÍA 10)
    # ==============================================================================
    f.write(' <Worksheet ss:Name="05_Capital_Financiacion">\n')
    f.write('  <Table ss:DefaultColumnWidth="100">\n')
    f.write('   <Column ss:Width="30"/>\n')
    f.write('   <Column ss:Width="200"/>\n')
    f.write('   <Column ss:Width="130"/>\n')
    f.write('   <Column ss:Width="90"/>\n')
    f.write('   <Column ss:Width="160"/>\n')
    f.write('   <Column ss:Width="260"/>\n')

    f.write('   <Row ss:Height="25">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="4" ss:StyleID="TituloPrincipal"><Data ss:Type="String">PASO 4: CAPITAL INICIAL Y FUENTES DE FINANCIACIÓN (FONDO EMPRENDER)</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="18">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="4" ss:StyleID="SubtituloVerde"><Data ss:Type="String">Estructura financiera de arranque: $120.000.000 COP distribuidos en capital semilla, propio y bancario</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="10"/>\n')

    f.write('   <Row ss:Height="24">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="EncabezadoTabla"><Data ss:Type="String">FUENTE DE FINANCIACIÓN</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">MONTO APORTADO</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">% PART.</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">CONDICIONES / PLAZO</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">DESTINACIÓN EN EL PROYECTO</Data></Cell>\n')
    f.write('   </Row>\n')

    fuentes = [
        ("Fondo Emprender SENA", 80000000, 0.6667, "Capital semilla condonable (4 empleos)", "Maquinaria, hornos, equipos de cocina, TI y adecuaciones locativas"),
        ("Aporte Propio Karen Campo", 30000000, 0.2500, "Patrimonio propio / ahorros", "Muebles, menaje, gastos preoperativos, registro mercantil y licencias"),
        ("Microcrédito Banco Agrario", 10000000, 0.0833, "24 meses, tasa 1.2% MV ($497k/mes)", "Fondo de contingencia y capital de trabajo operativo inicial")
    ]
    for nom, monto, pct, cond, dest in fuentes:
        f.write('   <Row ss:Height="22">\n')
        f.write(f'    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(nom)}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{monto}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoPorc"><Data ss:Type="Number">{pct}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(cond)}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(dest)}</Data></Cell>\n')
        f.write('   </Row>\n')

    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="FilaTotal"><Data ss:Type="String">TOTAL CAPITAL DE INVERSIÓN</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-3]C:R[-1]C)"><Data ss:Type="Number">120000000</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-3]C:R[-1]C)"><Data ss:Type="Number">1.0</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal"><Data ss:Type="String">100.0% Financiado</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal"><Data ss:Type="String">Presupuesto Cerrado y Equilibrado</Data></Cell>\n')
    f.write('   </Row>\n')

    # Cuadro de Usos de Fondos
    f.write('   <Row ss:Height="20"/>\n')
    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="4" ss:StyleID="SubtituloVerde"><Data ss:Type="String">DISTRIBUCIÓN Y DESTINACIÓN DEL CAPITAL INICIAL (USO DE RECURSOS)</Data></Cell>\n')
    f.write('   </Row>\n')

    usos = [
        ("Maquinaria y Equipo de Producción", 56500000, 0.4708, "Horno napolitano, amasadora, refrigeradores, laminadora"),
        ("Adecuaciones Locativas y Filtros Chimenea", 18500000, 0.1542, "Extracción de humos, acometidas de gas y sanitarias"),
        ("Muebles, Enseres y Menaje de Trattoria", 16000000, 0.1333, "Mesas, sillas teca, vitrina de atención, barra y menaje"),
        ("Tecnología, POS y Red Gigabit", 8000000, 0.0667, "Servidor POS touch, tabletas comanderas, impresoras de cocina"),
        ("Motocicleta 125cc con Baúl Térmico", 7500000, 0.0625, "Flota de entrega rápida para domicilios directos a 70°C"),
        ("Gastos Preoperativos y Formalización Legal", 6000000, 0.0500, "Cámara de Comercio Popayán, RUES, Bomberos, Sayco, Invima"),
        ("Capital de Trabajo y Stock Inicial 3 Meses", 7500000, 0.0625, "Harina de fuerza, mozzarella caucano, pomodoro y caja de seguridad")
    ]
    for nom, monto, pct, det in usos:
        f.write('   <Row ss:Height="20">\n')
        f.write(f'    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(nom)}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{monto}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoPorc"><Data ss:Type="Number">{pct}</Data></Cell>\n')
        f.write(f'    <Cell ss:MergeAcross="1" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(det)}</Data></Cell>\n')
        f.write('   </Row>\n')

    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="FilaTotal"><Data ss:Type="String">TOTAL USOS DE CAPITAL</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-7]C:R[-1]C)"><Data ss:Type="Number">120000000</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-7]C:R[-1]C)"><Data ss:Type="Number">1.0</Data></Cell>\n')
    f.write('    <Cell ss:MergeAcross="1" ss:StyleID="FilaTotal"><Data ss:Type="String">Balance de Inversión 100% Calzado</Data></Cell>\n')
    f.write('   </Row>\n')

    f.write('  </Table>\n')
    f.write(' </Worksheet>\n')

    # ==============================================================================
    # HOJA 6: BALANCE GENERAL INICIAL DE APERTURA (PASO 5 GUÍA 10)
    # ==============================================================================
    f.write(' <Worksheet ss:Name="06_Balance_General_Inicial">\n')
    f.write('  <Table ss:DefaultColumnWidth="110">\n')
    f.write('   <Column ss:Width="30"/>\n')
    f.write('   <Column ss:Width="240"/>\n')
    f.write('   <Column ss:Width="130"/>\n')
    f.write('   <Column ss:Width="40"/>\n')
    f.write('   <Column ss:Width="240"/>\n')
    f.write('   <Column ss:Width="130"/>\n')

    f.write('   <Row ss:Height="25">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="4" ss:StyleID="TituloPrincipal"><Data ss:Type="String">BALANCE GENERAL DE APERTURA (DÍA 1 DE OPERACIÓN)</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="18">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="4" ss:StyleID="SubtituloVerde"><Data ss:Type="String">Pizzería Gourmet Bella Italia Popayán | NIT 901.876.543-1 | Karen Yuliana Campo</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="10"/>\n')

    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="EncabezadoAzul"><Data ss:Type="String">ACTIVOS</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoAzul"><Data ss:Type="String">VALOR COP</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="Default"/>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">PASIVOS Y PATRIMONIO</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">VALOR COP</Data></Cell>\n')
    f.write('   </Row>\n')

    balance_rows = [
        ("ACTIVO CORRIENTE", "", "", "PASIVO CORRIENTE", ""),
        ("Efectivo y Equivalentes (Caja/Bancos)", 21500000, "", "Obligaciones Financieras (Porción Corriente)", 4945000),
        ("Inventarios Iniciales (Materias Primas)", 7500000, "", "Cuentas por Pagar Proveedores", 0),
        ("Gastos Pagados por Anticipado (Pólizas)", 3000000, "", "Total Pasivo Corriente", 4945000),
        ("Total Activo Corriente", 32000000, "", "", ""),
        ("", "", "", "PASIVO NO CORRIENTE", ""),
        ("ACTIVO NO CORRIENTE", "", "", "Obligaciones Bancarias a Largo Plazo", 5055000),
        ("Maquinaria y Equipo Industrial", 56500000, "", "Total Pasivo No Corriente", 5055000),
        ("Adecuaciones Locativas y Ductos", 18500000, "", "TOTAL PASIVOS", 10000000),
        ("Muebles y Enseres de Salón", 16000000, "", "", ""),
        ("Equipos de Cómputo y TI", 8000000, "", "PATRIMONIO NETO", ""),
        ("Flota y Equipo de Transporte (Moto)", 7500000, "", "Capital Semilla Fondo Emprender SENA", 80000000),
        ("Activos Intangibles (Software/Registro)", 3000000, "", "Capital Suscrito y Pagado (Karen Campo)", 30000000),
        ("Total Activo No Corriente", 109500000, "", "Gastos Preoperativos Activados", 6000000),
        ("", "", "", "TOTAL PATRIMONIO", 116000000),
        ("TOTAL ACTIVOS", 141500000, "", "TOTAL PASIVO Y PATRIMONIO", 126000000)
    ]
    # Let's adjust exact values so equation balances exactly:
    # Activos:
    # Efectivo en Bancos: $6.000.000
    # Inventarios Iniciales: $7.500.000
    # Gastos Pagados por Anticipado: $2.500.000
    # -> Activo Corriente: $16.000.000
    # Activo No Corriente:
    # Maquinaria y Equipo: $56.500.000
    # Adecuaciones Locativas: $18.500.000
    # Muebles y Enseres: $16.000.000
    # Equipos de Cómputo: $8.000.000
    # Vehículo Moto: $7.500.000
    # Intangibles (Software POS): $3.500.000
    # -> Activo No Corriente: $110.000.000
    # Total Activos: $126.000.000 COP
    #
    # Pasivos:
    # Microcrédito Bancario Porción Corriente (Año 1): $4.945.000
    # Microcrédito Bancario Porción Largo Plazo (Año 2): $5.055.000
    # Total Pasivos: $10.000.000 COP
    #
    # Patrimonio:
    # Fondo Emprender SENA: $80.000.000
    # Aporte Karen Campo: $30.000.000
    # Gastos preoperativos formalización: $6.000.000
    # Total Patrimonio: $116.000.000 COP
    # Total Pasivo + Patrimonio: $126.000.000 COP! EXACT!
    
    balance_exacto = [
        ("ACTIVO CORRIENTE", "", "", "PASIVO CORRIENTE", ""),
        ("Efectivo y Equivalentes de Efectivo", 6000000, "", "Obligaciones Bancarias (Porción Corto Plazo)", 4945000),
        ("Inventarios Iniciales de Materias Primas", 7500000, "", "Otras Cuentas por Pagar de Apertura", 0),
        ("Gastos Pagados por Anticipado (Seguros/Pólizas)", 2500000, "", "Total Pasivo Corriente", 4945000),
        ("Total Activo Corriente", 16000000, "", "", ""),
        ("", "", "", "PASIVO NO CORRIENTE", ""),
        ("ACTIVO NO CORRIENTE", "", "", "Obligaciones Bancarias a Largo Plazo", 5055000),
        ("Maquinaria y Equipo de Cocina Industrial", 56500000, "", "Total Pasivo No Corriente", 5055000),
        ("Adecuaciones Locativas e Instalaciones", 18500000, "", "TOTAL PASIVOS DE APERTURA", 10000000),
        ("Muebles, Enseres y Menaje de Restaurante", 16000000, "", "", ""),
        ("Equipos de Cómputo, POS y Redes", 8000000, "", "PATRIMONIO DE APERTURA", ""),
        ("Flota y Equipo de Transporte (Motocicleta)", 7500000, "", "Capital Semilla Fondo Emprender SENA", 80000000),
        ("Activos Intangibles (Software POS y Licencias)", 3500000, "", "Capital Propio Emprendedora Karen Campo", 30000000),
        ("Total Activo No Corriente", 110000000, "", "Aportes de Capital Preoperativo", 6000000),
        ("", "", "", "TOTAL PATRIMONIO DE APERTURA", 116000000),
        ("TOTAL ACTIVOS DE APERTURA", 126000000, "", "TOTAL PASIVO + PATRIMONIO", 126000000)
    ]

    for c1, v1, sep, c2, v2 in balance_exacto:
        f.write('   <Row ss:Height="20">\n')
        
        # Lado Activos
        if c1 in ["ACTIVO CORRIENTE", "ACTIVO NO CORRIENTE"]:
            f.write(f'    <Cell ss:Index="2" ss:StyleID="SubtituloVerde"><Data ss:Type="String">{xe(c1)}</Data></Cell>\n')
            f.write('    <Cell ss:StyleID="SubtituloVerde"/>\n')
        elif c1 in ["Total Activo Corriente", "Total Activo No Corriente"]:
            f.write(f'    <Cell ss:Index="2" ss:StyleID="FilaTotal"><Data ss:Type="String">{xe(c1)}</Data></Cell>\n')
            f.write(f'    <Cell ss:StyleID="FilaTotal"><Data ss:Type="Number">{v1}</Data></Cell>\n')
        elif c1 == "TOTAL ACTIVOS DE APERTURA":
            f.write(f'    <Cell ss:Index="2" ss:StyleID="CardHeader"><Data ss:Type="String">{xe(c1)}</Data></Cell>\n')
            f.write(f'    <Cell ss:StyleID="CardValue"><Data ss:Type="Number">{v1}</Data></Cell>\n')
        elif c1 != "":
            f.write(f'    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(c1)}</Data></Cell>\n')
            f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{v1}</Data></Cell>\n')
        else:
            f.write('    <Cell ss:Index="2" ss:StyleID="Default"/>\n')
            f.write('    <Cell ss:StyleID="Default"/>\n')
            
        f.write('    <Cell ss:StyleID="Default"/>\n')

        # Lado Pasivos y Patrimonio
        if c2 in ["PASIVO CORRIENTE", "PASIVO NO CORRIENTE", "PATRIMONIO DE APERTURA"]:
            f.write(f'    <Cell ss:StyleID="SubtituloVerde"><Data ss:Type="String">{xe(c2)}</Data></Cell>\n')
            f.write('    <Cell ss:StyleID="SubtituloVerde"/>\n')
        elif c2 in ["Total Pasivo Corriente", "Total Pasivo No Corriente", "TOTAL PASIVOS DE APERTURA", "TOTAL PATRIMONIO DE APERTURA"]:
            f.write(f'    <Cell ss:StyleID="FilaTotal"><Data ss:Type="String">{xe(c2)}</Data></Cell>\n')
            f.write(f'    <Cell ss:StyleID="FilaTotal"><Data ss:Type="Number">{v2}</Data></Cell>\n')
        elif c2 == "TOTAL PASIVO + PATRIMONIO":
            f.write(f'    <Cell ss:StyleID="CardHeader"><Data ss:Type="String">{xe(c2)}</Data></Cell>\n')
            f.write(f'    <Cell ss:StyleID="CardValue"><Data ss:Type="Number">{v2}</Data></Cell>\n')
        elif c2 != "":
            f.write(f'    <Cell ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(c2)}</Data></Cell>\n')
            f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{v2}</Data></Cell>\n')
        else:
            f.write('    <Cell ss:StyleID="Default"/>\n')
            f.write('    <Cell ss:StyleID="Default"/>\n')

        f.write('   </Row>\n')

    # Cuadro de Verificación de Cuadre Contable
    f.write('   <Row ss:Height="20"/>\n')
    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="4" ss:StyleID="SubtituloVerde"><Data ss:Type="String">VERIFICACIÓN DE LA ECUACIÓN PATRIMONIAL FUNDAMENTAL</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="20">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="1" ss:StyleID="EncabezadoTabla"><Data ss:Type="String">ECUACIÓN CONTABLE</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="Default"/>\n')
    f.write('    <Cell ss:MergeAcross="1" ss:StyleID="EncabezadoTabla"><Data ss:Type="String">ESTADO DE CUADRE</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="1" ss:StyleID="FilaDatoCentro"><Data ss:Type="String">ACTIVO ($126M) = PASIVO ($10M) + PATRIMONIO ($116M)</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="Default"/>\n')
    f.write('    <Cell ss:MergeAcross="1" ss:StyleID="CardValue"><Data ss:Type="String">CUADRE PERFECTO: DIFERENCIA $0 COP</Data></Cell>\n')
    f.write('   </Row>\n')

    f.write('  </Table>\n')
    f.write(' </Worksheet>\n')

    # ==============================================================================
    # HOJA 7: ESTADO DE RESULTADOS PROYECTADO A 12 MESES (P&G)
    # ==============================================================================
    f.write(' <Worksheet ss:Name="07_Estado_Resultados_12M">\n')
    f.write('  <Table ss:DefaultColumnWidth="85">\n')
    f.write('   <Column ss:Width="30"/>\n')
    f.write('   <Column ss:Width="230"/>\n')
    for m in range(1, 13):
        f.write('   <Column ss:Width="85"/>\n')
    f.write('   <Column ss:Width="110"/>\n')

    f.write('   <Row ss:Height="25">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="13" ss:StyleID="TituloPrincipal"><Data ss:Type="String">PASO 5: ESTADO DE RESULTADOS PROYECTADO A 12 MESES (P&amp;G AÑO 1)</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="18">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="13" ss:StyleID="SubtituloVerde"><Data ss:Type="String">Evolución mensual de ventas, costos variables, gastos operacionales, EBITDA y utilidad neta</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="10"/>\n')

    # Encabezado meses
    f.write('   <Row ss:Height="24">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="EncabezadoTabla"><Data ss:Type="String">RUBRO / CONCEPTO FINANCIERO</Data></Cell>\n')
    for m in range(1, 13):
        f.write(f'    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">MES {m}</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoAzul"><Data ss:Type="String">TOTAL AÑO 1</Data></Cell>\n')
    f.write('   </Row>\n')

    # Factores estacionales de ventas mes a mes (meses iniciales curva de arranque, meses 6 y 12 picos altos)
    factores = [0.065, 0.070, 0.075, 0.080, 0.085, 0.095, 0.085, 0.085, 0.085, 0.090, 0.095, 0.110]
    total_anual_ventas = 310500000
    ventas_mensuales = [round(total_anual_ventas * f_m) for f_m in factores]
    # Ajuste para cuadrar exactamente $310.500.000
    dif_ventas = total_anual_ventas - sum(ventas_mensuales)
    ventas_mensuales[-1] += dif_ventas

    costos_mensuales = [round(v * 0.30338164) for v in ventas_mensuales]
    dif_costos = 94200000 - sum(costos_mensuales)
    costos_mensuales[-1] += dif_costos

    # Filas de P&G
    # 1. Ventas
    f.write('   <Row ss:Height="20">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">(+) Ingresos Operacionales (Ventas)</Data></Cell>\n')
    for vm in ventas_mensuales:
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{vm}</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(RC[-12]:RC[-1])"><Data ss:Type="Number">310500000</Data></Cell>\n')
    f.write('   </Row>\n')

    # 2. Costo de Ventas
    f.write('   <Row ss:Height="20">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">(-) Costo de Mercancía Vendida (CMV)</Data></Cell>\n')
    for cm in costos_mensuales:
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{cm}</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(RC[-12]:RC[-1])"><Data ss:Type="Number">94200000</Data></Cell>\n')
    f.write('   </Row>\n')

    # 3. Utilidad Bruta
    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="SubtituloVerde"><Data ss:Type="String">(=) UTILIDAD BRUTA</Data></Cell>\n')
    for m in range(12):
        ub = ventas_mensuales[m] - costos_mensuales[m]
        f.write(f'    <Cell ss:StyleID="SubtituloVerde" ss:Formula="=R[-2]C-R[-1]C"><Data ss:Type="Number">{ub}</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="SubtituloVerde" ss:Formula="=R[-2]C-R[-1]C"><Data ss:Type="Number">216300000</Data></Cell>\n')
    f.write('   </Row>\n')

    # Gastos de Operación
    nomina_mensual = 10988746
    arriendo_mensual = 2500000
    servicios_mensual = 1200000
    pauta_mensual = 300000
    deprec_mensual = 862500
    contador_mensual = 350000
    aseo_mensual = 200000

    gastos_items = [
        ("(-) Gastos de Personal (Nómina 4 empleados)", nomina_mensual, 131864952),
        ("(-) Arriendo Local Centro Histórico", arriendo_mensual, 30000000),
        ("(-) Servicios Públicos y Leña Certificada", servicios_mensual, 14400000),
        ("(-) Publicidad Digital y Marketing Local", pauta_mensual, 3600000),
        ("(-) Depreciación de Activos Fijos", deprec_mensual, 10350000),
        ("(-) Asesoría Contable y Software Tributario", contador_mensual, 4200000),
        ("(-) Mantenimiento, Aseo y Fumigación", aseo_mensual, 2400000)
    ]

    for nom_g, v_mes, v_tot in gastos_items:
        f.write('   <Row ss:Height="20">\n')
        f.write(f'    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(nom_g)}</Data></Cell>\n')
        for m in range(12):
            f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{v_mes}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda" ss:Formula="=SUM(RC[-12]:RC[-1])"><Data ss:Type="Number">{v_tot}</Data></Cell>\n')
        f.write('   </Row>\n')

    # Total Gastos Operacionales
    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="FilaTotal"><Data ss:Type="String">(=) TOTAL GASTOS OPERACIONALES</Data></Cell>\n')
    for m in range(12):
        f.write('    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-7]C:R[-1]C)"><Data ss:Type="Number">16401246</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(R[-7]C:R[-1]C)"><Data ss:Type="Number">196814952</Data></Cell>\n')
    f.write('   </Row>\n')

    # Utilidad Operativa (EBIT)
    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="EncabezadoTabla"><Data ss:Type="String">(=) UTILIDAD OPERACIONAL (EBIT)</Data></Cell>\n')
    for m in range(12):
        f.write('    <Cell ss:StyleID="EncabezadoTabla" ss:Formula="=R[-9]C-R[-1]C"/>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla" ss:Formula="=R[-9]C-R[-1]C"><Data ss:Type="Number">19485048</Data></Cell>\n')
    f.write('   </Row>\n')

    # Gastos Financieros (Intereses microcrédito)
    f.write('   <Row ss:Height="20">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">(-) Gastos Financieros (Interés Microcrédito)</Data></Cell>\n')
    intereses_mes = [115000, 110000, 105000, 100000, 95000, 90000, 85000, 80000, 75000, 65000, 56000, 50000]
    for im in intereses_mes:
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{im}</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaDatoMoneda" ss:Formula="=SUM(RC[-12]:RC[-1])"><Data ss:Type="Number">1026000</Data></Cell>\n')
    f.write('   </Row>\n')

    # Utilidad Antes de Impuestos
    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="SubtituloVerde"><Data ss:Type="String">(=) UTILIDAD ANTES DE IMPUESTOS (UAI)</Data></Cell>\n')
    for m in range(12):
        f.write('    <Cell ss:StyleID="SubtituloVerde" ss:Formula="=R[-2]C-R[-1]C"/>\n')
    f.write('    <Cell ss:StyleID="SubtituloVerde" ss:Formula="=R[-2]C-R[-1]C"><Data ss:Type="Number">18459048</Data></Cell>\n')
    f.write('   </Row>\n')

    # Provisión Impuestos 20%
    f.write('   <Row ss:Height="20">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">(-) Provisión Impuestos Régimen SIMPLE (20%)</Data></Cell>\n')
    for m in range(12):
        f.write('    <Cell ss:StyleID="FilaDatoMoneda" ss:Formula="=IF(R[-1]C>0,ROUND(R[-1]C*0.20,0),0)"/>\n')
    f.write('    <Cell ss:StyleID="FilaDatoMoneda" ss:Formula="=ROUND(R[-1]C*0.20,0)"><Data ss:Type="Number">3691810</Data></Cell>\n')
    f.write('   </Row>\n')

    # Utilidad Neta
    f.write('   <Row ss:Height="24">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="CardHeader"><Data ss:Type="String">(=) UTILIDAD NETA DEL EJERCICIO</Data></Cell>\n')
    for m in range(12):
        f.write('    <Cell ss:StyleID="CardValue" ss:Formula="=R[-2]C-R[-1]C"/>\n')
    f.write('    <Cell ss:StyleID="CardValue" ss:Formula="=R[-2]C-R[-1]C"><Data ss:Type="Number">14767238</Data></Cell>\n')
    f.write('   </Row>\n')

    f.write('  </Table>\n')
    f.write(' </Worksheet>\n')

    # ==============================================================================
    # HOJA 8: FLUJO DE CAJA PROYECTADO A 12 MESES
    # ==============================================================================
    f.write(' <Worksheet ss:Name="08_Flujo_Caja_12M">\n')
    f.write('  <Table ss:DefaultColumnWidth="90">\n')
    f.write('   <Column ss:Width="30"/>\n')
    f.write('   <Column ss:Width="230"/>\n')
    for m in range(1, 13):
        f.write('   <Column ss:Width="90"/>\n')
    f.write('   <Column ss:Width="110"/>\n')

    f.write('   <Row ss:Height="25">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="13" ss:StyleID="TituloPrincipal"><Data ss:Type="String">PASO 5: FLUJO DE CAJA Y TESORERÍA PROYECTADA A 12 MESES</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="18">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="13" ss:StyleID="SubtituloVerde"><Data ss:Type="String">Monitoreo de liquidez, recaudo en efectivo/tarjetas y saldo acumulado sin déficit de tesorería</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="10"/>\n')

    # Encabezados
    f.write('   <Row ss:Height="24">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="EncabezadoTabla"><Data ss:Type="String">CONCEPTO DE TESORERÍA</Data></Cell>\n')
    for m in range(1, 13):
        f.write(f'    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">MES {m}</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoAzul"><Data ss:Type="String">TOTAL AÑO 1</Data></Cell>\n')
    f.write('   </Row>\n')

    # Saldo Inicial de Caja
    # Mes 1 arranca con $6.000.000 de caja libre de arranque
    f.write('   <Row ss:Height="20">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="SubtituloVerde"><Data ss:Type="String">SALDO INICIAL DE EFECTIVO</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="SubtituloVerde"><Data ss:Type="Number">6000000</Data></Cell>\n')
    for m in range(2, 13):
        f.write('    <Cell ss:StyleID="SubtituloVerde" ss:Formula="=R[7]C[-1]"/>\n')
    f.write('    <Cell ss:StyleID="SubtituloVerde"><Data ss:Type="Number">6000000</Data></Cell>\n')
    f.write('   </Row>\n')

    # Entradas de Efectivo (Ventas de contado y POS digital)
    f.write('   <Row ss:Height="20">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">(+) Recaudo Ventas de Contado y Tarjeta/POS</Data></Cell>\n')
    for vm in ventas_mensuales:
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{vm}</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(RC[-12]:RC[-1])"><Data ss:Type="Number">310500000</Data></Cell>\n')
    f.write('   </Row>\n')

    # Salidas Operacionales
    f.write('   <Row ss:Height="20">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">(-) Pago Materias Primas e Insumos</Data></Cell>\n')
    for cm in costos_mensuales:
        f.write(f'    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">{cm}</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(RC[-12]:RC[-1])"><Data ss:Type="Number">94200000</Data></Cell>\n')
    f.write('   </Row>\n')

    # Salidas Nómina
    f.write('   <Row ss:Height="20">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">(-) Pago Nómina y Seguridad Social</Data></Cell>\n')
    for m in range(12):
        f.write('    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">10988746</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(RC[-12]:RC[-1])"><Data ss:Type="Number">131864952</Data></Cell>\n')
    f.write('   </Row>\n')

    # Salidas Otros Gastos Operativos (Arriendo + servicios + pauta + contador + aseo = $4.550.000/mes)
    f.write('   <Row ss:Height="20">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">(-) Arriendo, Servicios, Pauta y Contabilidad</Data></Cell>\n')
    for m in range(12):
        f.write('    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">4550000</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(RC[-12]:RC[-1])"><Data ss:Type="Number">54600000</Data></Cell>\n')
    f.write('   </Row>\n')

    # Salidas Servicio de Deuda (Cuota crédito $497.000/mes)
    f.write('   <Row ss:Height="20">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">(-) Cuota Microcrédito Bancario</Data></Cell>\n')
    for m in range(12):
        f.write('    <Cell ss:StyleID="FilaDatoMoneda"><Data ss:Type="Number">497000</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="FilaTotal" ss:Formula="=SUM(RC[-12]:RC[-1])"><Data ss:Type="Number">5964000</Data></Cell>\n')
    f.write('   </Row>\n')

    # Flujo Neto del Mes
    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="EncabezadoTabla"><Data ss:Type="String">(=) FLUJO NETO DEL PERIODO</Data></Cell>\n')
    for m in range(12):
        f.write('    <Cell ss:StyleID="EncabezadoTabla" ss:Formula="=R[-4]C-SUM(R[-3]C:R[-1]C)"/>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla" ss:Formula="=R[-4]C-SUM(R[-3]C:R[-1]C)"><Data ss:Type="Number">23871048</Data></Cell>\n')
    f.write('   </Row>\n')

    # Saldo Final de Caja
    f.write('   <Row ss:Height="24">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="CardHeader"><Data ss:Type="String">(=) SALDO FINAL DE CAJA ACUMULADO</Data></Cell>\n')
    for m in range(12):
        f.write('    <Cell ss:StyleID="CardValue" ss:Formula="=R[-6]C+R[-1]C"/>\n')
    f.write('    <Cell ss:StyleID="CardValue" ss:Formula="=RC[-1]"><Data ss:Type="Number">29871048</Data></Cell>\n')
    f.write('   </Row>\n')

    f.write('  </Table>\n')
    f.write(' </Worksheet>\n')

    # ==============================================================================
    # HOJA 9: INDICADORES FINANCIEROS Y PUNTO DE EQUILIBRIO (DASHBOARD)
    # ==============================================================================
    f.write(' <Worksheet ss:Name="09_Indicadores_Equilibrio">\n')
    f.write('  <Table ss:DefaultColumnWidth="110">\n')
    f.write('   <Column ss:Width="30"/>\n')
    f.write('   <Column ss:Width="220"/>\n')
    f.write('   <Column ss:Width="130"/>\n')
    f.write('   <Column ss:Width="100"/>\n')
    f.write('   <Column ss:Width="260"/>\n')

    f.write('   <Row ss:Height="25">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="3" ss:StyleID="TituloPrincipal"><Data ss:Type="String">DASHBOARD DE INDICADORES FINANCIEROS Y PUNTO DE EQUILIBRIO</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="18">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="3" ss:StyleID="SubtituloVerde"><Data ss:Type="String">Evaluación de rentabilidad, umbral de equilibrio, ROI, payback y viabilidad Fondo Emprender</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="10"/>\n')

    f.write('   <Row ss:Height="24">\n')
    f.write('    <Cell ss:Index="2" ss:StyleID="EncabezadoTabla"><Data ss:Type="String">INDICADOR FINANCIERO</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">VALOR CALCULADO</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">BENCHMARK / META</Data></Cell>\n')
    f.write('    <Cell ss:StyleID="EncabezadoTabla"><Data ss:Type="String">INTERPRETACIÓN DE RESULTADOS</Data></Cell>\n')
    f.write('   </Row>\n')

    indicadores = [
        ("Ventas Totales Proyectadas Año 1", "$ 310.500.000 COP", "> $280M COP", "Ingresos comerciales suficientes para absorber la operación"),
        ("Costos Variables Totales (CMV)", "$ 94.200.000 COP", "< 35% ventas", "30.34% de los ingresos, excelente eficiencia en costeo de materias primas"),
        ("Margen de Contribución Total", "$ 216.300.000 COP", "> 65% ventas", "69.66% de margen bruto para responder por la carga fija empresarial"),
        ("Costos Fijos Operacionales Totales", "$ 197.840.952 COP", "Control estricto", "Incluye nómina formal ($131.86M), arriendo, servicios, depreciaciones e intereses"),
        ("Punto de Equilibrio en Pesos (Break-Even)", "$ 283.846.416 COP", "< Ventas Totales", "Monto mínimo en pesos requerido para no perder dinero en el ejercicio"),
        ("Punto de Equilibrio en Unidades (Anual)", "7.096 Unidades", "< Unidades totales", "Equivale a 591 unidades promedio al mes"),
        ("Punto de Equilibrio en Unidades (Diario)", "19.7 Unidades / día", "< 35 pizzas/día", "Con solo 20 pizzas vendidas al día el restaurante cubre el 100% de costos y nómina"),
        ("Margen de Seguridad de Ventas", "8.58%", "> 5%", "Las ventas proyectadas superan el punto de equilibrio en $26.653.584 COP"),
        ("Utilidad Operacional (EBIT)", "$ 19.485.048 COP", "> 5% ventas", "Margen operacional del 6.28% en año de puesta en marcha"),
        ("EBITDA Año 1", "$ 29.835.048 COP", "> 9% ventas", "Flujo operativo bruto del 9.61% antes de depreciaciones y financiamiento"),
        ("Utilidad Neta Año 1", "$ 14.767.238 COP", "> 4% ventas", "Rentabilidad final limpia para reserva legal y reinversión tecnológica"),
        ("Retorno sobre la Inversión (ROI)", "12.31% anual", "> Tasa DTF (10%)", "Rentabilidad superior al costo de oportunidad del mercado de capitales"),
        ("Período de Recuperación (Payback)", "2.8 años", "< 4 años", "Recuperación completa del capital mediante flujo de caja operativo"),
        ("Generación de Empleo Directo Formal", "4 Empleos Directos", "Meta: 4 Empleos", "Cumplimiento al 100% de la meta para condonación total de $80M Fondo Emprender")
    ]

    for ind, val, meta, interp in indicadores:
        f.write('   <Row ss:Height="22">\n')
        f.write(f'    <Cell ss:Index="2" ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(ind)}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoCentro"><Data ss:Type="String">{xe(val)}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoCentro"><Data ss:Type="String">{xe(meta)}</Data></Cell>\n')
        f.write(f'    <Cell ss:StyleID="FilaDatoTexto"><Data ss:Type="String">{xe(interp)}</Data></Cell>\n')
        f.write('   </Row>\n')

    # Resumen Gráfico / Destacado
    f.write('   <Row ss:Height="20"/>\n')
    f.write('   <Row ss:Height="22">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="3" ss:StyleID="SubtituloVerde"><Data ss:Type="String">SÍNTESIS DE VIABILIDAD PARA COMITÉ DE EVALUACIÓN FONDO EMPRENDER SENA</Data></Cell>\n')
    f.write('   </Row>\n')
    f.write('   <Row ss:Height="35">\n')
    f.write('    <Cell ss:Index="2" ss:MergeAcross="3" ss:StyleID="CardValue"><Data ss:Type="String">PROYECTO FINANCIERAMENTE VIABLE, SOSTENIBLE Y APTO PARA CONDONACIÓN DEL 100%</Data></Cell>\n')
    f.write('   </Row>\n')

    f.write('  </Table>\n')
    f.write(' </Worksheet>\n')

    f.write('</Workbook>\n')

print("Generando XML Spreadsheet 2003 completado exitosamente.")

# Convert to ODS and XLSX using LibreOffice headless
ods_path = os.path.join(HOJA_DIR, 'GA10-240201529-AA3-EV01_Plan_Negocio.ods')
xlsx_path = os.path.join(HOJA_DIR, 'GA10-240201529-AA3-EV01_Plan_Negocio.xlsx')

print("Convirtiendo XML a ODS con soffice...")
cmd_ods = ['soffice', '--headless', '--convert-to', 'ods', xml_file_path, '--outdir', HOJA_DIR]
res_ods = subprocess.run(cmd_ods, capture_output=True, text=True)
print("Salida ODS:", res_ods.stdout, res_ods.stderr)

print("Convirtiendo ODS a XLSX con soffice...")
cmd_xlsx = ['soffice', '--headless', '--convert-to', 'xlsx:Calc MS Excel 2007 XML', ods_path, '--outdir', HOJA_DIR]
res_xlsx = subprocess.run(cmd_xlsx, capture_output=True, text=True)
print("Salida XLSX:", res_xlsx.stdout, res_xlsx.stderr)

# Copiar a entrega Zajuna
if os.path.exists(xlsx_path):
    shutil.copy(xlsx_path, os.path.join(ENTREGA_HOJA_DIR, 'GA10-240201529-AA3-EV01_Plan_Negocio.xlsx'))
    shutil.copy(xlsx_path, os.path.join(ENTREGA_DIR, 'GA10-240201529-AA3-EV01_Plan_Negocio.xlsx'))
    print("Copia a carpeta de entrega Zajuna XLSX realizada.")

if os.path.exists(ods_path):
    shutil.copy(ods_path, os.path.join(ENTREGA_HOJA_DIR, 'GA10-240201529-AA3-EV01_Plan_Negocio.ods'))
    shutil.copy(ods_path, os.path.join(ENTREGA_DIR, 'GA10-240201529-AA3-EV01_Plan_Negocio.ods'))
    print("Copia a carpeta de entrega Zajuna ODS realizada.")

print("Proceso finalizado con éxito.")
