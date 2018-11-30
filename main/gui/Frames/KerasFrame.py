'''



'''

from tkinter import *
from tkinter import ttk
from main.gui.Utilities.Settings import Settings


class KerasFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, master=parent,bg=Settings.BACKGROUND_COLOR.value)
        self.pack()
        self.components = []
        self.layers = []


        mainFrame = Frame(self,bg=Settings.BACKGROUND_COLOR.value)
        mainFrame.pack(padx=10, pady=10)

        networkConfigsFrame = Frame(mainFrame,bg=Settings.BACKGROUND_COLOR.value)
        networkConfigsFrame.pack()

        networkTypeFrame = Frame(networkConfigsFrame,bg=Settings.BACKGROUND_COLOR.value)
        networkTypeFrame.pack(padx=10, pady=10)

        modelTypeLabel = Label(networkTypeFrame, fg=Settings.FONT_COLOR.value, text="Type:",bg=Settings.BACKGROUND_COLOR.value)
        modelTypeLabel.pack(side="left")
        modelTypeConfig = ttk.Combobox(networkTypeFrame, state='readonly', values=['Sequential'])
        modelTypeConfig.pack(side="left")

        networkMetricFrame = Frame(networkConfigsFrame,bg=Settings.BACKGROUND_COLOR.value)
        networkMetricFrame.pack(padx=10, pady=10)
        modelMetricLabel = Label(networkMetricFrame, fg=Settings.FONT_COLOR.value, bg=Settings.BACKGROUND_COLOR.value, text="Metric:")
        modelMetricLabel.pack(side="left")
        modelMetricConfig = ttk.Combobox(networkMetricFrame, state='readonly', values=['accuracy'])
        modelMetricConfig.pack(side="left")

        networkEpochsFrame = Frame(networkConfigsFrame,bg=Settings.BACKGROUND_COLOR.value)
        networkEpochsFrame.pack(padx=10, pady=10)
        modelEpochsLabel = Label(networkEpochsFrame, fg=Settings.FONT_COLOR.value, bg=Settings.BACKGROUND_COLOR.value, text="Epochs:")
        modelEpochsLabel.pack(side="left")
        modelEpochsConfig = Entry(networkEpochsFrame)
        modelEpochsConfig.pack(side="left")

        networkBatchsFrame = Frame(networkConfigsFrame,bg=Settings.BACKGROUND_COLOR.value)
        networkBatchsFrame.pack(padx=10, pady=10)
        modelBatchLabel = Label(networkBatchsFrame, fg=Settings.FONT_COLOR.value, bg=Settings.BACKGROUND_COLOR.value, text="Batch Size:")
        modelBatchLabel.pack(side="left")
        modelBatchConfig = Entry(networkBatchsFrame)
        modelBatchConfig.pack(side="left")

        self.components.append([modelTypeConfig, modelMetricConfig, modelEpochsConfig, modelBatchConfig])

        layersFrame = Frame(mainFrame,bg=Settings.BACKGROUND_COLOR.value)
        layersFrame.pack(padx=10, pady=10)

        addLayerButton = Button(networkConfigsFrame, text="Add Layer", bg=Settings.REGULAR_BUTTON1_COLOR.value, command=lambda: self.addLayer(layersFrame, self.layers))
        addLayerButton.pack(padx=10, pady=10)

        self.addLayer(layersFrame, self.layers)

    def addLayer(self, layersFrame, layers):
        newLayerFrame = Frame(layersFrame,bg=Settings.BACKGROUND_COLOR.value)
        newLayerFrame.pack()

        layerTypeFrame = Frame(newLayerFrame,bg=Settings.BACKGROUND_COLOR.value)
        layerTypeFrame.pack(padx=10, pady=10)
        layerTypeLabel = Label(layerTypeFrame, fg=Settings.FONT_COLOR.value, text="Type:",bg=Settings.BACKGROUND_COLOR.value)
        layerTypeLabel.pack(side="left")
        layerTypeConfig = ttk.Combobox(layerTypeFrame, state='readonly', values=['Dense', 'Conv 1D'])
        layerTypeConfig.pack(side="left")

        layerNodesFrame = Frame(layersFrame,bg=Settings.BACKGROUND_COLOR.value)
        layerNodesFrame.pack(padx=10, pady=10)
        layerNodesLabel = Label(layerNodesFrame, fg=Settings.FONT_COLOR.value, text="Nodes",bg=Settings.BACKGROUND_COLOR.value)
        layerNodesLabel.pack(side="left")
        layerNodesEntry = Entry(layerNodesFrame)
        layerNodesEntry.pack(side="left")

        layerActivationFrame = Frame(newLayerFrame,bg=Settings.BACKGROUND_COLOR.value)
        layerActivationFrame.pack(padx=10, pady=10)
        layerActivationLabel = Label(layerActivationFrame, fg=Settings.FONT_COLOR.value, text="Activation:",bg=Settings.BACKGROUND_COLOR.value)
        layerActivationLabel.pack(side="left")
        layerActivationConfig = ttk.Combobox(layerActivationFrame, state='readonly', values=['relu','softmax','sigmoid'])
        layerActivationConfig.pack(side="left")

        layers.append([layerTypeConfig, layerNodesEntry, layerActivationConfig])

    def get(self):
        model = []
        model.append([self.components[0][0].get(), self.components[0][1].get(), int(self.components[0][2].get()), int(self.components[0][3].get())])
        for layer in self.layers:
            model.append({"Type": layer[0].get(), "Nodes": int(layer[1].get()), "Activation": layer[2].get()})
        print(model)
        return model
