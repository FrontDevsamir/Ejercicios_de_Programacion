
from textwrap import fill
import tkinter as tk
from tkinter import Button, ttk, messagebox
import os
import sys
import random
import string as strg
import conexion


class Styles:

    """
       *|> Metodo de inicializacion donde se definiran todos los estilos por default para la interfaz grafica GUI <|*
    """

    def __init__(self, master) -> None:

        self.style = ttk.Style(master=master)
        self.style.theme_use('alt')

        self.theme = {
            'light': {
                'bg': '#E6F3FF', 'bg-lb-nm': '#235A9F', 'bg-lb-dg': 'red', 'bg-btn-nm': '#0078D4', 'bg-btn-hv': '#235A9F', 'clr-bd': '#80B9EE', 'clr-bd-fc': '#235A9F',
                'bg-btn-dg': 'red', 'fg-lb-nm': 'black', 'fg-lb-dg': 'black', 'fg-btn-nm': 'white', 'fg-btn-dg': 'black', 'fg-lb-rb': 'white'
            },
            'dark': {

            },
            'lightgreen': {

            },
            'darkgreen': {

            }
        }

        self.family = 'Cascadia Code PL'
        self.size = 15
        self.weight = 'normal'
        self.font = [self.family, self.size, self.weight]
        self.theme_use = 'light'

        # *====|> Empezamos a configurar los estilos con |>configure<| <|====
        # Frame
        self.style.configure(
            'TFrame', background=self.theme[self.theme_use]['bg'], takefocus=1)
        # BD.TFrame
        self.style.configure('BD.TFrame', borderwidth=3,
                             relief='groove', padding=10)
        # TLabel
        self.style.configure('TLabel', background=self.theme[self.theme_use]['bg'], foreground=self.theme[self.theme_use]['fg-lb-nm'], font=(
            'Cascadia Code PL', 18, 'normal'), padding=10, anchor='center', relief='groove', borderwidth=1)
        # HEADING.TLabel
        self.style.configure('HEADING.TLabel', font=('Cascadia Code PL', 25, 'normal'),
                             foreground=self.theme[self.theme_use]['bg'], background=self.theme[self.theme_use]['bg-lb-nm'])
        # ERROR.TLAbel
        self.style.configure('ERROR.TLabel', background=self.theme[self.theme_use]['bg-lb-dg'], foreground=self.theme[self.theme_use]
                             ['fg-lb-dg'], bordercolor='red', relief='flat', font=('Cascadia Code PL', 12, 'normal'))
        # FORM.TLabel
        self.style.configure('FORM.TLabel', font=(
            'Cascadia Code PL', 12, 'normal'), padding=8, justify='right', anchor='left', relief='flat')
        # TRADIOBUTTON
        self.style.configure('TRadiobutton', foreground=self.theme[self.theme_use]['fg-lb-nm'],
                             background=self.theme[self.theme_use]['bg'], takefocus=0, font=('Cascadia Code PL', 15, 'normal'), padding=10)
        # TButton
        self.style.configure('TButton', font=('Cascadia Code PL', 18, 'bold'),
                             background=self.theme[self.theme_use]['bg-btn-nm'], foreground=self.theme[self.theme_use]['fg-lb-rb'], padding=10, takefocus=0)
        self.style.map('TButton', background=[
                       ('pressed', self.theme[self.theme_use]['bg-btn-hv']), ('active', self.theme[self.theme_use]['bg-btn-hv'])])
        # DG.TButton
        self.style.configure(
            'DG.TButton', background=self.theme[self.theme_use]['bg-btn-dg'], foreground=self.theme[self.theme_use]['fg-btn-dg'])
        self.style.map('DG.TButton', background=[
                       ('pressed', self.theme[self.theme_use]['bg-btn-dg']), ('active', self.theme[self.theme_use]['bg-btn-dg'])])
        # S.TButton
        self.style.configure('S.TButton', font=(
            'Cascadia Code PL', 12, 'bold'), padding=2)
        # TEntry
        self.style.configure('TEntry', bordercolor=self.theme[self.theme_use]['clr-bd'],
                             fieldbackground=self.theme[self.theme_use]['bg'], font=('Cascadia Code PL', 15, 'normal'), border=5)
        # E.TEntry
        self.style.configure('E.TEntry', width=25, font=(
            'Cascadia Code PL', 10, 'normal'))

        # TCombobox
        self.style.configure('TCombobox', height=7)

        # TLabelFrame
        self.style.configure(
            'TLabelframe', background=self.theme[self.theme_use]['bg'])

        self.style.configure("Treeview", font=(
            'Cascadia Code PL', 12, 'normal', 'italic'), foreground='black', rowheight=35)
        self.style.map('Treeview', background=[
            ('selected', 'blue')], foreground=[('selected', 'white')])
        self.style.configure('Heading', background='blue',
                             foreground='white', padding=3, font=('Cascadia Code PL', 14, 'bold'))
        self.style.configure('TScrollbar', arrowcolor='deepblue',
                             bordercolor='blue', troughcolor='darkblue', background='skyblue')
        self.style.map('TScrollbar', background=[('active', 'blue')])

    """ 
        *|> Metodo que se encargara de realizar los cambios de estilos de colores de los widgets Tematicos . osea modificara sus estilos por default en __init__ <|*
    """

    def change(self, palett):

        pass


# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')


""" 
*|> CLASE QUE CREARA LA VENTANA PARA CREAR UN NUEVO USUARIO <|*
"""


class NuevoUsuario(ttk.Frame):

    def __init__(self, master, **kwarg):
        super().__init__(master, **kwarg)

        self.master = master
        self.styles = Styles(master)

        # Instaciamos la clase DataBase de modulo conexion para trabajar con el CRUD del programa
        self.DB = conexion.DataBase()
        self.DB.conectar('usuarios')

        self.crear_tabla_usuarios()

        self.var_rb = tk.IntVar(value=1)

        # WIDGTES
        self.lb_title = ttk.Label(
            self, text='BIENVENIDO A TU GESTOR DE CONTRASEÑAS', style='HEADING.TLabel')
        self.rb_one = ttk.Radiobutton(self, text='CREAR NUEVA CUENTA', value=1,
                                      variable=self.var_rb, takefocus=0, command=self.frame_rb_one)
        self.rb_two = ttk.Radiobutton(self, text='INICIAR SESION', value=2,
                                      variable=self.var_rb, takefocus=0, command=self.frame_rb_two)
        self.separator = ttk.Separator(self, orient='horizontal')

        # CONFIGURACION DE COLUMNAS Y FILAS DEL FRAME PRINCIPAL
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(4, weight=2)

        # Colocar Widgets en FRAME(SELF) Utilizando GRID
        self.lb_title.grid(row=0, column=0, columnspan=3, sticky='ew', pady=20)
        self.rb_one.grid(row=1, column=1, sticky='nsew')
        self.rb_two.grid(row=2, column=1, sticky='nsew')
        self.separator.grid(row=3, column=0, sticky='nsew',
                            columnspan=3, pady=25)

        self.frame_rb_one()

        # SE UBICA EL FRAME PRINCIPAL
        self.config(style='TFrame',  padding=(50, 10, 50, 10))
        self.pack(side='top', fill='both', expand=True)

    # Este metodo crea el frame para la opcion 1 CREAR NUEVA CUENTA

    def frame_rb_one(self):

        var_entry = tk.StringVar()
        var_entry_two = tk.StringVar()
        var_entry_three = tk.StringVar()
        var_entry_four = tk.StringVar()

        frame = ttk.Frame(self, style='BD.TFrame')

        frame.columnconfigure(0, weight=1)
        # frame.columnconfigure(1, weight=1)
        # frame.columnconfigure(2, weight=1)
        frame.columnconfigure(3, weight=1)
        frame.columnconfigure(6, weight=1)

        # Widgets de frame opcion 1
        lb = ttk.Label(frame, text='REGISTRA TUS DATOS',
                       style='HEADING.TLabel')
        lb_name = ttk.Label(frame, text='Nombre', style='FORM.TLabel')
        entry_name = ttk.Entry(frame, style='E.TEntry', width=25, font=(
            'Cascadia Code PL', 10, 'normal'), takefocus=1, textvariable=var_entry)

        lb_user = ttk.Label(
            frame, text='Nombre\nde usuario', style='FORM.TLabel')
        entry_user = ttk.Entry(frame, style='E.TEntry', width=25, font=(
            'Cascadia Code PL', 10, 'normal'), takefocus=1, textvariable=var_entry_two)

        lb_email = ttk.Label(frame, text='Email', style='FORM.TLabel')
        entry_email = ttk.Entry(frame, style='E.TEntry', width=25, font=(
            'Cascadia Code PL', 10, 'normal'), takefocus=1, textvariable=var_entry_three)

        lb_password = ttk.Label(frame, text='Contraseña', style='FORM.TLabel')
        entry_password = ttk.Entry(frame, style='E.TEntry', width=25, font=(
            'Cascadia Code PL', 10, 'normal'), takefocus=1, textvariable=var_entry_four)
        btn_crear_cuenta = ttk.Button(frame, text='CREAR CUENTA', style='TButton', takefocus=0, command=lambda: self.crear_cuenta(
            var_entry.get().strip(), var_entry_two.get().strip(), var_entry_three.get().strip(), var_entry_four.get().strip()))

        # ubicacion de widgets de frame opcion 1 con PACK
        lb.grid(row=0, column=0, columnspan=7, pady=40)
        lb_name.grid(row=1, column=1, pady=3, sticky='ew')
        entry_name.grid(row=1, column=2, pady=3, sticky='ew')
        lb_user.grid(row=1, column=4, pady=3, sticky='ew')
        entry_user.grid(row=1, column=5, pady=3, sticky='ew')
        lb_email.grid(row=2, column=1, pady=3, sticky='ew')
        entry_email.grid(row=2, column=2, pady=3, sticky='ew')
        lb_password.grid(row=2, column=4, pady=3, sticky='ew')
        entry_password.grid(row=2, column=5, pady=3, sticky='ew')
        btn_crear_cuenta.grid(row=3, column=0, columnspan=7, pady=50)

        frame.bind('<Button-1>', lambda x: self.focus_force())
        frame.grid(row=4, column=0, columnspan=3,
                   sticky='nsew', pady=30, padx=200)

    # Este metodo crea el frame para la opcion 2 INICIAR SESION

    def frame_rb_two(self):

        var_entry_email = tk.StringVar()
        var_entry_password = tk.StringVar()

        frame = ttk.Frame(self, style='BD.TFrame')
        frame.propagate(0)

        # Widgets de frame opcion 1
        lb = ttk.Label(frame, text='INICIAR SESION', style='HEADING.TLabel')

        lb_user = ttk.Label(frame, text='Usuario', style='FORM.TLabel')
        entry_user = ttk.Entry(frame, style='E.TEntry', width=25, font=(
            'Cascadia Code PL', 10, 'normal'), takefocus=1, textvariable=var_entry_email)

        lb_password = ttk.Label(frame, text='Contraseña', style='FORM.TLabel')
        entry_password = ttk.Entry(frame, style='E.TEntry', textvariable=var_entry_password, width=25, font=(
            'Cascadia Code PL', 10, 'normal'), takefocus=1)

        btn_login = ttk.Button(frame, text='INICIAR SESION', style='TButton', takefocus=0, command=lambda: self.iniciar_sesion(
            var_entry_email.get().strip(), var_entry_password.get().strip()))

        # ubicacion de widgets de frame opcion 1 con PACK
        lb.pack(side='top', pady=40)
        lb_user.pack(side='top')
        entry_user.pack(side='top')
        lb_password.pack(side='top')
        entry_password.pack(side='top')
        btn_login.pack(side='top', pady=40)

        frame.bind('<Button-1>', lambda x: self.focus_force())
        frame.grid(row=4, column=0, columnspan=3,
                   sticky='nsew', pady=30, padx=200)

    def validar_inputs(self, *inputs, tipo='register'):

        vacios = [
            len(i) == 0 or i.isspace() for i in inputs
        ]

        if all(vacios):
            return 'RELLENAR LOS DATOS POR FAVOR'

        if any(vacios):
            return 'TE FALTA COMPLETAR ALGUNOS DATOS'

        usuarios = [i[0]
                    for i in self.DB.get_name_users('usuarios', 'usuarios')]

        if tipo == 'login':

            if inputs[0] not in usuarios:
                return 'No existe usario registrdo con ese nombre'

            existe = self.DB.comprobar_login('usuarios', 'usuarios', inputs[0])

            if not (existe[0] == inputs[1]):
                return 'Contraseña Incorrecta'

        else:

            if inputs[1] in usuarios:
                return 'Ya existe ese nombre de usuario\nPrueba con otro'

        return True

    def crear_cuenta(self, nombre, user, email, password):

        validos = self.validar_inputs(nombre, user, email, password)
        if validos != True:
            messagebox.showerror('Error al crear cuenta', validos)

        else:
            datos = (nombre, user, email, password, user)
            # INSERTAMOS NUEVO USUARIO A LA TABLA USUARIOS
            sentencia_sql = '''
                INSERT INTO usuarios (
                    nombre,
                    usuario,
                    email,
                    password,
                    database
                )
                VALUES (
                    ?, ?, ?, ?, ?
                )
            '''

            self.DB.write('usuarios', datos, sentencia_sql)

            window_perfil(self.master, user)

    def iniciar_sesion(self, user, password):

        validos = self.validar_inputs(user, password, tipo='login')
        if validos != True:

            messagebox.showerror('Error al iniciar sesion', validos)

        else:

            window_perfil(self.master, user)

    def crear_tabla_usuarios(self):

        sentencia_sql = '''
                CREATE TABLE IF NOT EXISTS usuarios (
                    nombre TEXT NOT NULL,
                    usuario TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL,
                    database TEXT NOT NULL
                )
            '''

        self.DB.crear_tabla('usuarios', sentencia_sql)  # CREAMOS LA TABLA


