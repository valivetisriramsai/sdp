import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot1(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.title('cars')
    plt.bar(x,y)
    plt.xticks(rotation=50)
    plt.xlabel('car')
    plt.ylabel('price')
    plt.tight_layout() 
    graph=get_graph()
    return graph
def get_plot2(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.title('Booking')
    plt.bar(x,y)
    plt.xticks(rotation=50)
    plt.xlabel('car')
    plt.ylabel('return')
    plt.tight_layout() 
    graph=get_graph()
    return graph
def get_plot3(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.title('cars')
    plt.bar (x,y)
    plt.xticks(rotation=50)
    plt.xlabel('car')
    plt.ylabel('status')
    plt.tight_layout() 
    graph=get_graph()
    
    return graph
def get_plot4(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.title('Booking')
    plt.bar(x,y)
    plt.xticks(rotation=50)
    plt.xlabel('car')
    plt.ylabel('return')
    plt.tight_layout() 
    graph=get_graph()
    return graph

