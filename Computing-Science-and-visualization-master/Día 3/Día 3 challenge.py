# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:29:59 2017

@author: lm.mejia10
"""

import vtk 

pl3d = vtk.vtkMultiBlockPLOT3DReader()
xyx_file = "data/combxyz.bin"
q_file = "data/combq.bin"
pl3d.SetXYZFileName(xyx_file)
pl3d.SetQFileName(q_file)
pl3d.SetScalarFunctionNumber(100)
pl3d.SetVectorFunctionNumber(202)
pl3d.Update()

# create a data source
blocks = pl3d.GetOutput()
b0 = blocks.GetBlock(0)
points = vtk.vtkVertexGlyphFilter()
points.SetInputData(b0)
outline = vtk.vtkStructuredGridOutlineFilter()
outline.SetInputData(b0)


# mapper
outlineMapper = vtk.vtkPolyDataMapper()
outlineMapper.SetInputConnection(outline.GetOutputPort())

scalarsMapper = vtk.vtkPolyDataMapper()
scalarsMapper.SetInputConnection(points.GetOutputPort())
scalarsMapper.SetScalarModeToUsePointData()

# actor
outlineActor = vtk.vtkActor()
outlineActor.SetMapper(outlineMapper)
outlineActor.GetProperty().SetColor(1,1,1)

scalarsActor = vtk.vtkActor()
scalarsActor.SetMapper(scalarsMapper)

# create a rendering window and renderer
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderer.SetBackground(0.5, 0.5, 0.5)
renderWindow.AddRenderer(renderer)


# create and enable a renderWindowInteractor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())

renderWindow.SetInteractor(interactor)
renderer.AddActor(outlineActor)
renderer.AddActor(scalarsActor)

interactor.SetRenderWindow(renderWindow)
interactor.Start()