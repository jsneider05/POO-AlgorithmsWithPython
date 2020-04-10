from bokeh.plotting import figure, output_file, show
# figure -> ventana donde vamos a graficas
# output_file -> permitir determinar el nombre del archivo que vamos a tener como output
# show -> generar servidor que se prende y muestra el archivo html en el browser

if __name__ == "__main__":
    output_file('graficado_simple.html')
    fig = figure()

    total_vals = int(input('Cuantos valores quieres graficar? '))

    x_val = list(range(total_vals))
    y_val = []

    for x in x_val:
      val = int(input(f'Valor y para {x} '))
      y_val.append(val)

    fig.line(x_val, y_val, line_width=2)
    show(fig)
