# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:29:10 2017

@author: lm.mejia10
"""

import vtk 

# VTK module is already imported from the previous challenge so we do not need to do it again

# create a reader for your unstructured_grid
ugridReader = vtk.vtkUnstructuredGridReader()
ugridReader.SetFileName("data/exercise_op1.vtk")
ugridReader.Update()

ugrid = ugridReader.GetOutput()
scalarRange = ugrid.GetScalarRange()

# mapper
ugridMapper = vtk.vtkDataSetMapper()
ugridMapper.SetInputData(ugrid)
ugridMapper.SetScalarModeToUseCellData()
#ugridMapper.SetScalarModeToUsePointData()
ugridMapper.SetScalarRange(scalarRange)

# actor
ugridActor = vtk.vtkActor()
ugridActor.SetMapper(ugridMapper)

# create a rendering window and renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.5, 0.5, 0.5)
renderer.AddActor(ugridActor)

renderWindow = vtk.vtkRenderWindow()
renderWindow.SetSize(500, 500)
renderWindow.AddRenderer(renderer)
renderWindow.Render()

# create and enable a renderWindowInteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renderWindow)
iren.Start()