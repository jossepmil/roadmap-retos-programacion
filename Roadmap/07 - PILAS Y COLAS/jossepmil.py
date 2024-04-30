"""Ejercicios"""

#Pila/Stack (LIFO)last in, first out

stack = []
stack.append("1") #push
stack.append("2")
stack.append("3")
print(stack)

#pop
stack_item = stack[len(stack)-1]
del stack[len(stack)-1]
print(stack_item)

print(stack.pop())
print(stack)

#cola/Queue (FIFO)firts in, first out

queue = []

queue.append(1) #push
queue.append(2)
queue.append(3)

#dequeue
queue_item = queue[0]  #first item
del queue[0]
print(queue_item)
print(queue.pop(0))

print(queue)

"""Extra"""

def web_navigation():

    stack = []
    while True:
        action = input("anade un url con palabras adelante/atras/salir: ")
        if action == "salir":
            print("saliendo del navegador")
            break
        elif action == "adelante":
            print()
        elif action == "atras":
            stack.pop()
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"has navegado a:{stack[len(stack)-1]} ")
        else:
            print("Estas en la pagina de inicio")

web_navigation()


def shared_printed():
    queue = []

    while True:
        action = input("anade un documento o selecciona imprimir/salir: ")
        
        if action == "salir":
            break
        elif action == "impirmir":
            if len(queue) > 0:
                print(f"imprimiendo {queue.pop(0)}")
        else:
            queue.append(action)

        print(f"cola de impresion: {queue}")


shared_printed()
