
#!/usr/bin/python3
import sys
import csv
import plotext as plt

def execute_function(file_input: str):
    print("Hello from program")
    days=[]
    values=[]
    with open(file_input, mode="r", encoding="utf-8") as f:
        data = csv.reader(f, delimiter=',', skipinitialspace=True, quotechar='|')
        for row in data:
            try:
                days.append(int(row[0]))
                values.append(float(row[1]))
            except Exception as exc:
                print(exc)
   
    print(days, values)
    plt.date_form('Ymd')
    plt.plot(days,values)
    plt.hline(200, "red+")
    plt.hline(150, "orange+")
    plt.hline(100, "green+")
    plt.canvas_color("black")
    plt.title("Radon")
    plt.xlabel("Days")
    plt.ylabel("[bq/m^3]")
    plt.ylim(0,300)
    plt.show()
                
if __name__ == '__main__':
    if len(sys.argv) == 2:
        execute_function(sys.argv[1])
    else:
        print("Wrong number of arguments, only one file should be passed to this program.")
        print("... Exiting now")
        sys.exit(0)
