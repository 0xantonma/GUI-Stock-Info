from tkinter import *
from GameStop import Stock
from PIL import ImageTk, Image
from tkinter import messagebox
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web


functions = Stock() # Import the classes for results

# Call action functions for results
def stock_price(type):
    index_name = e.get()
    e.delete(0, END)
    data = ""

    if type == 1:
        real_time_price = Stock.realTimePrice(index_name)
        data += f"REAL TIME PRICE {index_name} : ${real_time_price['price']}\n\n"
    elif type == 2:
        time_series = Stock.timeSeries(index_name)

        data += "TIME SERIES: \n\n"

        for item in time_series:
            data += item['datetime'] + " - Open: " + item['open'] + " - High: " + item['high'] + " - Low: " + item[
                'low'] + " - Close: " + item['close'] + " - Volume: " + item['volume'] + "\n"
            data += "--------------------------------------------------------------------\n"
    elif type == 3:
        beta = Stock.betaIndicator(index_name)

        data += "\nBETA INDICATOR: \n\n"
        for item in beta:
            data += item['beta'] + " - " + item['datetime'] + "\n"
    elif type == 4 or type == 5 or type == 6:
        style.use("ggplot")
        start = dt.datetime(2015, 1, 1)
        end = dt.datetime(2021, 7, 28)
        df = web.get_data_yahoo(index_name, start, end)
        df["Adj Close"].plot()
        data += plt.show()

    # Define the frame for results


    resultPage = Toplevel()
    resultPage.title('Results')

    frame = LabelFrame(resultPage, text="Data", padx=5, pady=5)
    text_result = StringVar(resultPage)
    text_display = Label(frame, textvariable=text_result)
    frame.grid(row=0, column=0, columnspan=3, pady=10, padx=20)
    text_display.pack()
    text_result.set(data)

    btn2 = Button(resultPage, text="Close", command=resultPage.destroy).grid(row=1, column=0, columnspan=3, pady=10)






# Confirm user interaction
def confirmAction(val):
    data = messagebox.askyesno("Confirm action", "Are you sure you want to execute this command? Don't forget your API credits are limited.")
    if data == 1:
        stock_price(val)


# Set up the general settings for the program
root = Tk()
root.title("Stock Play")
p1 = PhotoImage(file='img/gme.png')
root.iconphoto(False, p1)
actionType = IntVar() # Search type: time series, real price or beta indicator







# Set up the logo
my_img = ImageTk.PhotoImage(Image.open("img/gme.png"))
my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=2, pady=5, padx=5)


# Create labels, entries & buttons
text_welcome = Label(root, text="Stock Index: (e.g. GME, AAPL, TSLA, BABA)")
e = Entry(root, width=35, borderwidth=5)
button_search = Button(root, text="Search", padx=40, pady=8, command=lambda: confirmAction(actionType.get()))

# Define radio buttons
rbut1 = Radiobutton(root, text="Real-time Price", variable=actionType, value=1)
rbut2 = Radiobutton(root, text="Time series changes (1d)", variable=actionType, value=2)
rbut3 = Radiobutton(root, text="Beta indicator (1d) ", variable=actionType, value=3)
rbut4 = Radiobutton(root, text="Price Graph ", variable=actionType, value=4)





# Grid labels, entries & buttons
text_welcome.grid(row=1, column=0, columnspan=2, padx=35, pady=10)
e.grid(row=2, column=0, columnspan=3, padx=35, pady=10)
button_search.grid(row=10, column=0, columnspan=3, padx=5)


# Frame display



# Display radio buttons
rbut1.grid(row=3, column=0, columnspan=3)
rbut2.grid(row=4, column=0, columnspan=3)
rbut3.grid(row=5, column=0, columnspan=3)
rbut3.grid(row=6, column=0, columnspan=3)
rbut4.grid(row=7, column=0, columnspan=3)






root.mainloop()
