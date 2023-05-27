#!/usr/bin/env python

import itk
import argparse

parser = argparse.ArgumentParser(description="Compute RBG Image To Grayscale Image.")
parser.add_argument("input_image")
parser.add_argument("output_image")
args = parser.parse_args()

Dimension = 2

ComponentType = itk.UC
InputPixelType = itk.RGBPixel[ComponentType]
InputImageType = itk.Image[InputPixelType, Dimension]

OutputPixelType = itk.UC
OutputImageType = itk.Image[OutputPixelType, Dimension]

reader = itk.ImageFileReader[InputImageType].New()
reader.SetFileName(args.input_image)

rgbFilter = itk.RGBToLuminanceImageFilter.New(reader)

writer = itk.ImageFileWriter[OutputImageType].New()
writer.SetFileName(args.output_image)
writer.SetInput(rgbFilter.GetOutput())

writer.Update()
