import os


PATH_STANDAR = R'C:\Users\SAMIR\MIS_CURSOS\Carrera_De_Desarrollo_de_sistemas\CICLO I'



def make_tem(curso, logro, tema, start, end):
            os.chdir(fr'{PATH_STANDAR}\{curso}\{logro}')

            for i in range(start, end) :
                if os.path.exists(f'{tema}{i+1:02d}'):
                    continue
                os.mkdir(f'{tema}{i+1:02d}')


def make_dir(curso):
    os.chdir(fr'{PATH_STANDAR}\{curso}')
    temas = 5
    logro = 'LOGRO_0'
    tema = 'TEMA_'
    start = 0
    end = 5

    if curso == 'ALGORITMOS_COMPUTACIONALES' :
        temas = 4

    for i in range(3) :
        os.chdir(fr'{PATH_STANDAR}\{curso}')

        if os.path.exists(F'{logro}{i+1}') :

            make_tem(curso, F'{logro}{i+1}', tema, start, end)
            start += 5
            end += 5

            continue

        os.mkdir(f'{logro}{i+1}')
        make_tem(curso, F'{logro}{i+1}', tema, start, end)
        start += 5
        end += 5
            
    
    os.mkdir(f'LOGRO_FINAL')

    



cursos = ['ALGORITMOS_COMPUTACIONALES', 'DISEÑO_WEB', 'LABORATORIO_INTEGRACION_I', 'SOPORTE_TI', 'DESARROLLO_PERSONAL']

for i in cursos:
    make_dir(i)






