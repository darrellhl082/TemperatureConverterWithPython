import tkinter as tk
from tkinter import font
# Class
class celsius():
    kelvin = lambda deg: deg + 273
    fahrenheit = lambda deg: (deg * 9/5) + 32
    reamur = lambda deg : deg * 4/5
    celsius = lambda deg : deg
class fahrenheit():
    celsius = lambda deg : (deg - 32) * 5/9
    kelvin = lambda deg : celsius.kelvin(fahrenheit.celsius(deg))
    reamur = lambda deg : celsius.reamur(fahrenheit.celsius(deg))
    fahrenheit = lambda deg : deg
class kelvin():
    celsius = lambda deg: deg - 273
    fahrenheit = lambda deg: celsius.fahrenheit(kelvin.celsius(deg))
    reamur = lambda deg: celsius.reamur(kelvin.celsius(deg))
    kelvin = lambda deg : deg
class reamur():
    celsius = lambda deg : deg * 5/4
    fahrenheit = lambda deg: celsius.fahrenheit(reamur.celsius(deg))
    kelvin = lambda deg : celsius.kelvin(reamur.celsius(deg))
    reamur = lambda deg : deg


# Function
def answer(toKelvin,toFahrenheit,toReamur,toCelsius):
        global ans
        textAns = f"{toKelvin:.3} K  {toFahrenheit:.3} F  {toReamur:.3} Re  {toCelsius:.3} C"
        ans.config(text = textAns) 
def convert(origin, degree):
    
        if origin == 'celsius':
            toKelvin = celsius.kelvin(degree)
            toFahrenheit = celsius.fahrenheit(degree)
            toReamur = celsius.reamur(degree)
            answer(toKelvin,toFahrenheit,toReamur,degree)
        elif origin =='fahrenheit':
            toKelvin = fahrenheit.kelvin(degree)
            toCelsius = fahrenheit.celsius(degree)
            toReamur = fahrenheit.reamur(degree)
            answer(toKelvin,degree,toReamur,toCelsius)
        elif origin =='reamur':
            toKelvin = reamur.kelvin(degree)
            toFahrenheit = reamur.fahrenheit(degree)
            toCelsius = reamur.celsius(degree)
            answer(toKelvin,toFahrenheit,degree,toCelsius)
        elif origin =='kelvin':
            toCelsius = kelvin.celsius(degree)
            toFahrenheit = kelvin.fahrenheit(degree)
            toReamur = kelvin.reamur(degree)
            answer(degree,toFahrenheit,toReamur,toCelsius)
def main():
    global ans
    origin = org.get()
    degree = float(inputDeg.get())
    convert(origin, degree)
  
# Tkinter
root= tk.Tk()
root.title('TemperatureConverter | darrellhl082-z.ma.af')
canvas = tk.Canvas(root, width = 600, height = 380,  relief = 'raised')
canvas.pack()

# tk Var Declaration
org = tk.StringVar()
values = {
    'Celsius':'celsius',
    'Kelvin':'kelvin',
    'Fahrenheit':'fahrenheit',
    'Reamur':'reamur'
}

rdBtn = 100

# Structure declaration
h1 = tk.Label(root, text='Temperature Converter', font=('helvetica', 18))
inputText = tk.Label(root, text="Pilih satuan suhu yang akan diubah:", font=('helvetica', 14))
for text,values in values.items():
    inputOrg = tk.Radiobutton(root, text=text, variable=org,value=values)
    canvas.create_window(300, rdBtn, window=inputOrg)
    rdBtn += 30
degText = tk.Label(root, text="Masukkan derajat suhu:", font=('helvetica', 14))
inputDeg = tk.Entry(root)
acc = tk.Label(root, text="=", font=('helvetica', 12))
ans=tk.Label(root , font=('helvetica', 12 ))
button = tk.Button(root, text='Get Answer',command=main, bg='blue', fg='white',font=('helvetica', 12)  )


# Tkinter structure
canvas.create_window(300, 30, window=h1)
canvas.create_window(300, 70, window=inputText)
canvas.create_window(300, 230, window=degText)
canvas.create_window(300, 255,width= 100 , window=inputDeg)
canvas.create_window(300, 277.5, window=acc)
canvas.create_window(300, 300, window=ans)
canvas.create_window(300, 330, window=button)

# Mainloop
root.mainloop()