""" 
*|> Clase de la ventana prinicpal del programa , que contendra varios metodos para trabajar en esta ventana <|*
"""


class MainWindow(ttk.Frame):

    def __init__(self, master, database, **kwarg):
        super().__init__(master, **kwarg)

        self.master = master
        self.database = database
        # Instaciamos la clase DataBase de modulo conexion para trabajar con el CRUD del programa
        self.DB = conexion.DataBase()
        self.DB.conectar(self.database)

        self.master.title('🔰 Gestiona Contraseñas')
        self.master.configure(cursor='circle')
        #path_ico = resource_path(r'.\icono.ico')
        # self.master.iconbitmap(path_ico)

        # Creamos variables
        self.var_rb = tk.IntVar(value=1)

        self.styles = Styles(master)  # Instaciamos los estilos definidos
        # Definimos Widgets
        self.lb_title = ttk.Label(
            self, text='GESTOR DE CONTRASEÑAS', style='HEADING.TLabel')
        self.rb_one = ttk.Radiobutton(self, text='CREAR NUEVA TABLA DE CREDENCIALES',
                                      value=1, variable=self.var_rb, takefocus=0, command=self.frame_rb_one)
        self.rb_two = ttk.Radiobutton(self, text='ABRIR TABLA EXISTENTE DE CREDENCIALES',
                                      value=2, variable=self.var_rb, takefocus=0, command=self.frame_rb_two)
        self.separator = ttk.Separator(self, orient='horizontal')

        # CONFIGURACION DE COLUMNAS Y FILAS DEL FRAME PRINCIPAL
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(4, weight=2)

        # Colocar Widgets en FRAME(SELF) Utilizando GRID
        self.lb_title.grid(row=0, column=0, columnspan=3, sticky='ew', pady=20)
        self.rb_one.grid(row=1, column=1, sticky='nsew')
        self.rb_two.grid(row=2, column=1, sticky='nsew')
        self.separator.grid(row=3, column=0, sticky='nsew',
                            columnspan=3, pady=25)

        self.frame_rb_one()

        # EVENTOS PARA WIDGETS
        self.bind('<Button-1>', lambda x: self.focus_force())

        # UBICAMOS EL FRAME PARA QUE OCUPE TODA LA VENTANA
        self.config(style='TFrame',  padding=(50, 10, 50, 10))
        self.pack(fill='both', expand=1, padx=10, side='top')

    # Este metodo crea el frame para la opcion 1 CREAR NUEVA TABLA

    def frame_rb_one(self):

        var_entry = tk.StringVar()

        frame = ttk.Frame(self, style='BD.TFrame')

        # Widgets de frame opcion 1
        lb = ttk.Label(frame, text='NOMBRE DE NUEVA TABLA',
                       style='HEADING.TLabel')
        entry = ttk.Entry(frame, style='TEntry', width=25, font=(
            'Cascadia Code PL', 15, 'normal'), takefocus=0, textvariable=var_entry)
        btn_crear_table = ttk.Button(frame, text='CREAR TABLA', style='TButton', takefocus=0,
                                     command=lambda: self.show_tabla(var_entry.get().strip(), frame, error))
        error = ttk.Label(frame, style='ERROR.TLabel',
                          background=self.styles.theme[self.styles.theme_use]['bg'])

        # ubicacion de widgets de frame opcion 1 con PACK
        lb.pack(side='top', pady=40)
        entry.pack(side='top')
        btn_crear_table.pack(side='top', pady=50)
        error.pack(side='top')

        frame.bind('<Button-1>', lambda x: self.focus_force())
        frame.grid(row=4, column=0, columnspan=3,
                   sticky='nsew', pady=30, padx=200)

    # Este metodo crea el frame para la opcion 2 ABRIR TABLA

    def frame_rb_two(self):

        frame = ttk.Frame(self, style='BD.TFrame')
        frame.propagate(0)

        # Widgets de frame opcion 2
        lb = ttk.Label(frame, text='SELECCIONAR TABLA', style='HEADING.TLabel')
        self.tablas = ttk.Combobox(frame, style='TCombobox', state='readonly', font=(
            'Cascadia Code PL', 15, 'normal'))
        self.tablas['values'] = self.DB.get_num_tablas(self.database)
        self.tablas.set('Seleccionar')
        btn_abrir_table = ttk.Button(frame, text='ABRIR TABLA', style='TButton', takefocus=0,
                                     command=lambda: self.show_tabla(self.tablas.get().strip(), frame, error, 'abrir'))
        error = ttk.Label(frame, style='ERROR.TLabel',
                          background=self.styles.theme[self.styles.theme_use]['bg'])

        # ubicacion de widgets de frame opcion 1 con PACK
        lb.pack(side='top', pady=40)
        self.tablas.pack(side='top')
        btn_abrir_table.pack(side='top', pady=50)
        error.pack(side='top')

        frame.bind('<Button-1>', lambda x: self.focus_force())
        frame.grid(row=4, column=0, columnspan=3,
                   sticky='nsew', pady=30, padx=200)

    # Metodo que se llamara al presionar el boton CREAR TABLA o ABRIR TABLA En cualquiera de los casos comprobara si todo esta bien para mostrar la tabla de contraseñas

    def show_tabla(self, nameTabla, frame, variable, accion='write'):

        llave = False

        if accion == 'write':

            tablas = self.DB.get_num_tablas(self.database)

            if nameTabla.isspace() or len(nameTabla) == 0:
                llave = True
                frame.after(10, lambda: self.mensaje_error(
                    'Escoge un nombre\nPara la tabla', 0, bg='red', frame=frame, fg='black', variable=variable))

            elif nameTabla in tablas:
                llave = True
                frame.after(10, lambda: self.mensaje_error(
                    'Ya existe una tabla\nCon ese nombre', 0, bg='red', frame=frame, fg='white', variable=variable))

            else:
                chars = strg.punctuation
                llave_char = False
                for char in chars:
                    if char in nameTabla:
                        llave_char = True
                        break

                if (llave_char):
                    llave = True
                    frame.after(10, lambda: self.mensaje_error(
                        'No deberias incluir\nsignos de puntuacion', 0, bg='red', frame=frame, fg='black', variable=variable))

                else:
                    self.crear_tabla(nameTabla)  # Creamos la tabla

        else:

            if nameTabla == 'Seleccionar':
                llave = True
                frame.after(10, lambda: self.mensaje_error(
                    'Escoge\nUna tabla', 0, bg='red', frame=frame, fg='black', variable=variable))

        # AL NO OCURRIR NINGUN ERROR DE VALIDACION Y QUE LA VARIABLE LLAVE SIGA EN FALSE SE PROCEDE A EJECUTAR LA SEGUNDA VENTANA
        if not (llave):
            window_Tabla(self.master, self.database, nameTabla)

    # METODO PARA CREAR UNA TABLA UTILIZANDO EL MODULO conexion Y LA CLASE DataBase

    def crear_tabla(self, nameTabla):

        sentencia_sql = f'''
                        CREATE TABLE {nameTabla!r} (
                            id INTEGER,
                            nombre TEXT NOT NULL,
                            usuario TEXT,
                            correo_numero TEXT NOT NULL,
                            password TEXT NOT NULL,
                            url TEXT,
                            descripcion TEXT
                        )
                    '''
        verificar = self.DB.crear_tabla(self.database, sentencia_sql)

    def mensaje_error(self, mensaje, count, **kw):

        if count <= 2:
            kw['variable'].config(
                background=kw['bg'], text=mensaje, foreground=kw['fg'], justify='center')
            kw['frame'].after(
                1000, lambda: self.mensaje_error(mensaje, count + 1, **kw))

        else:
            kw['variable'].config(
                background=self.styles.theme[self.styles.theme_use]['bg'], text='')


