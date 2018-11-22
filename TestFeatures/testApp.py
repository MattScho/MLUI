from tkinter import *
from tkinter import ttk

def addLayer(layersFrame, layers):
    newLayerFrame = Frame(layersFrame)
    newLayerFrame.pack()

    layerTypeLabel = Label(newLayerFrame, text="Type:")
    layerTypeLabel.pack(side="left")
    layerTypeConfig = ttk.Combobox(newLayerFrame, state='readonly', values=['Dense'])
    layerTypeConfig.pack(side="left")

    layers.append([layerTypeConfig])

def compileModel(components, layers):
    model = []
    model.append([components[0][0].get(), components[0][1].get()])
    for layer in layers:
        model.append([layer[0].get()])
    print(model)


components =[]
layers = []

root = Tk()

mainFrame = Frame(root)
mainFrame.pack()

networkConfigsFrame = Frame(mainFrame)
networkConfigsFrame.pack()

networkTypeFrame = Frame(networkConfigsFrame)
networkTypeFrame.pack()

modelTypeLabel = Label(networkTypeFrame, text="Type:")
modelTypeLabel.pack(side="left")
modelTypeConfig = ttk.Combobox(networkTypeFrame, state='readonly', values=['Sequential'])
modelTypeConfig.pack(side="left")

networkMetricFrame = Frame(networkConfigsFrame)
networkMetricFrame.pack()
modelMetricLabel = Label(networkMetricFrame, text="Metric:")
modelMetricLabel.pack(side="left")
modelMetricConfig = ttk.Combobox(networkMetricFrame, state='readonly', values=['accuracy'])
modelMetricConfig.pack(side="left")

components.append([modelTypeConfig, modelMetricConfig])

layersFrame = Frame(mainFrame)
layersFrame.pack()

addLayerButton = Button(networkConfigsFrame,text="Add Layer", command=lambda:addLayer(layersFrame, layers))
addLayerButton.pack()

addLayer(layersFrame, layers)

compileBtnFrame = Frame(mainFrame)
compileBtnFrame.pack()

compileButton = Button(compileBtnFrame, text="Compile Model", command=lambda:compileModel(components, layers))
compileButton.pack()

root.mainloop()
