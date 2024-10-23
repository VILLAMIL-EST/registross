from datetime import datetime


class Principal:
    estudiantes = []
    cursos = []
    sesiones = []
    asistencias = []

    class Estudiante:
        def __init__(self, tipo_documento, numero_documento, nombres):
            self.tipo_documento = tipo_documento
            self.numero_documento = numero_documento
            self.nombres = nombres

        def __str__(self):
            return f"Tipo de Documento: {self.tipo_documento}, Número: {self.numero_documento}, Nombres: {self.nombres}"

    class Curso:
        def __init__(self, codigo, nombre):
            self.codigo = codigo
            self.nombre = nombre

        def __str__(self):
            return f"Código: {self.codigo}, Nombre: {self.nombre}"

    class Sesion:
        def __init__(self, codigo_curso, hora_inicio, hora_final, fecha):
            self.codigo_curso = codigo_curso
            self.hora_inicio = hora_inicio
            self.hora_final = hora_final
            self.fecha = fecha

        def __str__(self):
            return f"Código Curso: {self.codigo_curso}, Hora Inicio: {self.hora_inicio}, Hora Final: {self.hora_final}, Fecha: {self.fecha}"

    class Asistencia:
        def __init__(self, codigo_sesion, documento_estudiante, estado):
            self.codigo_sesion = codigo_sesion
            self.documento_estudiante = documento_estudiante
            self.estado = estado

        def __str__(self):
            return f"Código Sesión: {self.codigo_sesion}, Documento Estudiante: {self.documento_estudiante}, Estado: {self.estado}"

    @classmethod
    def agregarEstudiante(cls):
        print("\nSeleccione el tipo de documento:")
        print("1. Tarjeta de identidad")
        print("2. Cédula")
        opcion = input("Ingrese el número de opción --> ")

        if opcion == '1':
            tipo_documento = "Tarjeta de identidad"
        elif opcion == '2':
            tipo_documento = "Cédula"
        else:
            print("Opción no válida. Intente nuevamente.")
            return

        numero_documento = input("Ingrese el número de documento: ")
        nombres = input("Ingrese los nombres completos del estudiante: ")
        estudiante = cls.Estudiante(tipo_documento, numero_documento, nombres)
        cls.estudiantes.append(estudiante)
        print("\nEstudiante agregado correctamente.")

    @classmethod
    def listarEstudiante(cls, numero_documento):
        filtrados = [estudiante for estudiante in cls.estudiantes if estudiante.numero_documento == numero_documento]
        if not filtrados:
            print(f"No hay estudiantes registrados con el documento: {numero_documento}.")
        else:
            for estudiante in filtrados:
                print(estudiante)

    @classmethod
    def agregarCurso(cls):
        codigo = input("Ingrese el código del curso: ")
        nombre = input("Ingrese el nombre del curso: ")
        curso = cls.Curso(codigo, nombre)
        cls.cursos.append(curso)
        print("\nCurso agregado correctamente.")

    @classmethod
    def listarCurso(cls, codigo):
        filtrados = [curso for curso in cls.cursos if curso.codigo == codigo]
        if not filtrados:
            print(f"No hay cursos registrados con el código: {codigo}.")
        else:
            for curso in filtrados:
                print(curso)

    @classmethod
    def agregarSesion(cls):
        codigo_curso = input("Ingrese el código del curso: ")
        hora_inicio = input("Ingrese la hora de inicio (HH:MM): ")
        hora_final = input("Ingrese la hora final (HH:MM): ")
        fecha = input("Ingrese la fecha (DD/MM/YYYY): ")
        sesion = cls.Sesion(codigo_curso, hora_inicio, hora_final, fecha)
        cls.sesiones.append(sesion)
        print("\nSesión agregada correctamente.")

    @classmethod
    def listarSesion(cls, codigo_sesion):
        filtrados = [sesion for sesion in cls.sesiones if sesion.codigo_curso == codigo_sesion]
        if not filtrados:
            print(f"No hay sesiones registradas con el código de sesión: {codigo_sesion}.")
        else:
            for sesion in filtrados:
                print(sesion)

    @classmethod
    def agregarAsistencia(cls):
        codigo_sesion = input("Ingrese el código de la sesión: ")
        documento_estudiante = input("Ingrese el documento del estudiante: ")

        estado = input("Ingrese el estado (0: Si llegó, 1: Llegó tarde, 2: No llegó): ")
        while estado not in ['0', '1', '2']:
            print("Estado no válido. Debe ser 0, 1 o 2.")
            estado = input("Ingrese el estado (0: Si llegó, 1: Llegó tarde, 2: No llegó): ")

        asistencia = cls.Asistencia(codigo_sesion, documento_estudiante, estado)
        cls.asistencias.append(asistencia)
        print("\nAsistencia agregada correctamente.")

    @classmethod
    def listarAsistencia(cls, codigo_sesion, documento_estudiante):
        filtradas = [asistencia for asistencia in cls.asistencias
                     if
                     asistencia.codigo_sesion == codigo_sesion and asistencia.documento_estudiante == documento_estudiante]

        if not filtradas:
            print(
                f"No hay asistencias registradas para el código de sesión: {codigo_sesion} y documento: {documento_estudiante}.")
        else:
            for asistencia in filtradas:
                print(asistencia)

    @classmethod
    def listarTardanzasSesion(cls, codigo_sesion):
        tardanzas = [asistencia for asistencia in cls.asistencias if
                     asistencia.codigo_sesion == codigo_sesion and asistencia.estado == '1']
        if not tardanzas:
            print(f"No hubo estudiantes que llegaron tarde en la sesión con código: {codigo_sesion}.")
        else:
            print(f"Estudiantes que llegaron tarde en la sesión {codigo_sesion}:")
            for asistencia in tardanzas:
                print("Numero de Identidad: " + asistencia.documento_estudiante)

    @classmethod
    def listarTardanzasCursoRango(cls, codigo_curso, fecha_inicio, fecha_fin):
        fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")
        sesiones_curso = [sesion for sesion in cls.sesiones if sesion.codigo_curso == codigo_curso]

        if not sesiones_curso:
            print(f"No hay sesiones del curso {codigo_curso} en el rango de fechas dado.")
            return
        for sesion in sesiones_curso:
            tardanzas_sesion = [asistencia for asistencia in cls.asistencias
                                if asistencia.codigo_sesion == sesion.codigo_curso and asistencia.estado == '1']
            print(
                f"Sesión {sesion.codigo_curso} del {sesion.fecha}: {len(tardanzas_sesion)} estudiantes llegaron tarde.")

    @classmethod
    def iniciar(cls):
        while True:
            print("_- Menú Principal -_")
            print("\n1.  Agregar estudiante")
            print("2.  Agregar curso")
            print("3.  Agregar sesión")
            print("4.  Registrar asistencia")
            print("5.  Listar datos de un estudiante")
            print("6.  Listar datos de un curso")
            print("7.  Listar datos de una sesión")
            print("8.  Listar datos de una asistencia")
            print("9.  Consultar estudiantes que llegaron tarde")
            print("10. Consultar veces de llegadas tardias de un estudiante")
            print("11. Salir")

            opcion = input("Seleccione una opción --> ")

            if opcion == '1':
                cls.agregarEstudiante()
            elif opcion == '2':
                cls.agregarCurso()
            elif opcion == '3':
                cls.agregarSesion()
            elif opcion == '4':
                cls.agregarAsistencia()
            elif opcion == '5':
                documento_id = input("Ingrese el documento del estudiante: ")
                cls.listarEstudiante(documento_id)
            elif opcion == '6':
                codigo_curso = input("Ingrese el código del curso: ")
                cls.listarCurso(codigo_curso)
            elif opcion == '7':
                codigo_sesion = input("Ingrese el código de la sesión: ")
                cls.listarSesion(codigo_sesion)
            elif opcion == '8':
                codigo_sesion = input("Ingrese el código de la sesión: ")
                documento_estudiante = input("Ingrese el documento del estudiante: ")
                cls.listarAsistencia(codigo_sesion, documento_estudiante)
            elif opcion == '9':
                codigo_sesion = input("Ingrese el código de la sesión: ")
                cls.listarTardanzasSesion(codigo_sesion)
            elif opcion == '10':
                codigo_curso = input("Ingrese el código del curso: ")
                fecha_inicio = input("Ingrese la fecha de inicio (DD/MM/YYYY): ")
                fecha_fin = input("Ingrese la fecha final (DD/MM/YYYY): ")
                cls.listarTardanzasCursoRango(codigo_curso, fecha_inicio, fecha_fin)
            elif opcion == '11':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")


# Ejecutar el programa
Principal.iniciar()