class Tabla:

    def __init__(self, master, db, nameTabla) -> None:

        self.master = master
        self.DB = conexion.DataBase()
        self.DB.conectar(db)
        self.database = db
        self.nameTabla = nameTabla

        self.styles = Styles(master)
        # self.styles.style.theme_use('alt')

        self.labelframe = ttk.Labelframe(self.master, style='TLabelframe')

        self.labelframe.columnconfigure(1, weight=1)
        self.labelframe.columnconfigure(3, weight=1)
        self.labelframe.columnconfigure(6, weight=1)
        # self.labelframe.rowconfigure(0, weight=1)
        self.labelframe.rowconfigure(1, weight=1)
        self.labelframe.rowconfigure(2, weight=1)
        self.labelframe.rowconfigure(3, weight=1)
        # self.labelframe.rowconfigure(1, weight=1)

        # WIDGETS
        # BOTON PARA VOLVER A TU PERFIL
        self.btn_volver = ttk.Button(self.labelframe, text='HOME', command= lambda: window_perfil(self.master, self.database))
        self.desplegar_tablas = ttk.Combobox(
            self.labelframe, state='readonly', font=('Cascadia Code PL', 15, 'normal'))
        self.desplegar_tablas['values'] = self.DB.get_num_tablas(self.database)
        self.desplegar_tablas.set(nameTabla)
        self.input_buscar = ttk.Entry(self.labelframe, width=25, font=(
            'Cascadia Code PL', 17, 'normal'), takefocus=1)
        self.btn_buscar = ttk.Button(
            self.labelframe, text='BUSCAR', style='S.TButton')
        self.delete_tabla = ttk.Button(
            self.labelframe, text='ELIMINAR TABLA', style='DG.TButton')

        # TABLA DE DATOS
        self.frame_tabla = ttk.Frame(
            self.labelframe, style='TFrame')

        self.tabla_credenciales = ttk.Treeview(
            self.frame_tabla, show='headings')  # TABLA DE DATOS
        self.scroll_y = ttk.Scrollbar(
            self.frame_tabla, orient='vertical', command=self.tabla_credenciales.yview)
        self.scroll_x = ttk.Scrollbar(
            self.frame_tabla, orient='horizontal', command=self.tabla_credenciales.xview)

        self.tabla_credenciales.tag_configure('gray', background='gray')
        self.tabla_credenciales.tag_configure('skyblue', background='skyblue')

        self.tabla_credenciales.config(
            yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)

        self.tabla_credenciales['columns'] = (
            'NOMBRE', 'USUARIO', 'CORREO O NUMERO', 'CONTRASEÑA', 'URL', 'DESCRIPCION')
        self.tabla_credenciales.column('NOMBRE', minwidth=350, anchor='w')
        self.tabla_credenciales.column('USUARIO', minwidth=350, anchor='w')
        self.tabla_credenciales.column(
            'CORREO O NUMERO', minwidth=380, anchor='w')
        self.tabla_credenciales.column('CONTRASEÑA', minwidth=350, anchor='w')
        self.tabla_credenciales.column('URL', minwidth=350, anchor='w')
        self.tabla_credenciales.column('DESCRIPCION', minwidth=380, anchor='w')

        self.tabla_credenciales.heading('NOMBRE', text='NOMBRE')
        self.tabla_credenciales.heading('USUARIO', text='UUSARIO')
        self.tabla_credenciales.heading(
            'CORREO O NUMERO', text='CORREO O NUMERO')
        self.tabla_credenciales.heading('CONTRASEÑA', text='CONTRASEÑA')
        self.tabla_credenciales.heading('URL', text='URL')
        self.tabla_credenciales.heading('DESCRIPCION', text='DESCRIPCION')

        # FRAME DE BOTONES DE EDIT
        self.frame_footer = ttk.Frame(self.labelframe)
        self.frame_btns = ttk.Frame(self.frame_footer)
        self.frame_legend = ttk.Frame(self.frame_footer)

        # botones eliminar - actualizar - agregar
        self.btn_delete = ttk.Button(
            self.frame_btns, text='-', style='DG.TButton')
        self.btn_update = ttk.Button(self.frame_btns, text='ACTUALIZAR')
        self.btn_add = ttk.Button(self.frame_btns, text='+')
        #  ---------------------------------
        # labels para legend
        self.total = ttk.Label(self.frame_legend, text='TOTAL: 20')
        self.total_select = ttk.Label(
            self.frame_legend, text='SELECCIONADOS: 5')

        # UBICACION DE BOTONES DE FRAME BOTONES
        self.btn_delete.pack(side='left', expand=True, fill='x')
        self.btn_update.pack(side='left', expand=True, fill='x')
        self.btn_add.pack(side='right', expand=True, fill='x')

        # UBICACION DE LABEL DE LEGEND
        self.total.pack(side='left', expand=True, fill='x')
        self.total_select.pack(side='right', expand=True, fill='x')

        # CONFIGURACION DEL FRAME TABLA PARA DARLES PESO A SUS COLUMNAS O FILAS
        self.frame_tabla.columnconfigure(0, weight=1)
        self.frame_tabla.columnconfigure(1, weight=1)
        self.frame_tabla.rowconfigure(0, weight=1)

        self.tabla_credenciales.grid(
            row=0, column=0, sticky='nsew', columnspan=2)
        self.scroll_y.grid(row=0, column=2, sticky='nsew')
        self.scroll_x.grid(row=1, column=0, sticky='nsew', columnspan=2)

        # UBICAMOS WIDGETS
        self.btn_volver.grid(row=0, column=0, sticky='e')
        self.desplegar_tablas.grid(row=0, column=2, sticky='ew')
        self.input_buscar.grid(row=0, column=4, sticky='ew')
        self.btn_buscar.grid(row=0, column=5, sticky='ew')
        self.delete_tabla.grid(row=0, column=7, sticky='ew')

        self.frame_tabla.grid(row=1, column=0, columnspan=8,
                              rowspan=3, sticky='nsew', pady=20)

        # UBICACION DE FRAMES DE FOOTER
        self.frame_btns.pack(side='right')
        self.frame_legend.pack(side='left')

        self.frame_footer.grid(row=4, column=0, columnspan=8, sticky='nsew')

        self.labelframe.pack(side='top', fill='both', expand=True)

    # METODO PARA ABRIR VENTANA MODAL

    def open_modal(self, frame):

        ventana = tk.Toplevel(self.master, highlightthickness=5, highlightbackground='DarkOrchid1',
                              highlightcolor='DarkOrchid1', relief='ridge', bd=5)
        ventana.overrideredirect(1)
        ventana.focus_set()

        frame.config(master=ventana)
        frame.pack(side='top', expand=True, fill='both')

        ventana.grab_set()
        self.master.wait_window(ventana)

    # metodo para crear frame para añdir credencial

    def frame_add_update_credencial(self, boton, titulo, comando, modificar):

        self.var_btn_key = tk.StringVar()
        self.varName = tk.StringVar()
        self.varCorreo = tk.StringVar()
        self.var_error1 = tk.StringVar()
        self.var_error2 = tk.StringVar()
        self.var_error3 = tk.StringVar()

        # if boton == 'ACTUALIZAR' or modificar:
        #     id = self.tabla_credenciales.selection()
        #     fila = self.db.read(
        #         F'SELECT * FROM {self.nameTabla} WHERE ID="{id[0]}"')
        #     self.varName.set(fila[0][1])
        #     self.varCorreo.set(fila[0][2])
        #     self.var_btn_key.set(fila[0][3])

        self.frame_add_update_credencial = ttk.Frame()
        # ||||
        self.frame_add_update_credencial.columnconfigure(0, weight=1)
        self.frame_add_update_credencial.columnconfigure(1, weight=1)
        self.frame_add_update_credencial.columnconfigure(2, weight=1)
        self.frame_add_update_credencial.columnconfigure(4, weight=1)
        # ||||
        self.new = ttk.Label(self.frame_add_update_credencial, text=titulo)
        self.label1 = ttk.Label(
            self.frame_add_update_credencial, text='NOMBRE')
        self.nombre_credencial = ttk.Entry(
            self.frame_add_update_credencial, textvariable=self.varName, font=('Cascadia Code PL', 12, 'normal'))
        self.error1 = ttk.Label(
            self.frame_add_update_credencial, textvariable=self.var_error1)
        self.label2 = ttk.Label(
            self.frame_add_update_credencial, text='CORREO O NUMERO')
        self.correo_credencial = ttk.Entry(
            self.frame_add_update_credencial, textvariable=self.varCorreo, font=('Cascadia Code PL', 12, 'normal'))
        self.error2 = ttk.Label(self.frame_add_update_credencial, textvariable=self.var_error2)
        self.label3 = ttk.Label(self.frame_add_update_credencial, text='CONTRASEÑA')
        self.key_credencial = ttk.Entry(
            self.frame_add_update_credencial, textvariable=self.var_btn_key, font= ('Cascadia Code PL', 12, 'normal'))
        self.img_crear_key = ttk.Button(self.frame_add_update_credencial, image=self.imagen,
                                        anchor='w', relief='flat')
        self.error3 = ttk.Label(self.frame_add_update_credencial, textvariable=self.var_error3)
        self.btn = ttk.Button(self.frame_add_update_credencial,
                              text=boton)

        self.btn_cancel = ttk.Button(self.frame_add_update_credencial, text='Cancelar', command=lambda: [self.frame_add_update_credencial.pack_forget(), self.logo_password.pack(
            side='top', fill='both', expand=1, padx=5, pady=2)])

        self.new.grid(row=0, columnspan=3, column=1, pady=15,
                      sticky='nsew', padx=50, ipady=8)
        self.label1.grid(row=1, column=1, columnspan=3, sticky='nsew', pady=7)
        self.nombre_credencial.grid(
            row=2, column=1, columnspan=3, sticky='nsew', ipady=2)
        self.error1.grid(row=3, column=1, columnspan=3, sticky='ne')
        self.label2.grid(row=4, column=1, columnspan=3, sticky='nsew', pady=5)
        self.correo_credencial.grid(
            row=5, column=1, columnspan=3, sticky='nsew', ipady=2)
        self.error2.grid(row=6, column=1, columnspan=3, sticky='ne')
        self.label3.grid(row=7, column=1, columnspan=3, sticky='nsew', pady=5)
        self.key_credencial.grid(row=8, column=1, columnspan=2, sticky='nsew')
        self.img_crear_key.grid(row=8, column=3)
        self.error3.grid(row=9, column=1, columnspan=3, sticky='ne')
        self.btn.grid(row=10, column=1, columnspan=1,
                      pady=15, sticky='nsew', padx=1)
        self.btn_cancel.grid(row=10, column=2, pady=15,
                             sticky='nsew', columnspan=2, padx=1)

    def add_credencial(self):
        pass


def window_perfil(master, database):

    master.destroy()
    master.quit()

    ventana = tk.Tk()
    ventana.geometry('1000x780+250+8')
    ventana.minsize(1000, 780)
    ventana.focus_force()
    MainWindow(ventana, database)
    ventana.mainloop()


def window_Tabla(master, database, nameTabla):

    master.destroy()
    master.quit()

    ventana = tk.Tk()
    ventana.geometry('1400x780+50+8')
    ventana.state('zoomed')
    ventana.minsize(1400, 780)
    Tabla(ventana, database, nameTabla)
    ventana.mainloop()


if __name__ == '__main__':

    # main()
    ventana = tk.Tk()

    ventana.geometry('1200x780+170+8')
    ventana.minsize(1200, 780)

    NuevoUsuario(ventana)

    ventana.mainloop()
